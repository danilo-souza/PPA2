FROM postman/newman

RUN newman run $(pwd)/Unit_Tests.postman_collection.json
