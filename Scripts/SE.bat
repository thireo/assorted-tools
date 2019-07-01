@ECHO OFF
rem net use Z: \\DCNAS\docs
cls
rem pushd "\\DCNAS\docs\Danish Care\Produktion\Programmerings filer\Epi-Care mobile\Android App\2.2.0\" > NUL 2>&1
echo Soeger efter tilsluttede mobiler: 
adb wait-for-device > NUL 2>&1
if %ERRORLEVEL% NEQ 0 (
	echo HUSK: Kun en mobil tilsluttet ad gangen!
	EXIT /b 1
)


adb shell media volume --stream 4 --set 1 > NUL 2>&1
adb shell media volume --stream 2 --set 1 > NUL 2>&1



for /f "tokens=1-4" %%G in ('adb devices -l') DO (
	set ID=%%G
	set MODEL=%%J
)


if "%ID:~0,16%"=="ES2BA80621006079" OR "%ID:~0,16%"=="LGH340ne8e09bfc" OR "%ID:~0,16%"=="ZY323VFPCP" (
	echo Fandt: %ID% - %MODEL%
	rem echo Installerer Epi-Care mobile DK
	pushd "\\DCNAS\docs\Danish Care\Produktion\Programmerings filer\Epi-Care mobile\Android App\2.2.0\" > NUL 2>&1
	for /f "tokens=10 delims=,:" %%x in (apks\seoutput.json) do set Text=%%x
	echo Installerer ECM SE - (%Text%)
	call :install_dk
	popd
	adb shell reboot -p
	EXIT /B 0
) else (
	echo Fandt ingen mobil
	PAUSE
	EXIT /B 0
)

rem setlocal ENABLEDELAYEDEXPANSION
set /a count=1

:test
        adb shell ps | grep dk.danishcare.epicare.mobile2 > output
        if %ERRORLEVEL% NEQ 0 (
rem                echo bob
        rem      adb shell ps | grep dk.danishcare.epicare.mobile2
        rem     echo $1
		rem echo %ERRORLEVEL%
	rem     timeout 1s
		SLEEP 1
		set /a count+=1
		echo App ikke klar: %count%
		if "%count%" GEQ "3" (
			exit 1
		) else (
rem		endlocal
	        call :test
		)
) else (
rem        echo woaw
rem        echo %ERRORLEVEL%
	echo App startet.
	sleep 3
	exit /b 0
)


:install_dk
	setlocal
	@echo off
	rem ECHO performing DK ECM 2.1.0 install
	rem @echo off
	rem echo %pwd%
	adb shell cmd package uninstall dk.danishcare.epicare.mobile2 > NUL 2>&1
rem	if %ERRORLEVEL% NEQ 0 (
rem		echo Kunne ikke afinstallere appen.
rem		EXIT /b 1
rem	) else (
rem		echo Afinstallation af gammel app - Faerdig.
rem	)

	@echo off
	rem adb shell cmd package install -g -r "C:\svnrepos\ecm testarea\Epicare Mobile 2\DK\release\DKRelease-2.2.0.apk"
	adb install -r -g -d "apks/SERelease-2.2.0.apk" > NUL 2>&1
	if %ERRORLEVEL% NEQ 0 (
		echo Kunne ikke installere app'en.
		EXIT /b 1
	) else (
		echo Installation af app - faerdig.
	)

	@ECHO OFF
	adb shell pm grant dk.danishcare.epicare.mobile2 android.permission.WRITE_EXTERNAL_STORAGE > NUL 2>&1
	adb shell pm grant dk.danishcare.epicare.mobile2 android.permission.READ_CALL_LOG > NUL 2>&1
	adb shell pm grant dk.danishcare.epicare.mobile2 android.permission.BLUETOOTH > NUL 2>&1
	adb shell pm grant dk.danishcare.epicare.mobile2 android.permission.BLUETOOTH_ADMIN > NUL 2>&1
	adb shell pm grant dk.danishcare.epicare.mobile2 android.permission.WAKE_LOCK > NUL 2>&1
	adb shell pm grant dk.danishcare.epicare.mobile2 android.permission.RECEIVE_BOOT_COMPLETED > NUL 2>&1
	adb shell pm grant dk.danishcare.epicare.mobile2 android.permission.CALL_PHONE > NUL 2>&1
	adb shell pm grant dk.danishcare.epicare.mobile2 android.permission.READ_PHONE_STATE > NUL 2>&1
	adb shell pm grant dk.danishcare.epicare.mobile2 android.permission.MODIFY_AUDIO_SETTINGS2 > NUL 2>&1
	adb shell pm grant dk.danishcare.epicare.mobile2 android.permission.SEND_SMS > NUL 2>&1
	adb shell pm grant dk.danishcare.epicare.mobile2 android.permission.READ_CONTACTS > NUL 2>&1
	adb shell pm grant dk.danishcare.epicare.mobile2 android.permission.VIBRATE > NUL 2>&1
	adb shell pm grant dk.danishcare.epicare.mobile2 android.permission.ACCESS_COARSE_LOCATION > NUL 2>&1
	adb shell pm grant dk.danishcare.epicare.mobile2 android.permission.ACCESS_FINE_LOCATION > NUL 2>&1
	adb shell pm grant dk.danishcare.epicare.mobile2 android.permission.ACCESS_NETWORK_STATE > NUL 2>&1
	adb shell pm grant dk.danishcare.epicare.mobile2 android.permission.INTERNET > NUL 2>&1
	adb shell pm grant dk.danishcare.epicare.mobile2 android.permission.PROCESS_OUTGOING_CALLS > NUL 2>&1
	adb shell pm grant dk.danishcare.epicare.mobile2 android.permission.REQUEST_IGNORE_BATTERY_OPTIMIZATIONS > NUL 2>&1
	adb shell pm grant dk.danishcare.epicare.mobile2 android.permission.READ_EXTERNAL_STORAGE > NUL 2>&1
	ECHO Blev faerdig med at tillade ALT

	@echo off
	adb shell dumpsys deviceidle whitelist +dk.danishcare.epicare.mobile2 > NUL 
	adb shell dumpsys deviceidle whitelist +com.android.bluetooth > NUL
	if %ERRORLEVEL% NEQ 0 (
		echo Batteri optimering IKKE slået fra.
		EXIT /b 1
	) else (
		echo Batteri optimering slaaet fra.
	)
	@echo off
        adb shell settings put secure dialer_default_application dk.danishcare.epicare.mobile2
	adb shell am start -n dk.danishcare.epicare.mobile2/.EpiCareFreeActivity > NUL
	ECHO Startede Epi-Care mobile app'en
	rem PAUSE
	call :test
	adb shell am broadcast -a "dk.danishcare.epicare.mobile2.tts" --ei "dk.danishcare.epicare.mobile2.tts.key" 0x2a2a
	adb shell media volume --stream 4 --set 3 > NUL 2>&1
	adb shell media volume --stream 2 --set 3 > NUL 2>&1
	rem popd
	echo FAERDIG
	endlocal
	exit /b 0
	

rem Ideas for ECM testing.
rem adb shell am broadcast -a "dk.danishcare.opkald.tæller" --el tæller 101010
