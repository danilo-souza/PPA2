FROM postman/newman

RUN apk add nodejs npm
RUN npm install -g newman
