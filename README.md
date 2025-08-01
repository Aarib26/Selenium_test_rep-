# 🧪 Selenium + Jenkins + Git Integration Project

This is a beginner-friendly automation project using **Selenium**, **Pytest**, **Git**, and **Jenkins**. It's designed for learning **CI/CD with automation testing** using Python.

---

## 📂 Project Structure

```
selenium-jenkins/
├── test_pytest_jenkins.py      # Main Selenium test script
├── requirements.txt            # Python dependencies
├── pytest.ini                  # Pytest configuration (optional)
├── Jenkinsfile                 # Jenkins Pipeline definition (optional)
├── .gitignore                  # Ignore unnecessary folders
└── README.md                   # You're reading this!
```

---

## 🚀 What It Does

- Automates browser tasks using Selenium WebDriver.
- Uses `pytest` to run the test(s).
- Can be integrated and executed with Jenkins in CI/CD pipelines.
- Demonstrates Git-based version control with Jenkins pipelines.

---

## ⚙️ Prerequisites

### For Local Use
- ✅ Python 3.8 or higher
- ✅ Google Chrome installed
- ✅ Matching ChromeDriver (download from https://chromedriver.chromium.org/downloads)
- ✅ Git (for cloning the repo)
- ✅ pip (`python -m ensurepip --upgrade` if needed)

### For Jenkins Integration
- ✅ Java installed
- ✅ Jenkins installed (https://www.jenkins.io/download/)
- ✅ Jenkins user set up and running at `http://localhost:8080`

---

## 🔧 Setup and Run Locally

### 1. Clone this Repository

```bash
git clone https://github.com/Aarib26/Selenium_test_rep-.git
cd Selenium_test_rep-
```

### 2. (Optional but Recommended) Create a Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate    # Windows
```

### 3. Install Required Packages

```bash
pip install -r requirements.txt
```

### 4. Run the Test

```bash
pytest
```

---

## 🤖 Jenkins Integration Steps

### Option A: Freestyle Project

1. Open Jenkins: `http://localhost:8080`
2. Click `New Item` → choose **Freestyle Project**
3. In **Build Steps**, use:

```bash
cd C:\path\to\Selenium_test_rep-
venv\Scripts\activate
pip install -r requirements.txt
pytest
```

---

### Option B: Using `Jenkinsfile` (Declarative Pipeline)

1. In Jenkins, create a new item → select **Pipeline**
2. Choose **Pipeline script from SCM**
   - SCM: Git
   - Repo URL: `https://github.com/Aarib26/Selenium_test_rep-.git`
3. Jenkins will detect the `Jenkinsfile` and run the pipeline.

#### Jenkinsfile Sample:

```groovy
pipeline {
    agent any

    stages {
        stage('Install Requirements') {
            steps {
                bat 'python -m venv venv'
                bat '''
                call venv\\Scripts\\activate
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                bat '''
                call venv\\Scripts\\activate
                pytest
                '''
            }
        }
    }
}
```

---

## 📦 Example `requirements.txt`

```
selenium
pytest
```

---

## 🙋‍♂️ Who Is This For?

- DevOps and QA students
- Automation engineers
- Anyone learning Jenkins pipelines and Selenium

---

## 📌 Notes

- Don’t push `.venv/`, `.idea/`, or `__pycache__/` folders — they are ignored via `.gitignore`
- Always run `pip freeze > requirements.txt` after installing new packages

---

## 🤝 Contributions

This is a learning-focused repository. Feel free to fork, clone, and extend.

---

## 🧠 Author

**Aarib A.K.**  
Repo: [Selenium_test_rep-]((https://github.com/Aarib26/Selenium_test_rep-.git))
