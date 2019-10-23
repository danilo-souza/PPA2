FROM postman/newman

RUN newman run Unit_Tests.postman_collection.json
