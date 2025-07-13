pipeline {
    agent any
    environment {
        DOCKER_IMAGE = "my-local-app" // 本地镜像名
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm // 拉取 GitHub 代码
            }
        }
    }
}