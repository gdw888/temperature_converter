// Pipeline example
pipeline {
  agent any
  triggers {
    githubPush() // This is the trigger for GitHub webhooks
  }
  stages {
    stage('Example') {
      steps {
        echo 'Build triggered from GitHub webhook'
      }
    }
  }
}

