pipeline {
    agent any

    stages {

        stage('Clone Repo') {
            steps {
                git 'https://github.com/mkvarshini64-del/devops-project.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t varshinimk/devops-flask-app:v1 .'
            }
        }

        stage('Push Docker Image') {
            steps {
                sh 'docker push varshinimk/devops-flask-app:v1'
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh 'kubectl apply -f k8s/'
            }
        }

    }
}