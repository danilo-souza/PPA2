FROM postman/newman

RUN newman run Unit_Tests.postman_collections.json
