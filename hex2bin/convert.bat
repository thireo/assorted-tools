del main.bin
del code.bin
del codetest.bin
CALL touch.bat "main.bin"
CALL touch.bat "code.bin"
hex2bin /L65536 /P0xFF main.hex main.bin

echo Remember to add checksum + P's for the first 128 bytes, f.ex. "9B9APPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP"

::cat 128chars.txt >> code.bin
::cat main.bin >> code.bin

type 128chars.txt main.bin > code.bin

del main.bin


