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
            steps {
                sh 'python Unit_Tests.py'
            }
        }
    }
}
