@ECHO OFF
SETLOCAL
mkdir crushed
FOR /F "tokens=*" %%G IN ('dir/b *.png') DO pngcrush -rem iCCP %%G crushed\%%G