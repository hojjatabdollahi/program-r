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



## Introduction

Program Y is an AIML interpreter written in Python. It includes an entire Python 3 framework for building you own chat bots using
Artificial Intelligence Markup Language, or AIML for short.

Program Y is fully cross platform, running on

- Mac OSX
- Linux
- Windows

100% Support for all AIML 2.0 Tags plus all Pandora bot ones they never documented

- Full support for al AIML 2.0 Tags
- RDF Support through addtriple, deletetriple, select, uniq and uniq
- List processing with First and Rest
- Advanced learn support including resetlearn and resetlearnf
- Full Out Of Band Support
- Full embedded XML/HTML Support
- Dynamic Sets, Maps and Variables

Program Y is extremely extensible, you can

- Add you own AIML tags
- Add you own Spelling Checker
- Support User Authorisation
- Support User Authentication
- Add your own Out Out Band (OOB) tags
- Add Dynamic Sets in Python
- Add Dynamic Maps in Python
- Add Dynamic Variables in Python
- Run a variety of clients

Program-Y comes with a base set of grammars for various industry sectors, including

- Energy Industry
- Banking
- Telecoms
- Weather
- Surveys
- News Feeds
- Maps

Using Program-Y
----------------
Full documentation is available on `Program Y Wiki <https://github.com/keiffster/program-y/wiki>`_

Program-Y ships with a very basic bot that has a single answer, after installation you can chat with your Program Y by running one of the many bots found in GitHub repo

- `Y-Bot <https://github.com/keiffster/y-bot>`_
- `Alice2 <https://github.com/keiffster/alice2-y>`_
- `Rosie <https://github.com/keiffster/rosie-y>`_
- `Professor <https://github.com/keiffster/professor-y>`_

See the individual folders for unix and windows scripts required to run a bot.

Getting Started
---------------
Once you have got the system installed and have run one or more of the bots, head over to the
`Tutorial <https://github.com/keiffster/program-y/wiki/AIML-Tutorial>`_ on the Wiki for a full
run down of everything possible in AIML
