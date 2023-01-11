    FROM node
    WORKDIR /app
    RUN npm install -g nodemon
    COPY package.json package.json 
    RUN npm install
    COPY . .
    EXPOSE 80
    CMD ["nodemon", "server.js"]