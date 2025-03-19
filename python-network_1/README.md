### `0-hbtn_status.py`
A script that fetches a status URL using the `urllib` package and displays the response body with details about its type and content.

### `1-hbtn_header.py`
Takes a URL as input and displays the value of the `X-Request-Id` header from the response using `urllib`.

### `2-post_email.py`
Sends a POST request with an email parameter to a given URL and displays the response body using `urllib`.

### `3-error_code.py`
Handles HTTP errors when making requests with `urllib`, displaying error codes when they occur.

### `4-hbtn_status.py`
Similar to the first script but uses the more modern `requests` library instead of `urllib`.

### `5-hbtn_header.py`
Retrieves the `X-Request-Id` header from a URL response using the `requests` library.

### `6-post_email.py`
Sends a POST request with an email parameter using the `requests` library.

### `7-error_code.py`
Makes HTTP requests using `requests` and handles error codes without exceptions.

### `8-json_api.py`
Sends a POST request with a letter parameter and processes JSON responses, showing how to work with API data.

### `10-my_github.py`
Uses Basic Authentication with the GitHub API to retrieve a user's ID, demonstrating authenticated API requests.