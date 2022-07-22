# Flask-React---Client-Proxy-Admin
---
### Client visits web page - visitors data (user id and page endpoint) sends to proxy server - by web sockets data receive to admin side. Used to be Docker Compose, React Admin, Socket.io, Flask
---
## Client-Server
```
http://127.0.0.1:5001
```
```
Visitng web site pages. Data of current user is saved in cookies. 
Each visited page means that client sends on proxy (Flask) data={'end_user_id': value1, 'web_page_url': value2}.
```
---
## Proxy-Server
```
http://127.0.0.1:6001
```
```
Server waits for request data by REST API.
After post data on the server - with open connection data sends to admin side. 
```
---
## Admin-Server
```
http://127.0.0.1:3000
```
```
Admin side show each message about visitors
```
---
## Start compose
```
docker-compose build
docker-compose up
```
