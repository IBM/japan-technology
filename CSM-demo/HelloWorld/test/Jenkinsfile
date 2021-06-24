pipeline {
  agent {
    label "maven"
  }
  options {
    buildDiscarder(logRotator(numToKeepStr: '50')) 
  }
  parameters {
      string(name: 'stage', defaultValue: '')
  }
  environment {
    DATE_TAG=sh (script: 'date --utc +v%Y%m%d%H%M', returnStdout: true).trim()
    BRANCH_NAME="${GIT_BRANCH}"
  }
  
  stages {
    stage('Initialize') {
       steps {
        sh "echo Initializing.."
        println("Date: ${env.DATE_TAG}\nBranch: ${env.BRANCH_NAME}")
      }
    }
    stage('App: Build') {
      steps {
        sh "echo Building App.."
      }
    }
    stage('App: Test') {
      steps {
        sh "echo Testing App.."
      }
    }
    stage('App: Container Image') {
      steps {
        sh "echo Testing App.."
      }
    }
  }
}
