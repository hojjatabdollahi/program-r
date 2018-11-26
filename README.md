## Introduction

Program R is an AIML interpreter written in Python. It includes an entire Python 3 framework for building you own chat bots using
Artificial Intelligence Markup Language, or AIML for short.

Program R is fully cross platform, running on

- Mac OSX
- Linux
- Windows


## Installation
### Windows
To install program-r in windows you should do the following:

1- Clone the repository
```
git clone https://github.com/roholazandie/program-r.git
```

2- Install virtualenv for windows

3- after creating and activating virtualenv:
```
pip install -r requirements.txt
```

4- Open powershell or cmd and run:
```
set-executionpolicy RemoteSigned
```
Now you can run /env/Scripts/activate

5- Install spacy:

-  Run powershell as admin in project directory

- Activate the environment:
```
python -m venv env
```
- Run:
```
./env/Scripts/activate
```
- Run:
```
pip install -U spacy
```
- Run:
```
/env/Scripts/python -m spacy download en
```
You should see the "linking successful" message.

4 - Set src:
- In pycharm:
    Right click on src then Mark as directory and then sources root

- In command line:
        Add src path to PYTHONPATH


## Points on using
1 - the rephrase file should contain only one sentence phrases.


## Running

Before running in windows you need to make sure that you have a tmp folder in the root of dive C:. This will keep track of
log files. In linux the folder is /tmp and is already created so you don't need any configuration.



## Docker
With this, container can use the host network, so mongodb can run on host system.
```
docker run -i -t --net=host programr_programr
```
