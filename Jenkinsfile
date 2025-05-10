pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Set up Python Environment') {
            steps {
                bat 'python -m venv venv'
                bat 'call venv\\Scripts\\activate'
                bat 'pip install -r requirements.txt'
            }
        }
        stage('Build Docker Image') {
            steps {
                bat 'docker build -t moja-aplikacja-fastapi .'
            }
        }
        stage('Run Docker Container') {
            steps {
                bat 'docker stop moja-aplikacja-fastapi-kontener || true'
                bat 'docker rm moja-aplikacja-fastapi-kontener || true'
                bat 'docker run -d --name moja-aplikacja-fastapi-kontener -p 12123:12123 moja-aplikacja-fastapi'
            }
        }
    }
}
