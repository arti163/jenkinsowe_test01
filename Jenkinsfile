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
                sh 'python3 -m venv venv'
                sh 'source venv/bin/activate'
                sh 'pip install -r requirements.txt'
                }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t moja-aplikacja-fastapi .'
                }
        }
        stage('Run Docker Container') {
            steps {
                sh 'docker stop moja-aplikacja-fastapi-kontener || true' // Zatrzymaj istniejący kontener, jeśli istnieje
                sh 'docker rm moja-aplikacja-fastapi-kontener || true'   // Usuń istniejący kontener, jeśli istnieje
                sh 'docker run -d --name moja-aplikacja-fastapi-kontener -p 12123:12123 moja-aplikacja-fastapi'
                }
        }
    }
}
