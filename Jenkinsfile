pipeline {
    agent any  // 在任何可用节点上运行

    environment {
        // 环境变量定义
        DOCKER_IMAGE = "employee-manager"
        CONTAINER_NAME = "employee-web"
    }

    stages {
        // 阶段1: 获取代码
        stage('Checkout') {
            steps {
                checkout scm  // 从SCM(GitHub)获取代码
            }
        }

        // 阶段2: 安装依赖
        stage('Install Dependencies') {
            steps {
                script {
                    // 创建并激活虚拟环境
                    bat 'python -m venv venv'
                    bat '.\\venv\\Scripts\\activate'
                    
                    // 安装依赖
                    bat 'pip install -r requirements.txt'
                }
            }
        }

        // 阶段3: 运行测试
        stage('Run Tests') {
            steps {
                script {
                    // 运行pytest测试并生成覆盖率报告
                    bat 'pytest --junitxml=test-results.xml'
                    
                    // 保存测试结果
                    junit 'test-results.xml'
                }
            }
        }

        // 阶段4: 构建Docker镜像
        stage('Build Docker Image') {
            steps {
                script {
                    // 使用当前构建ID作为镜像标签
                    docker.build("${env.DOCKER_IMAGE}:${env.BUILD_ID}")
                }
            }
        }

        // 阶段5: 部署到本地Docker
        stage('Deploy to Docker') {
            steps {
                script {
                    // 停止并移除旧容器（如果存在）
                    bat 'docker stop ${env.CONTAINER_NAME} || true'
                    bat 'docker rm ${env.CONTAINER_NAME} || true'
                    
                    // 运行新容器
                    docker.image("${env.DOCKER_IMAGE}:${env.BUILD_ID}").run(
                        "--name ${env.CONTAINER_NAME} -d -p 5000:5000"
                    )
                }
            }
        }
    }

    // 后置操作（无论成功失败都会执行）
    post {
        always {
            // 清理：删除临时镜像
            script {
                bat 'docker rmi ${env.DOCKER_IMAGE}:${env.BUILD_ID} || true'
            }
            
            // 清理虚拟环境
            bat 'rmdir /s /q venv' 
        }
        success {
            // 成功时输出应用访问地址
            echo 'Deployment successful! Access the app at: http://localhost:5000'
        }
        failure {
            // 失败时通知
            echo 'Deployment failed! Check the logs for details.'
        }
    }
}