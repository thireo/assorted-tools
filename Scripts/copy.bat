@echo off
echo Current directory:
set olddir=%cd%
echo %olddir%
pushd "\\DCNAS\docs\Danish Care\Produktion\Programmerings filer\Epi-Care mobile\Android App\2.2.0\"
echo Starts copying...
cp "%olddir%/DK/release/DKRelease-2.2.0.apk" "apks\DKRelease-2.2.0.apk"
cp "%olddir%/DK/release/output.json" "apks\dkoutput.json"
echo DK
cp "%olddir%/UK/release/UKRelease-2.2.0.apk" "apks\UKRelease-2.2.0.apk"
cp "%olddir%/UK/release/output.json" "apks\ukoutput.json"
echo UK
cp "%olddir%/DE/release/DERelease-2.2.0.apk" "apks\DERelease-2.2.0.apk"
cp "%olddir%/DE/release/output.json" "apks\deoutput.json"
echo DE
cp "%olddir%/SE/release/SERelease-2.2.0.apk" "apks\SERelease-2.2.0.apk"
cp "%olddir%/SE/release/output.json" "apks\seoutput.json"
echo SE
cp "%olddir%/NO/release/NORelease-2.2.0.apk" "apks\NORelease-2.2.0.apk"
cp "%olddir%/NO/release/output.json" "apks\nooutput.json"
echo NO
cp "%olddir%/NL/release/NLRelease-2.2.0.apk" "apks\NLRelease-2.2.0.apk"
cp "%olddir%/NL/release/output.json" "apks\nloutput.json"
echo NL
cp "%olddir%/DK/release/output.json" "apks\output.json"
popd
for /f "tokens=2 delims==" %%x in (version.properties) do set Text=%%x
echo Version %Text%
