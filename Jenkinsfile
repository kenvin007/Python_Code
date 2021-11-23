pipeline {
    agent any
    parameters {
        choic(name: 'choices',
        choices:'a\nb\n')
    }
    stages {
        stage('build') {
            steps {
                sh '/usr/local/bin/python3 --version'
            }
        }
    }
}