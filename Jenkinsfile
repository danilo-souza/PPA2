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
                node{
                    checkout scm

                    docker.image('mysql:5').withRun('-e "MYSQL_ROOT_PASSWORD='' MYSQL_USER=danilo MYSQL_PASSWORD=password MYSQL_DATABASE=BMI MYSQL_DATABASE=RETIREMENT -p 3306:3306"'){c ->
                     sh 'while ! mysqladmin ping -h0.0.0.0 --silent; do sleep 1; done'
                     sh 'python DB_TESTS.py'
                     }
                }
            }
        }
    }
}
