#!/usr/bin/bash

search_dir="C:\Gits\backupafdct\cvsrepo"



for repo in "$search_dir"/*/; do
	cd "C:\Gits\backupafdct\cvs2svn-2.5.0"
	echo "$repo"
	echo ${repo#*/}
	C:/Users/Andreas/.platformio/python27/python.exe cvs2git --blobfile=/tmp/gitblob.dat --dumpfile=/tmp/gitdump.dat "$repo" --encoding=WINDOWS-1252
	cd "C:\Gits\backupafdct\gits"
	git init --bare "${repo#*/}"
	cd "${repo#*/}"
	cat "/tmp/gitblob.dat" "/tmp/gitdump.dat" | git fast-import
	#read -p "Press [Enter] key to start backup..."
done