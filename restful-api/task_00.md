# Differences Between HTTP and HTTPS:

## HTTP (Hypertext Transfer Protocol):
A protocol used for transmitting data over the web. It’s unencrypted, meaning the data exchanged between the client and server can be intercepted or tampered with.

## HTTPS (Hypertext Transfer Protocol Secure):
A more secure version of HTTP that uses SSL/TLS encryption to protect data. This ensures that the communication between the client and server is encrypted, preventing interception, tampering, or eavesdropping. It also verifies the identity of the website through certificates issued by trusted authorities.

# Common HTTP Methods and Status Codes:

## HTTP Methods:
**GET**:

Description: Retrieves data from the server.
Use Case: Fetching a webpage or data from an API.

**POST**:

Description: Sends data to the server to create or update a resource.
Use Case: Submitting a form or uploading a file.

**PUT**:

Description: Updates an existing resource or creates a new one if it doesn’t exist.
Use Case: Updating user profile information.

**DELETE**:

Description: Deletes a resource on the server.
Use Case: Removing a user account.

**PATCH**:

Description: Partially updates a resource.
Use Case: Updating one field in a user profile (e.g., changing an email address).

**HEAD**:

Description: Retrieves the headers of a resource without the body.
Use Case: Checking the metadata of a resource without downloading it.

**OPTIONS**:

Description: Describes the communication options for the target resource.
Use Case: Checking which HTTP methods are supported by a server.

# HTTP Status Codes:

## 200 OK:

Description: The request was successful.
Scenario: The requested page is delivered to the user.

## 301 Moved Permanently:

Description: The requested resource has been permanently moved to a new URL.
Scenario: Redirecting to a new page.

## 404 Not Found:

Description: The requested resource could not be found on the server.
Scenario: When a user tries to access a non-existent page.

## 500 Internal Server Error:

Description: The server encountered an unexpected condition that prevented it from fulfilling the request.
Scenario: An error on the server side, such as a misconfigured server.

## 403 Forbidden:

Description: The server understands the request but refuses to authorize it.
Scenario: Accessing a restricted page or resource without proper permissions.

## 502 Bad Gateway:

Description: The server received an invalid response from the upstream server.
Scenario: A server acting as a gateway or proxy fails to get a valid response from an upstream server.

## 503 Service Unavailable:

Description: The server is currently unable to handle the request due to temporary overloading or maintenance.
Scenario: A server is down for maintenance or experiencing high traffic.
