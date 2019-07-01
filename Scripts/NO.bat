@ECHO OFF
cls

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
	pushd "\\DCNAS\docs\Danish Care\Produktion\Programmerings filer\Epi-Care mobile\Android App\2.2.0\" > NUL 2>&1
	for /f "tokens=10 delims=,:" %%x in (apks\nooutput.json) do set Text=%%x
	rem popd
	echo Installerer ECM NO - (%Text%)
	rem pushd "\\DCNAS\docs\Danish Care\Produktion\Programmerings filer\Epi-Care mobile\Android App\2.2.0\" > NUL 2>&1
	call :install_dk
	popd
	adb shell reboot -p 
	EXIT /B 0
) else (
	echo Fandt ingen mobil
	PAUSE
	EXIT /B 0
)

set /a count=1

:test
        adb shell ps | grep dk.danishcare.epicare.mobile2 > output
        if %ERRORLEVEL% NEQ 0 (
		SLEEP 1
		set /a count+=1
		echo App ikke klar: %count%
		if "%count%" GEQ "3" (
			exit 1
		) else (
	        call :test
		)
) else (
	echo App startet.
	sleep 3
	exit /b 0
)

:install_dk
	setlocal
	@echo off
	adb shell cmd package uninstall dk.danishcare.epicare.mobile2 > NUL 2>&1
	adb install -r -g -d "apks/NORelease-2.2.0.apk" > NUL 2>&1
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
	call :test
	adb shell am broadcast -a "dk.danishcare.epicare.mobile2.tts" --ei "dk.danishcare.epicare.mobile2.tts.key" 0x2a2a
	adb shell media volume --stream 4 --set 3 > NUL 2>&1
	adb shell media volume --stream 2 --set 3 > NUL 2>&1
	
	echo FAERDIG
	endlocal
	exit /b 0
	rem endlocal

