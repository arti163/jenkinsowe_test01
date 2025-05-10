pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Check Conda Availability') {
            steps {
                bat 'conda --version'
            }
        }
        stage('Create Conda Environment') {
            steps {
                bat 'conda env create -f environment.yml'
            }
        }
        stage('Activate Conda Environment') {
            steps {
                bat 'call conda activate myfastapienv' // Upewnij się, że nazwa pasuje do environment.yml
                bat 'conda info --envs' // Opcjonalnie: wyświetl listę środowisk conda
            }
        }
        stage('Install Dependencies with Conda') {
            steps {
                bat 'conda install -c conda-forge fastapi uvicorn'
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
