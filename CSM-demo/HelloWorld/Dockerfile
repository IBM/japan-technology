# reference page: https://nodejs.org/ja/docs/guides/nodejs-docker-webapp/

# base image
FROM node:16

# create application directory
WORKDIR /usr/src/app

# install application dependencied libs
COPY package.json ./
RUN npm install

# bundle application source code to docker image
COPY . .

# mapping to docker daemon
EXPOSE 3000

# start server
CMD ["node", "app.js"]
