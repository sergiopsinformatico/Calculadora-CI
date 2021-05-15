pipeline {
    agent none 
    stages {
        stage('Build') { 
            agent {
                docker {
                    image 'python:2-alpine' 
                }
            }
            steps {
                sh 'python -m py_compile sources/calculadora.py' 
                stash(name: 'compiled-results', includes: 'sources/*.py*') 
            }
        }
		stage('Test') { 
            agent {
                docker {
                    image 'python:2-alpine' 
                }
            }
            steps {
                sh 'python -m unittest -v sources/test_calculadora.py' 
            }
        }
    }
}