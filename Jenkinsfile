pipeline {
    environment {
        PYTHONPATH = ".;pages"
        }
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/Mujtaba-git/duckduckgo'
            }
        }

        stage('Create virtual environment') {
            steps {
                powershell 'python -m venv .venv'
            }
        }

        stage('Activate virtual environment and install dependencies') {
            steps {
                powershell '.\\.venv\\Scripts\\Activate; pip install -r requirements.txt'
            }
        }

//         stage('Run tests') {
//             steps {
//                 powershell '.\\.venv\\Scripts\\Activate; pytest --junitxml=report.xml'
//             }
//         }

        stage('Run tests') {
            steps {
            sh 'pytest --junitxml=report.xml --html=report.html'
            }
        }

        stage('Publish results') {
            steps {
                junit 'report.xml'
                publishHTML([allowMissing: false, alwaysLinkToLastBuild: true, keepAll: true, reportDir: '.', reportFiles: 'report.html', reportName: 'HTML Report'])
            }
        }
    }
}
