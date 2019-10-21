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
            agent {
                docker {
                    image 'python:3-alpine'
                    image 'mysql'
                }
            }
            steps {
                sh 'python DB_Test.py'
                sh 'docker run --name testdb -e MYSQL_ROOT_PASSWORD='' MYSQL_USER=danilo MYSQL_PASSWORD='' MYSQL_DATABASE=BMI MYSQL_DATABASE=RETIREMENT'
            }
        }
    }
}
