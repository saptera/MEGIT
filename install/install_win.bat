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

:: Set Python interpreter path
SET pyBin=python
:: Set valid Python version range [incusive, exclusive)
SET minVersion=3.9.0
SET maxVersion=9.9.9

:: Check Python installation
%pyBin% -V 2>NUL
IF errorLevel 1 GOTO errorNoPython
:: Check Python version
CALL :parsePythonVersion %minVersion%, parMinVer
CALL :parsePythonVersion %maxVersion%, parMaxVer
FOR /F "tokens=2 USEBACKQ DELIMS= " %%F IN (`%pyBin% -V`) DO (SET version=%%F)
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
%pyBin% -m pip install --upgrade pip

:: Install required packages
%pyBin% -m pip install numpy
%pyBin% -m pip install scipy
%pyBin% -m pip install opencv-python
%pyBin% -m pip install shapely
%pyBin% -m pip install matplotlib
%pyBin% -m pip install h5py
%pyBin% -m pip install PySide6

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
