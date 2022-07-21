FROM node:latest

RUN mkdir /admin-app
WORKDIR /admin-app

COPY package.json /admin-app/

RUN npm install

CMD [ "npm", "start" ]
