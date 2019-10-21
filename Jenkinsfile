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
                echo 'Hello'
            }
        }
        stage('Unit_Test') {
            agent {
                docker {
                    image 'python:3-alpine'
                }
            }
            steps {
                sh 'python Unit_Tests.py'
            }
        }
        stage('DB_Test') {
            agent{
                docker{
                    image 'python:3-alpine'
                }
            }
            steps{
                sh 'apk add --no-cache --virtual .build-deps gcc musl-dev'
                sh 'apk add mariadb-dev'
                sh 'pip install mysqlclient'
                sh 'run  run -d --name db -p 3306:3306 -e MYSQL_ROOT_PASSWORD=root MYSQL_USER=danilo MYSQL_PASSWORD=password MYSQL_DATABASE=BMI MYSQL_DATABASE=RETIREMENT mysql'
                sh 'python DB_TESTS.py'
            }
        }
    }
}
