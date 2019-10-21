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
                    label 'docker'
                    image 'python:3-alpine'
                    image 'mysql'
                }
            }
            steps{
                sh 'docker -run --name db -p 3306:3306 -e MYSQL_ROOT_PASSWORD=root MYSQL_USER=danilo MYSQL_PASSWORD=password MYSQL_DATABASE=BMI MYSQL_DATABASE=RETIREMENT'
                sh 'python DB_TESTS.py'
            }
        }
    }
}
