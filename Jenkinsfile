stage('Run Tests') {
    steps {
        script {
            // 创建测试数据库
            bat 'python init_db.py'
            
            // 设置环境变量
            bat 'set FLASK_APP=wsgi.py'
            
            // 运行测试
            bat 'pytest --junitxml=test-results.xml'
            junit 'test-results.xml'
        }
    }
}