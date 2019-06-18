@echo off
echo Current directory:
set olddir=%cd%
echo %olddir%
pushd "\\DCNAS\docs\Danish Care\Produktion\Programmerings filer\Epi-Care mobile\Android App\2.2.0\"
echo Starts copying...
cp "%olddir%/DK/release/DKRelease-2.2.0.apk" "apks\DKRelease-2.2.0.apk"
echo DK
cp "%olddir%/UK/release/UKRelease-2.2.0.apk" "apks\UKRelease-2.2.0.apk"
echo UK
cp "%olddir%/DE/release/DERelease-2.2.0.apk" "apks\DERelease-2.2.0.apk"
echo DE
cp "%olddir%/SE/release/SERelease-2.2.0.apk" "apks\SERelease-2.2.0.apk"
echo SE
cp "%olddir%/NO/release/NORelease-2.2.0.apk" "apks\NORelease-2.2.0.apk"
echo NO
cp "%olddir%/NL/release/NLRelease-2.2.0.apk" "apks\NLRelease-2.2.0.apk"
echo NL
popd
