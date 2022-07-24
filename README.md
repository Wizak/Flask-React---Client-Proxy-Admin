# Flask-React-Client-Proxy-Admin
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
Server waits for data from post request using REST API.
After post data on the server - with open connection data receive to admin side. 
```
---
## Admin-Server
```
http://localhost:3000
```
```
Admin side shows each info message about visitors.
```
---
## Begin with Docker
```
Build images
```
```
docker compose build
```
```
Build images, run containers and start
```
```
docker-compose up
```
```
Use this commands for run compose of containers and check solutions.
```

