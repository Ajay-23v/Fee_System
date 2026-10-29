pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Syntax Check') {
            steps {
                bat 'python -m compileall -q .'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t fee-system:latest .'
            }
        }
    }

    post {
        success {
            echo 'Fee System pipeline completed successfully!'
        }
        failure {
            echo 'Fee System pipeline failed. Check the console output.'
        }
    }
}