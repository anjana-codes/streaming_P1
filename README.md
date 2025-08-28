# Project Title: streaming_P1
Initial Streaming Project using the provided producer and consumer scripts.

### Name: Anjana Dhakal, 08/28/2025

## Objectives :

The goal is to:
Understand Python generators. 
Modify producers and consumers for real-time data streaming.
Perform basic real-time analytics.

![Python 3.11](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white)

This project introduces streaming data. 
The Python language includes generators - we'll use this feature to generate some streaming buzzline messages. 
As the code runs, it will continuously update the log file. 
We'll use a consumer to monitor the log file and alert us when a special message is detected. 

## Steps for Project Initialization

1. Create-repo-in-github.
2. Use git to clone the new repository to your local machine.
3. Clone-repo-to-local machine.
4. Add key files such as .gitignore and requirements.txt.
5. Use Git to add, commit, and push your new files to GitHub.
 ```
    git add .
    git commit -m " update readme.md"
    git push origin main

```
6. ALWAYS Create a Python Virtual Environment for your project.

 ```
    python -m venv .env
    source .env/bin/activate
```
7. Install dependencies.
```
    pip install -U pip setuptools wheel
    py -m pip install --upgrade -r requirements.txt
```

### Task 1: Create a Unique Producer
1. Add a new Python script in the producers folder.
2. Name your script using your unique identifier (basic_producer_anjana.py).
3. Copy and paste the content from the example file into yours. 
4. Git add, commit, and push your changes to your GitHub repo before making any other changes. 
     See instructions at https://github.com/denisecase/buzzline-01-case/blob/main/docs/GIT-ADD-COMMIT-PUSH.mdLinks to an external site.
5. Modify your Python generator to produce custom messages.
6. Log these messages using the provided logger.
7. As you work, git add, commit, and push your changes to your GitHub repo. (Frequent small, commits are helpful.)

## Task 2: Create a Unique Consumer
1. Add a new Python script in the consumers folder.
2. Name your script uniquely (basic_consumer_anjana.py).
3. Copy and paste the content from the example file into  yours. 
4. Git add, commit, and push your changes to your GitHub repo before making any other changes. 
5. Continue to read the log file in real time as we did in the example. 
6. Implement real-time analytics (e.g., alerting on a specific pattern that matches your new messages).
7. As you work, git add, commit, and push your changes to your GitHub repo. 

## Task 3. Generate Streaming Data (Terminal 1)

Now we'll generate some streaming data. By the way - you've done 90% of the hard work before we even look at code. Congratulations!

In VS Code, open a terminal. Use the commands below to activate .venv, and run the generator as a module. To learn more about why we run our Python file as a module, see PYTHON-PKG-IMPORTS

Windows:
 ```
.venv\Scripts\activate
py -m producer.basic_producer_anjana

```

## Task 4. Monitor an Active Log File (Terminal 2)
A common streaming task is monitoring a log file as it is being written. This project has a consumer that reads and processes our own log file as log messages arrive.

In VS Code, open a NEW terminal in your root project folder. Use the commands below to activate .venv, and run the file as a module.

Windows:
 ```
.venv\Scripts\activate
py -m consumer.basic_consumer_anjana

```

## Save Space
To save disk space, you can delete the .venv folder when not actively working on this project. We can always recreate it, activate it, and reinstall the necessary packages later. Managing Python virtual environments is a necessary and valuable skill. We will get a good amount of practice.

## License
This project is licensed under the MIT License as an example project. You are encouraged to fork, copy, explore, and modify the code as you like. See the LICENSE file for more.
