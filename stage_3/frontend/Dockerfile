FROM node:22-alpine as build

WORKDIR /app

COPY stage_1/frontend/cloud-system-frontend/package.json stage_1/frontend/cloud-system-frontend/package-lock.json ./

RUN npm install

COPY stage_1/frontend/cloud-system-frontend ./

RUN rm -f .env
RUN npm run build 

FROM nginx:alpine3.19

COPY --from=build /app/dist /usr/share/nginx/html
COPY stage_3/frontend/nginx.conf.template etc/nginx/templates/default.conf.template