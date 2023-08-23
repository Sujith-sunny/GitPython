pipeline {
  agent any
  // environment {
  //   AWS_ACCOUNT_ID="596264129479"
  //   AWS_DEFAULT_REGION="us-east-1"
  //   IMAGE_REPO_NAME="jenkins-pipeline-demo"
  //   IMAGE_TAG="latest"
  //   REPOSITORY_URI = "${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_DEFAULT_REGION}.amazonaws.com/${IMAGE_REPO_NAME}"
  // }
  
  stages {
    stage('Logging into AWS ECR') {
      steps {
          script {
            sh "aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 596264129479.dkr.ecr.us-east-1.amazonaws.com"
          }
                 
      }
    }
    stage('Checkout') {
      steps {
        git 'https://github.com/Sujith-sunny/gitpython.git'
      }
    }

    stage('Build') {
      // steps {
      //   sh 'docker build -t name python_repo:us-east-1/latest'
      //   dockerImage = docker.build "${IMAGE_REPO_NAME}:${IMAGE_TAG}"
      // }
      steps{
        script {
          dockerImage = docker.build "python_repo:latest"
        }
      }
    }

    stage('Push') {
      steps {
        sh "docker tag python_repo:latest 596264129479.dkr.ecr.us-east-1.amazonaws.com/python_repo:latest"
        sh "docker push 596264129479.dkr.ecr.us-east-1.amazonaws.com/python_repo:latest"
      }
    }
  }
}