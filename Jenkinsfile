pipeline {
  agent {
    docker {
      image 'python:3.8'
    }
  }

  stages {
    stage('Build') {
      steps {
        sh 'pip install -r requirements.txt'
        sh 'python Name.py'
      }
    }

    stage('Deploy') {
      steps {
        sh 'docker build -t mydocker .'
        sh 'docker push mydocker'
      }
    }
  }
}