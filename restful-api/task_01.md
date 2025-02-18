# 1. Running curl --version:
This command shows the version of curl installed and lists the protocols it supports.

## Command:

**sh**
```
curl --version
```
**Expected Output:**

**yaml**
```
curl 7.68.0 (x86_64-pc-linux-gnu) libcurl/7.68.0 OpenSSL/1.1.1d zlib/1.2.11
Release-Date: 2020-02-05
Protocols: dict file ftp ftps http https imap imaps pop3 pop3s smtp smtps telnet tftp
Features: AsynchDNS HTTP2 HTTPS-proxy IDN IPv6 Kerberos Largefile NTLM NTLM_WB SSL TLS-SRP UnixSockets
```
Here, you'll see the version of curl, the supported protocols like HTTP, HTTPS, FTP, etc., and the features like HTTP2, SSL, etc.

# 2. Fetching Posts from JSONPlaceholder:

Fetching data from a public API like JSONPlaceholder will return JSON data with multiple posts.

## Command:

**sh**
```
curl https://jsonplaceholder.typicode.com/posts
```
**Expected Output:**

**json**
```
[
  {
    "userId": 1,
    "id": 1,
    "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
    "body": "quia et suscipit\nsuscipit..."
  },
  {
    "userId": 1,
    "id": 2,
    "title": "qui est esse",
    "body": "est rerum tempore vitae\nsequi sint..."
  },
  ...
]
```

This output shows an array of posts. Each post has a userId, id, title, and body.

# 3. Fetching Only Headers:

When you use the -I (capital i) flag with curl, it fetches only the HTTP response headers, not the body.

**Command:**

**sh**
```
curl -I https://jsonplaceholder.typicode.com/posts
```

**Expected Output:**

**yaml**
```
HTTP/1.1 200 OK
Date: Sat, 18 Feb 2025 10:00:00 GMT
Content-Type: application/json; charset=utf-8
Content-Length: 1290
Connection: keep-alive
x-powered-by: Express
```

This output will show the HTTP status code (200 OK), the content type (application/json), content length, and other headers, but no actual post data.

## 4. Making a POST Request:

A POST request sends data to a server. For JSONPlaceholder, even though no actual data is saved, it will simulate a creation and return the newly created post data.

**Command:**

**sh**
```
curl -X POST -H "Content-Type: application/json" \
     -d '{"title": "foo", "body": "bar", "userId": 1}' \
     https://jsonplaceholder.typicode.com/posts
```

**Expected Output:**

**json**
```
{
  "title": "foo",
  "body": "bar",
  "userId": 1,
  "id": 101
}
```
This response confirms the simulated creation of a post with the title, body, and userId you sent, and it adds an id of 101 as the simulated ID.

