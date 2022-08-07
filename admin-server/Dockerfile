FROM node:latest

RUN mkdir /admin-app
WORKDIR /admin-app

COPY package.json /admin-app

RUN npm install

EXPOSE 3000

ENTRYPOINT [ "npm" ]
CMD ["start" ]
