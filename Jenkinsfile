pipeline {
  agent any
  stages {
    stage('Checkout') {
      steps {
        git 'https://github.com/Sujith-sunny/gitpython.git'
      }
    }

    stage('Build') {
      steps {
        sh 'docker build -t Name python_repo:us-east-1/latest'
      }
    }

    stage('Push') {
      steps {
        sh 'docker push 596264129479.dkr.ecr.us-east-1.amazonaws.com/python_repo:latest'
      }
    }
  }
}