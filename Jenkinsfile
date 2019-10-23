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
                        label 'WebApp' 
                        sh 'ls'
                        
                        sh 'docker run -d --network=Web -v "$(pwd)":"$(pwd)" -w /var/jenkins_home/workspace/PPA2 -p 5000:5000 python:3-alpine "./BMI_RETIREMENT_WEB_TEST.py"'
                        sh 'docker run --network=Web newman run Unit_Tests.json_collection.py postman/newman'
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
