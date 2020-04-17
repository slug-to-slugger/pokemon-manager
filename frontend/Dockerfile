FROM node:10.15.3-alpine

WORKDIR /var/www/frontend

ENV PATH /app/node_modules/.bin:$PATH

COPY package.json package-lock.json ./

RUN npm install

COPY . ./

CMD ["npm", "start"]