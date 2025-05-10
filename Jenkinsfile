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
        stage('Run Unit Tests') {
           steps {
               //bat 'python -m pytest main.py' // Uruchom testy bezpośrednio z main.py
               bat 'conda run pytest main.py' // Uruchom testy bezpośrednio z main.py
           }
        }
        stage('Build Docker Image') {
            steps {
                bat 'docker build -t moja-aplikacja-fastapi .'
            }
        }
        stage('Run Docker Container') {
            steps {
                script {
                    def containerName = 'moja-aplikacja-fastapi-kontener'
                    def stopCommand = "docker stop ${containerName}"
                    def removeCommand = "docker rm ${containerName}"

                    // Spróbuj zatrzymać kontener i zignoruj błąd, jeśli go nie ma
                    try {
                        bat script: stopCommand
                    } catch (Exception e) {
                        echo "Kontener '${containerName}' nie istnieje lub nie działa."
                    }

                    // Spróbuj usunąć kontener i zignoruj błąd, jeśli go nie ma
                    try {
                        bat script: removeCommand
                    } catch (Exception e) {
                        echo "Kontener '${containerName}' nie istnieje."
                    }

                    // Uruchom nowy kontener
                    bat "docker run -d --name ${containerName} -p 12123:12123 moja-aplikacja-fastapi"
                }
            }
        }
    }
}
