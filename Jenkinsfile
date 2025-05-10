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
        stage('Check and Remove Existing Conda Environment') {
            steps {
                script {
                    def environmentName = 'myfastapienv' // Zdefiniuj nazwę środowiska jako zmienną
                    def checkEnvCommand = "conda env list | findstr /C:\"${environmentName}\""
                    def envExists = bat(script: checkEnvCommand, returnStatus: true) == 0

                    if (envExists) {
                        echo "Środowisko Conda '${environmentName}' już istnieje. Usuwam..."
                        bat "conda env remove -n ${environmentName} -y"
                    } else {
                        echo "Środowisko Conda '${environmentName}' nie istnieje. Będzie utworzone."
                    }
                }
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
