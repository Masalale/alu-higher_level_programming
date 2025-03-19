# Python Network #0

## Description
This project focuses on understanding HTTP protocols, making network requests in Python, and learning about web interactions. It covers concepts related to URLs, HTTP methods, headers, and using tools like curl for web requests.

## Scripts and their Functions

### 0-body_size.sh
Takes a URL as input, sends a request and displays the size of the response body in bytes. Uses curl's silent mode to fetch headers and grep to extract the Content-Length.

### 1-body.sh
Sends a GET request to a URL and displays the body of the response, but only if the status code is 200. The flags used ensure it fails silently on errors.

### 2-delete.sh
Sends a DELETE request to the specified URL and displays the response body. Demonstrates how to use HTTP methods beyond GET.

### 3-methods.sh
Queries what HTTP methods a server accepts by sending an OPTIONS request. Extracts and displays just the allowed methods from the response headers.

### 4-header.sh
Sends a GET request with a custom header (X-HolbertonSchool-User-Id: 98) and displays the response body. Shows how to add custom headers to requests.

### 5-post_params.sh
Demonstrates sending POST data by submitting email and subject parameters in the request body and displaying the server's response.