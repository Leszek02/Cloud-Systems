FROM node:22-alpine as build

ARG VITE_PORT=5000
ARG VITE_HOST="127.0.0.1"

WORKDIR /app

COPY ../../stage_1/frontend/cloud-system-frontend/package.json ../../stage_1/frontend/cloud-system-frontend/package-lock.json ./

RUN npm install

COPY ../../stage_1/frontend/cloud-system-frontend ./

ENV VITE_PORT=${VITE_PORT}
ENV VITE_HOST=${VITE_HOST}

RUN npm run build 

FROM nginx:alpine3.19

COPY --from=build /app/dist /usr/share/nginx/html