pipeline {
    agent none
    options {
        skipStagesAfterUnstable()
    }
    stages {
        stage('Build') {
            agent {
                docker {
                    image 'mysql:5.7'
                }
            }
            steps {
                sh 'pip install mysqlclient'
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
                sh 'python DB_TESTS.py'
            }
        }
    }
}
