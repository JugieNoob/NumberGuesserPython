@echo off
git init
git add .
git status
set /p NameOfCommit=What what you like to name your commit?
git commit -m "%NameOfCommit%"
git remote add origin https://github.com/JugieNoob/NumberGuesserPython.git
git push --force -u origin main
echo "Press ENTER to close this window!"
set /p EnterToClose=