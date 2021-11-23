pipeline {
    agent any
    parameters {
        choice(name: 'all_choices',
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