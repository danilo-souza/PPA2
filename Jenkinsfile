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
            steps{
                script{
                    node{
                        label 'database test'
                        docker.image('mysql').withRun('--name db -e "MYSQL_ROOT_PASSWORD=root MYSQL_USER=danilo MYSQL_PASSWORD=password MYSQL_DATABASE=BMI MYSQL_DATABASE=RETIREMENT"'){c ->
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
