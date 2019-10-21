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
            steps{
                sh 'apk add --no-cache --virtual .build-deps gcc musl-dev'
                sh 'apk add mariadb-dev'
                sh 'pip install mysqlclient'
                sh 'python DB_TESTS.py'
            }
        }
    }
}
