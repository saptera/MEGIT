@ECHO OFF
TITLE MEGIT System
ECHO  __^| ^|_______________________^| ^|__
ECHO (__   _______________________   __)
ECHO    ^| ^|                       ^| ^|
ECHO    ^| ^|  MEGIT Data Pipeline  ^| ^|
ECHO  __^| ^|_______________________^| ^|__
ECHO (__   _______________________   __)
ECHO    ^| ^|                       ^| ^|
ECHO.

:: Set valid Python version range [incusive, exclusive)
SET minVersion=3.9.0
SET maxVersion=9.9.9

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

:: Set pipeline path
SET zoomGUI=%cd%%\megit\script\preproc_zoom.py
SET overGUI=%cd%%\megit\script\preproc_over.py
SET predMOD=%cd%%\megit\script\model_pred.py
SET crsDET=%cd%%\megit\script\crs_det.py
SET crsVLD=%cd%%\megit\script\crs_vld.py

:: Launch MEGIT system
ECHO.
ECHO Please select from the following steps:
ECHO     1 - MEGIT zoom video preprocessing GUI
ECHO     2 - MEGIT overview video preprocessing GUI
ECHO     3 - MEGIT animal pose estimation SCRIPT
ECHO     4 - MEGIT region cross detection SCRIPT
ECHO     5 - MEGIT manual cross validation GUI
ECHO     q - Exit system
ECHO.

:getStep
SET step=0
SET /P step=Choose the step in the pipeline: 

:: Launch pipeline subsystem
IF "%step%"=="1" (
    ECHO MEGIT zoom video preprocessing
    ECHO ----------------------------------------
    python %zoomGUI%
) ELSE IF "%step%"=="2" (
    ECHO MEGIT overview video preprocessing
    ECHO ----------------------------------------
    python %overGUI%
) ELSE IF "%step%"=="3" (
    ECHO MEGIT animal pose estimation
    GOTO launchPred
) ELSE IF "%step%"=="4" (
    ECHO MEGIT region cross detection
    ECHO ----------------------------------------
    GOTO launchCrsDet
) ELSE IF "%step%"=="5" (
    ECHO MEGIT manual cross validation
    ECHO ----------------------------------------
    python %crsVLD%
) ELSE IF "%step%"=="q" (
    ECHO Exiting system
    ECHO Press any key to exit...
    PAUSE >NUL
    EXIT
)
:scriptFin
ECHO ----------------------------------------
ECHO.
GOTO getStep


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


:launchPred
SET procDIR=""
SET /P procDIR=Please define the preprocessed data directory: 
IF %procDIR%=="" (
    ECHO The process directory MUST be defined!
    GOTO launchPred
)
SET selcMOD=""
SET /P selcMOD=Please define the customized model, use default if not defined: 
SET infrSTP=0
SET /P infrSTP=Please define the processing batch size, use 300 if undefined: 
:: Run inference
ECHO ----------------------------------------
IF %selcMOD%=="" (
    IF "%infrSTP%"=="0" (
        python %predMOD% %procDIR%
    ) ELSE (
        python %predMOD% %procDIR% -s %infrSTP%
    )
) ELSE (
    IF "%infrSTP%"=="0" (
        python %predMOD% %procDIR% -m %selcMOD%
    ) ELSE (
        python %predMOD% %procDIR% -m %selcMOD% -s %infrSTP%
    )
)
GOTO scriptFin


:launchCrsDet
SET procDIR=""
SET /P procDIR=Please define the pose estimation results data directory: 
IF %procDIR%=="" (
    ECHO The process directory MUST be defined!
    GOTO launchCrsDet
)
SET detTh=""
SET /P detTh=Please define the detection threshold, 3.0 if undefined: 
:: Run cross detection
ECHO ----------------------------------------
IF %detTh%=="" (
    python %crsDET% %procDIR%
) ELSE (
    python %crsDET% %procDIR% -t %detTh%
)
GOTO scriptFin

