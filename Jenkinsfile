pipeline {
    agent any
    environment {
        DOCKER_HUB = credentials('docker-hub-credentials')  // Jenkins中配置的Docker Hub凭据
    }
    stages {
        // 阶段1：拉取代码
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/your-repo/python-jenkins-pipeline.git'
            }
        }
        // 阶段2：设置Python环境
        stage('Setup') {
            steps {
                bat 'python -m venv venv'
                bat 'venv\\Scripts\\pip install -r requirements.txt'
            }
        }
        // 阶段3：运行测试并生成覆盖率报告
        stage('Test') {
            steps {
                bat 'venv\\Scripts\\pytest --cov=app tests/ --cov-report=xml'
            }
            post {
                always {
                    junit '**/test-reports/*.xml'  // 收集测试结果
                    cobertura(coberturaReportFile: '**/coverage.xml')  // 覆盖率报告
                }
            }
        }
        // 阶段4：构建Docker镜像
        stage('Build Docker Image') {
            when {
                branch 'main'
            }
            steps {
                script {
                    docker.build("your-dockerhub-username/python-app:${env.BUILD_ID}")
                }
            }
        }
        // 阶段5：推送镜像到Docker Hub
        stage('Push to Docker Hub') {
            when {
                branch 'main'
            }
            steps {
                script {
                    docker.withRegistry('https://registry.hub.docker.com', 'docker-hub-credentials') {
                        docker.image("your-dockerhub-username/python-app:${env.BUILD_ID}").push()
                    }
                }
            }
        }
    }
    // 阶段6：通知与清理
    post {
        success {
            emailext to: 'team@example.com',
                     subject: "Pipeline Succeeded: ${currentBuild.fullDisplayName}",
                     body: "Details: ${env.BUILD_URL}"
        }
        failure {
            emailext to: 'team@example.com',
                     subject: "Pipeline Failed: ${currentBuild.fullDisplayName}",
                     body: "Check logs at: ${env.BUILD_URL}"
        }
        always {
            cleanWs()  // 清理工作空间
        }
    }
}