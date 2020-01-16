@echo off
set PATH=%PATH%;C:\Users\bartl\Anaconda3\envs\embedded\Scripts;C:\Program Files (x86)\Google\Chrome\Application\;
set FLASK_APP=serwer.py
set FLASK_ENV=development

rem start cmd /k "C:\Users\bartl\Anaconda3\Scripts\activate.bat embedded"


call C:\Users\bartl\Anaconda3\Scripts\activate.bat embedded


@echo on

start cmd /C chrome.exe 127.0.0.1:5000
rem start flask run

call python -m serwer
rem start flask run

rem cmd /k