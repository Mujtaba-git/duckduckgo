pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'REPOSITORY_URL'
            }
        }

        stage('Install dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run tests') {
            steps {
                sh 'pytest --junitxml=report.xml'
            }
        }

        stage('Publish results') {
            steps {
                junit 'report.xml'
            }
        }
    }
}
