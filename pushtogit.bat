@echo off
git init
git add .
git status
set /p NameOfCommit=What what you like to name your commit?
git commit -m "%NameOfCommit%"
git push -u origin master
echo "Press ENTER to close this window!"
set /p EnterToClose=
