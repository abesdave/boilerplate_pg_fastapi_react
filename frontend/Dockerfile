FROM node:latest as base

WORKDIR /app/
COPY . .

FROM base as dev
EXPOSE 5173
RUN npm install
ENTRYPOINT [ "npm", "run", "dev" ]

FROM base as prod
EXPOSE 3000
RUN bash -c "npm install --production"
RUN bash -c "npm run build"
ENTRYPOINT [ "npm", "run", "serve", "./dist" ]