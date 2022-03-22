FROM node:14-alpine3.12 as base

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
ENV PATH /usr/src/app/node_modules/.bin:$PATH
ENV CHOKIDAR_USEPOLLING true

COPY .npmrc /usr/src/app
COPY package.json /usr/src/app
RUN yarn install

FROM base as local
CMD ["yarn", "start"]

FROM base as prod-build

COPY public /usr/src/app/public
COPY src /usr/src/app/src
RUN yarn build

FROM nginx:1.18-alpine as prod

COPY --from=prod-build /usr/src/app/build /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
