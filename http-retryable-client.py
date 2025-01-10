from requests.adapters import HTTPAdapter, Retry
from requests_ratelimiter import LimiterSession

class HttpRetryableClient:
    def __init__(
        self, 
        request_per_second = 10, 
        max_retry = 3, 
        backoff_factor = 0.1, 
        status_forcelist=[429, 500, 502, 503, 504]
    ):
        self.request_per_second = request_per_second
        self.max_retry = max_retry
        self.backoff_factor = backoff_factor
        self.status_forcelist = status_forcelist
        self._setup_session()

    def _setup_session(self):
        self.session = LimiterSession(per_second=self.request_per_second)

        # mount retry adapters
        retry_adapter = HTTPAdapter(max_retries=Retry(
            total=self.max_retry,
            backoff_factor=self.backoff_factor,
            status_forcelist=self.status_forcelist)
        )
        self.session.mount("http://", retry_adapter)
        self.session.mount("https://", retry_adapter)
    
    def request(self, method, url, **kwargs):
        response = self.session.request(method, url, **kwargs)
        return response
    
    def get(self, url, **kwargs):
        return self.request("GET", url, **kwargs)
    
    def post(self, url, data=None, json=None, **kwargs):
        return self.request("POST", url, data=data, json=json, **kwargs)
    
    def put(self, url, data=None, **kwargs):
        return self.request("PUT", url, data=data, **kwargs)
    
    def delete(self, url, **kwargs):
        return self.request("DELETE", url, **kwargs)