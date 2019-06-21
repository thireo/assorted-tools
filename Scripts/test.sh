#!/bin/bash +v

function installnow ()
{
	set +v
	pushd "//DCNAS/docs/Danish Care/Produktion/Programmerings filer/Epi-Care mobile/Android App/2.2.0/" > NUL 2>&1
	#cd \\DCNAS\docs\Danish Care\Produktion\Programmerings filer\Epi-Care mobile\Android App\2.2.0\ #> NUL 2>&1
	#@echo off
	#rem ECHO performing DK ECM 2.1.0 install
	#rem @echo off
	#rem echo %pwd%
	adb shell cmd package uninstall dk.danishcare.epicare.mobile2 > NUL 2>&1
	#@echo off
	#rem adb shell cmd package install -g -r "C:\svnrepos\ecm testarea\Epicare Mobile 2\DK\release\DKRelease-2.2.0.apk"
	adb install -r -g -d "apks/DKRelease-2.2.0.apk" > NUL 2>&1
	#if %ERRORLEVEL% NEQ 0 (
	if [ $? -gt 0 ]; then
		echo Kunne ikke installere appen.
		exit
	else
		echo Installation af app - faerdig.
	fi

	#@ECHO OFF
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

	#@echo off
	adb shell dumpsys deviceidle whitelist +dk.danishcare.epicare.mobile2 > NUL 
	#if %ERRORLEVEL% NEQ 0 (
	if [ $? -gt 0 ]; then
		echo Batteri optimering IKKE slået fra.
		exit 1
	else
		echo Batteri optimering slaaet fra.
	fi
	#@echo off
	adb shell settings put secure dialer_default_application dk.danishcare.epicare.mobile2
	adb shell am start -n dk.danishcare.epicare.mobile2/.EpiCareFreeActivity > NUL
	echo Startede Epi-Care mobile appen
	#pause
	read -p "Tryk på ENTER for at fortsaette..."
	adb shell am broadcast -a dk.danishcare.epicare.mobile2.tts --ei dk.danishcare.epicare.mobile2.tts.key 0x2a2a
	echo "Slukker telefon om 5 sekunder..."
	sleep 5
	adb shell reboot -p
	popd > NUL
}

while [ : ]
do

	#@ECHO OFF
	set +v
	#rem net use Z: \\DCNAS\docs
	clear
	# pushd \\DCNAS\docs\Danish Care\Produktion\Programmerings filer\Epi-Care mobile\Android App\2.2.0\ > NUL 2>&1
	echo Soeger efter tilsluttede mobiler...
	adb wait-for-device > NUL 2>&1
	#ERR=$(adb wait-for-device) #> NUL 2>&1
	#bbbb=$(git remote -v)
	#echo "$bbbb"
	#echo "tt $ERR tt"
	#if [[ "$ERR" == *"error"* ]]; then
	#	echo HUSK Kun en mobil tilsluttet ad gangen
	#	break 2
	if [ $? -gt 0 ]; then
		echo HUSK Kun en mobil tilsluttet ad gangen
		#break 1
		echo Genstarter script om fem sekunder...
		sleep 5
		continue
	fi

	output=$(adb devices -l | sed -n '2p')
	#echo "$output"
	#delim=' '
	#bob=$(echo $ID | cut -f1 --delimiter="$delim")
	ID=$(echo "$output" | cut -f1 --delimiter=' ')
	MODEL=$(echo "$output" | cut -f3 --delimiter=':')
	#echo "woaw t $MODEL t"

	if [[ "$ID" == *"ES2BA80621006079"* ||  "$ID" == *"LGH340ne8e09bfc"* || "$ID" == *"ZY323VFPCP"* || "$ID" == *"PL2GAR9880706416"* ]]; then
		echo "Fandt $ID - $MODEL"
		#echo "bob $ID"
		echo Installerer Epi-Care mobile
		installnow
		#exit  0
	else
		echo "Fandt ingen passende mobil - $MODEL"
		#pause
		#exit 0
	fi
	sleep 10
	clear
done
