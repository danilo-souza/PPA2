pipeline {
    agent none
    options {
        skipStagesAfterUnstable()
    }
    stages {
        stage('Build') {
            agent {
                docker {
                    image 'python:3-alpine'
                }
            }
            steps {
                sh 'python -m py_compile BMI.py Retirement.py ShortestDistance.py SplitTheTip.py'
            }
        }
        stage('Functional Tests') {
            steps{
                script{
                    node{
                        label 'web test'
                        sh 'pwd'
                        docker.image('python:3-alpine').withRun('-u root -v $(pwd) python "$(pwd)/BMI_RETIREMENT_WEB_TEST.py"'){c ->

                            docker.image('python:3-alpine').inside("--link ${c.id}:db"){
                                sh 'apk add nodejs npm'
                                sh 'npm install -g newman'


                                sh 'newman run Unit_Tests.postman_collection.json'
                            }
                         }
                    }
                }
            }
        }
        stage('DB_Test') {
            steps{
                script{
                    node{
                        label 'database test'
                        docker.image('mysql:5.7').withRun('-p 3306:3306 -e "MYSQL_ROOT_PASSWORD=root" -e "MYSQL_DATABASE=BMI" -e "MYSQL_DATABASE=RETIREMENT"'){c ->
                            docker.image('mysql').inside("--link ${c.id}:db"){
                                sh 'while ! mysqladmin ping -hdb --silent; do sleep 1; done'
     
                            }

                            docker.image('python:3-alpine').inside("--link ${c.id}:db"){
                                sh 'apk add python3-dev'
                                sh 'apk add python-dev mariadb-dev'
                                sh 'apk add --no-cache --virtual .build-deps gcc musl-dev'
                                sh 'pip install mysqlclient'

                        
                                sh 'python3 DB_TESTS.py'
                            }
                         }
                    }
                }
            }
        }
    }
}
