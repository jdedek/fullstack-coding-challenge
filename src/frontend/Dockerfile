FROM node:lts-alpine

LABEL maintainer "Julien Dedek <jdedek@posteo.de>"

WORKDIR /app

COPY ./package*.json ./

RUN npm install

COPY . .

CMD ["npm", "run", "serve"]
