FROM postman/newman

RUN apk add nodejs npm
RUN npm install -g newman

RUN newman run Unit_Tests.postman_collection.json
