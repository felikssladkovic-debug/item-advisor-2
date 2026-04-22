FROM node:22-alpine AS site-builder
WORKDIR /build/site
COPY frontend/site/package.json ./
RUN npm install
COPY frontend/site ./
RUN npm run build

FROM node:22-alpine AS admin-builder
WORKDIR /build/admin
COPY frontend/admin/package.json ./
RUN npm install
COPY frontend/admin ./
RUN npm run build

FROM nginx:1.27-alpine
COPY infra/nginx/nginx.conf /etc/nginx/nginx.conf
COPY --from=site-builder /build/site/dist /usr/share/nginx/html/site
COPY --from=admin-builder /build/admin/dist /usr/share/nginx/html/admin

