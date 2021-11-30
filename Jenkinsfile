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
        stage('Parallel jobs') {
            parallel {
                stage('Build') {
                    steps {
                        echo "Hello ${params.all_choices}"
                        sh '/usr/bin/python3 --version'
                    }
                }
                stage('Installation Preparation') {
                    steps {
                        sleep 1
                        sh '/usr/bin/python3 testP.py'
                    }
                }
            }
        }
        stage('Unit Test') {
            steps {
                echo "Deliver ${params.branch}"
            }
        }
        stage('Full regression') {
            parallel {
                stage('Suite 1') {
                    steps {
                        echo "Hello ${params.all_choices}"
                        sh '/usr/bin/python3 --version'
                    }
                }
                stage('Suite 2') {
                    steps {
                        sleep 1
                        sh '/usr/bin/python3 testP.py'
                    }
                }
                stage('Suite 3') {
                    steps {
                        sleep 1
                        sh '/usr/bin/python3 testP.py'
                    }
                }
            }
        }
        stage('Final QA Test') {
            steps {
                echo "QA Test ${params.branch}"
            }
        }
        stage('Install Test') {
            steps {
                echo "Installation test ${params.branch}"
            }
        }
        stage('Public report') {
            steps {
                echo "Public report ${params.branch}"
            }
        }
    }
post {
    success {
        echo "The Pipeline success :)"
    }
  }
}