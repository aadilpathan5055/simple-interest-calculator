# Simple Interest Calculator

A small Python Tkinter desktop application that calculates simple interest from principal, rate, and time.

## Project structure

- `app.py` - the Tkinter GUI application
- `README.md` - project documentation and instructions
- `requirements.txt` - dependency notes

## Setup

1. Install Python 3.
2. Install the Tkinter system package if needed:
   - On Ubuntu/Debian:
     ```bash
     sudo apt update
     sudo apt install python3 python3-tk
     ```
   - On Windows, install Python from python.org and include Tcl/Tk support.
3. (Optional) Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
4. Install dependencies:
   ```bash
   python3 -m pip install --upgrade pip
   # No external pip packages are required for this app.
   ```

## Run

```bash
python3 app.py
```

## GitHub repository

Initial project implementation and later improvement commits are tracked in this repo.

## Jenkins with Docker

### Install Docker

1. Install Docker Engine:
   - On Ubuntu:
     ```bash
     sudo apt update
     sudo apt install docker.io
     sudo systemctl enable --now docker
     ```
2. Verify Docker is available:
   ```bash
   docker --version
   ```

### Run Jenkins in Docker

```bash
docker pull jenkins/jenkins:lts

docker volume create jenkins_home

docker run -d --name jenkins \
  -p 8080:8080 -p 50000:50000 \
  -v jenkins_home:/var/jenkins_home \
  jenkins/jenkins:lts
```

Open Jenkins at `http://localhost:8080`.

### Retrieve initial admin password

```bash
docker exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword
```

### Complete setup

1. Open Jenkins in your browser.
2. Enter the initial admin password.
3. Install suggested plugins.
4. Create the first admin user.

## Jenkins CI/CD pipeline guide

### Pipeline overview

A simple Jenkins pipeline for this repository can:
- checkout the repository
- install Python dependencies
- validate the Python code
- report build status

### Example Jenkinsfile

```groovy
pipeline {
  agent any
  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }
    stage('Install Dependencies') {
      steps {
        sh 'python3 -m pip install --upgrade pip'
        sh 'python3 -m pip install --upgrade setuptools'
      }
    }
    stage('Validate') {
      steps {
        sh 'python3 -m py_compile app.py'
      }
    }
    stage('Publish') {
      steps {
        echo 'Simple Interest Calculator is ready for use.'
      }
    }
  }
}
```

### Connect GitHub to Jenkins

1. Install the `GitHub` and `Git` plugins in Jenkins.
2. Create credentials for GitHub in Jenkins.
3. Create a new pipeline job and set the `Pipeline script from SCM` option.
4. Point Jenkins to this GitHub repository and choose the branch to build.
5. Optionally, configure a GitHub webhook to trigger builds on push.

### Simple CI/CD workflow

- Developer pushes code to GitHub.
- Jenkins detects the push and checks out the latest code.
- Jenkins runs validation and dependency steps.
- If the pipeline succeeds, the application is marked ready.

## Notes

- This app uses built-in Tkinter and does not require external pip libraries.
- For Linux, `python3-tk` is the package needed to run the GUI.
