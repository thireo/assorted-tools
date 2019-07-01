@echo off




if [%1]==[] (
	goto bob
) else (
	echo timing out in 30
	call loop
)

:loop
	echo Starter %1 installation
	pushd "\\DCNAS\docs\Danish Care\Produktion\Programmerings filer\Epi-Care mobile\Android App\2.2.0\" > NUL 2>&1
	cls
	call %1
	sleep 3
	popd
	goto loop
:bob
	echo Husk at angive SPROG (DK DE SE NO NL UK)
	exit /b 1
