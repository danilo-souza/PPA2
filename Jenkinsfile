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
                sh 'python -m py_compile BMI.py Retirement.py ShortestDistance.py SplitTheTip.py PPA1.py'
            }
        }
        stage('Test') {
            agent {
                docker {
                    image None
                }
            }
            steps {
                sh 'python Unit_Tests.py'
            }
        }
    }
}
