pipeline {
    agent any
    parameters {
        choice(name: 'all_choices',
        choices:'a\nb\n')
        string(name: 'enter path',
        defaultValue: 'somedefault path')
    }
    stages {
        stage('build') {
            steps {
                sleep 10
                sh '/usr/local/bin/python3 --version'
            }
        }
        stage('test') {
            steps {
                sleep 10
            }
        }
    }
}