pipeline {
    agent any
    environment {
        IMAGE_NAME = 'vincent772/simple-app'
        REGISTRY_CREDENTIALS = 'dockerhub-credentials'
    }
    stages {
        stage('Checkout') { 
            steps { 
                checkout scm 
            } 
        }
        stage('Build') { 
            steps { 
                bat 'echo "Mulai Build Aplikasi di Windows..."' 
            } 
        }
        stage('Build Docker Image') {
            steps { 
                bat '''
                    @echo off
                    set "PATH=C:\\Docker;%PATH%"
                    set "DOCKER_HOST=tcp://localhost:2375"
                    docker build -t %IMAGE_NAME%:%BUILD_NUMBER% .
                '''
            }
        }
        stage('Push Docker Image') {
            steps {
                withCredentials([usernamePassword(credentialsId: REGISTRY_CREDENTIALS,
                usernameVariable: 'USER', passwordVariable: 'PASS')]) {
                    bat '''
                        @echo off
                        set "PATH=C:\\Docker;%PATH%"
                        set "DOCKER_HOST=tcp://localhost:2375"
                        docker login -u %USER% -p %PASS%
                        docker push %IMAGE_NAME%:%BUILD_NUMBER%
                        docker tag %IMAGE_NAME%:%BUILD_NUMBER% %IMAGE_NAME%:latest
                        docker push %IMAGE_NAME%:latest
                    '''
                }
            }
        }
    }
}
