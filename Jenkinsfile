pipeline {
    agent any
    parameters {
        choice(name: 'all_choices',
        choices:'a\nb\n')
        text(name: 'enter path',
        defaultValue: 'somedefault path')
        string(name: 'branch',
        defaultValue: 'main')
    }
    stages {
        stage('build') {
            steps {
                sleep 1
                sh '/usr/local/bin/python3 --version'
            }
        }
        stage('test') {
            steps {
                sleep 1
            }
        }
    }
}