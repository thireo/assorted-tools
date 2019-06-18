echo OFF
if %1.==. goto end
if not exist %1 <nul (set/p z=) >%1
copy /b %1 +,,
echo %1 touched!
:end