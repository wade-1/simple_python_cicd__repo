pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "employee-manager"
        CONTAINER_NAME = "employee-web"
        GIT_SSH_COMMAND = 'ssh -o StrictHostKeyChecking=no'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    // 创建并激活虚拟环境
                    bat 'python -m venv venv'
                    bat '.\\venv\\Scripts\\activate'
                    def mirrors = [
                        'https://mirrors.aliyun.com/pypi/simple',
                        'https://mirrors.cloud.tencent.com/pypi/simple',
                        'https://pypi.org/simple'
                    ]
                    for (mirror in mirrors) {
                        try {
                            bat "pip install --retries 5 --timeout 30 -r requirements.txt -i ${mirror}"
                            bat 'pip install --retries 5 --timeout 30 --upgrade pytest-flask flask -i ${mirror}'
                            success = true
                            break
                        } catch (e) {
                            echo "Mirror ${mirror} failed, trying next..."
                        }
                    }
                    
                    if (!success) {
                        error "All mirrors failed!"
                    }
                    def success = false
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // 初始化测试数据库
                    bat 'python init_db.py'
                    
                    // 设置环境变量
                    bat 'set FLASK_APP=wsgi.py'
                    
                    // 运行测试
                    bat 'pytest --junitxml=test-results.xml'
                    junit 'test-results.xml'
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // 使用当前构建ID作为镜像标签
                    // need to ensure that the Docker daemon is running
                    docker.build("${env.DOCKER_IMAGE}:${env.BUILD_ID}")
                }
            }
        }

        stage('Deploy to Docker') {
            steps {
                script {
                    // 停止并移除旧容器
                    bat "docker stop ${env.CONTAINER_NAME} 2>nul || echo Container not found."
                    bat "docker rm ${env.CONTAINER_NAME} 2>nul || echo Container not found."
                    
                    // 运行新容器
                    docker.image("${env.DOCKER_IMAGE}:${env.BUILD_ID}").run(
                        "--name ${env.CONTAINER_NAME} -d -p 5000:5000"
                    )
                }
            }
        }
    }

    post {
        always {
            script {
                // 清理：删除临时镜像
                bat "docker rmi ${env.DOCKER_IMAGE}:${env.BUILD_ID} || true"
                // 清理虚拟环境
                bat 'rmdir /s /q venv'
            }
        }
        success {
            echo 'Deployment successful! Access the app at: http://localhost:5000'
        }
        failure {
            echo 'Deployment failed! Check the logs for details.'
        }
    }
}