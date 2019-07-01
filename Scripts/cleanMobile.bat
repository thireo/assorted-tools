@echo off
adb wait-for-device
if %ERRORLEVEL% NEQ 0 (
        echo HUSK: Kun en mobil tilsluttet ad gangen!
        EXIT /b 1
) else (
	echo Klargoerer mobil telefon
	adb shell am broadcast -a "dk.danishcare.epicare.mobile2.tts" --ei "dk.danishcare.epicare.mobile2.tts.key" 0x4242
	adb shell pm clear --user 0 com.google.android.apps.messaging
	adb shell pm clear --user 0 com.google.android.dialer
	
	
	adb shell am start com.google.android.apps.messaging
	SLEEP 5
	adb shell input draganddrop 250 250 250 250 500
	adb shell input tap 430 150
	adb shell input draganddrop 250 250 250 250 500
	adb shell input tap 430 150
	adb shell input draganddrop 250 250 250 250 500
	adb shell input tap 430 150
	
	#adb shell settings put global adb_enabled 0

	if %ERRORLEVEL% NEQ 0 (
		echo Klargoering fejlede...
		EXIT /b 1
	) else (
		echo Det lykkedes...
		EXIT /b 0
	)
)
