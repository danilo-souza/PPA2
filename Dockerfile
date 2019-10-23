FROM postman/newman

RUN apk add nodejs npm
RUN npm install -g newman

RUN newman run "https://github.com/danilo-souza/PPA2/blob/master/Unit_Tests.postman_collection.json"
