@echo off
cls
echo "**************************************************"
echo  This batch file will create a project directory.
echo  It is the initiating part for Assignment 1 from IaC.
echo "**************************************************"
echo  By Konrad Jeziorski, student ATU
echo "**************************************************"
echo *** Press [ctrl][c] to exit or any key to continue ***
pause 
set /p NAME=Enter the name of the project, then press [return] 
echo Creating %NAME%
mkdir %NAME%
cd %NAME%
mkdir Documentation
mkdir Examples
mkdir Results
mkdir Sources
mkdir Tests
cls
dir
echo " Detected OS is %OS%"
echo "**************************************************"
echo *** Finished creating project structure for %NAME% ***
echo "**************************************************"
:get Date
:getTime
echo  Created on %Date% at %time%
echo "**************************************************"
echo *** Press [ctrl][c] to exit or any key to continue ***
@pause
cd ..
cmd /K
