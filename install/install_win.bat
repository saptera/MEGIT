@ECHO OFF
TITLE iSCANoPy Installer
ECHO  __^| ^|_____________________________^| ^|__
ECHO (__   _____________________________   __)
ECHO    ^| ^|                             ^| ^|
ECHO    ^| ^|  MEGIT Installation Script  ^| ^|
ECHO  __^| ^|_____________________________^| ^|__
ECHO (__   _____________________________   __)
ECHO    ^| ^|                             ^| ^|
ECHO.

:: Set valid Python version range [incusive, exclusive)
SET minVersion=3.9.0
SET maxVersion=5.0.0

:: Check Python installation
python -V 2>NUL
IF errorLevel 1 GOTO errorNoPython
:: Check Python version
CALL :parsePythonVersion %minVersion%, parMinVer
CALL :parsePythonVersion %maxVersion%, parMaxVer
FOR /F "tokens=2 USEBACKQ DELIMS= " %%F IN (`python -V`) DO (SET version=%%F)
CALL :parsePythonVersion %version%, parVer
IF %parVer% LSS %parMinVer% (
    ECHO Version too low, Python ^>^=%minVersion% required.
    PAUSE >NUL
    EXIT
) ELSE IF %parVer% GEQ %parMaxVer% (
    ECHO Version too high, Python ^<%maxVersion% required.
    PAUSE >NUL
    EXIT
)

ECHO Press any key to start...
ECHO.
PAUSE >NUL
ECHO ----------------------------------------

:: Update PIP
python -m pip install --upgrade pip

:: Install required packages
python -m pip install numpy
python -m pip install scipy
python -m pip install opencv-python
python -m pip install shapely
python -m pip install matplotlib
python -m pip install h5py
python -m pip install PySide6

ECHO ----------------------------------------
ECHO.
ECHO DONE
ECHO Press any key to exit...
PAUSE >NUL
EXIT


:errorNoPython
ECHO Error^: Python not installed or not in PATH
PAUSE >NUL
EXIT


:parsePythonVersion
FOR /F "tokens=1,2,3 DELIMS=." %%a IN ("%~1") DO (
    SET components[1]=%%a
    IF %%b LSS 10 (SET components[2]=0%%b) ELSE (SET components[2]=%%b)
    IF %%c LSS 10 (SET components[3]=0%%c) ELSE (SET components[3]=%%c)
)
SET %~2=%components[1]%%components[2]%%components[3]%
EXIT /B
