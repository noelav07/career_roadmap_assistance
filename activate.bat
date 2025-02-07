@echo off
setlocal

:: Define variables
set ANACONDA_URL=https://repo.anaconda.com/archive/Anaconda3-2024.10-1-Windows-x86_64.exe
set INSTALLER=Anaconda3-2024.10-1-Windows-x86_64.exe
set INSTALL_PATH=C:\Anaconda3
set CONDA_ENV=career

echo Downloading Anaconda...
curl -o %INSTALLER% %ANACONDA_URL%

echo Installing Anaconda...
start /wait %INSTALLER% /InstallationType=JustMe /RegisterPython=1 /AddToPath=1 /S /D=%INSTALL_PATH%

echo Adding Conda to PATH...
setx PATH "%INSTALL_PATH%;%INSTALL_PATH%\Scripts;%INSTALL_PATH%\Library\bin;%PATH%" /M

echo Refreshing environment variables...
call %INSTALL_PATH%\Scripts\activate.bat

echo Creating Conda environment: %CONDA_ENV%...
call conda create -y -n %CONDA_ENV% python=3.12

echo Activating Conda environment...
call conda activate %CONDA_ENV%

echo Installing dependencies from requirements.txt...
call conda install -y --file requirements.txt

echo Installation complete! Environment '%CONDA_ENV%' is ready.

endlocal
