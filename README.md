# Coding Test Practice & Dev Workflow Setup

이 저장소는 **코딩 테스트 연습**과 **개발 업무 프로세스 구축**을 동시에 다루기 위한 프로젝트입니다. 

초기에는 하나의 프로젝트로 관리하며, 향후 필요 시 코딩 테스트용 프로젝트와 업무 프로세스용 프로젝트로 분리할 수 있습니다.

---

## 1. Environment

| 항목                 | 설정                                         |
| ------------------ | ------------------------------------------ |
| **OS**             | Windows 10/11                              |
| **Editor**         | PyCharm                                    |
| **Language**       | Python 3.x                                 |
| **VCS**            | Git + GitHub                               |

---

## 2. Project Structure

```
coding_test/
├─ main.py
├─ venv/
└─ .idea/ (PyCharm settings)
```

필요에 따라 알고리즘별 또는 주제별 디렉토리를 추가하여 관리할 수 있습니다.

---

## 3. Git Usage Guide (업무 프로세스용)

아래는 **GitHub 원격 저장소와 연동하는 다양한 케이스**를 정리한 가이드입니다. 

상황에 따라 복사/붙여넣기 하여 빠르게 프로젝트를 세팅할 수 있습니다.

우선은, 확인한 Case는 별도로 Check 합니다. (모두 Check 되었을 때, 이 문장은 제거합니다.)

---

### **Case A. 기존 프로젝트를 GitHub 빈 레포와 연동할 때** (Check)

```
git init
git add .
git commit -m "initial commit"

git remote add origin git@github.com:사용자명/레포명.git
git branch -M main
git push -u origin main
```

---

### **Case B. GitHub에서 클론한 뒤 작업하는 경우**

```
git clone git@github.com:사용자명/레포명.git
cd 레포명
```

작업 후 커밋:

```
git add .
git commit -m "message"
git push
```

---

### **Case C. 기존 remote 변경해야 할 때**

```
git remote remove origin
git remote add origin git@github.com:사용자명/레포명.git
git push -u origin main
```

---

### **Case D. .git을 잘못 만들었을 때 초기화** (CMD, Check)

PowerShell:

```
Remove-Item -Recurse -Force .git
git init
```

CMD:

```
rmdir /s /q .git
git init
```

---

## 4. How to Run (코딩 테스트 코드 실행)

### **1) 가상환경 활성화**

PowerShell:

```
.\venv\Scripts\Activate
```

CMD:

```
venv\Scripts\activate.bat
```

---

### **2) 실행**

```
python main.py
```

추가 알고리즘 파일을 작성할 경우:

```
python algorithms/xxx.py
```

---