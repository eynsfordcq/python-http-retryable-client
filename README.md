# HttpRetryableClient

`HttpRetryableClient` is a Python class that simplifies making HTTP requests with built-in retry logic and rate limiting. It uses `requests-ratelimiter` for Per-Host Rate Limit Tracking.


## Features

- **Automatic Retries**: Configurable retries for specific HTTP status codes.
- **Backoff Strategy**: Exponential backoff for retries to prevent immediate repeated requests.
- **Rate Limiting**: Limit the number of requests made per second to avoid overwhelming servers or hitting rate limits.


## Installation

You can install the required libraries using pip:

```bash
pip install -r requirements.txt
```


## Usage

Here’s how to use the `HttpRetryableClient`:

```python
from http_retryable_client import HttpRetryableClient

# Create a client instance
client = HttpRetryableClient(request_per_second=5, max_retry=3)

# Making a GET request
response = client.get('https://api.example.com/data')
print(response.json())

# Making a POST request
response = client.post('https://api.example.com/data', json={"key": "value"})
print(response.json())
```