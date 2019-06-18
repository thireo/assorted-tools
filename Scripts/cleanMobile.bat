@echo off
adb wait-for-device
if %ERRORLEVEL% NEQ 0 (
        echo HUSK: Kun en mobil tilsluttet ad gangen!
        EXIT /b 1
) else (
	echo Klargoerer mobil telefon
	adb shell am broadcast -a "dk.danishcare.epicare.mobile2.tts" --ei "dk.danishcare.epicare.mobile2.tts.key" 0x4242
	adb shell pm clear com.google.android.apps.messaging
	adb shell pm clear com.google.android.dialer
	adb shell settings put global adb_enabled 0
	if %ERRORLEVEL% NEQ 0 (
		echo Klargoering fejlede...
		EXIT /b 1
	) else (
		echo Det lykkedes...
		EXIT /b 0
	)
)
