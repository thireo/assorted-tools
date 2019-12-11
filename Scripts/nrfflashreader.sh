nrfjprog --memrd 512001 --w 8 | cut -d ' ' -f 2
nrfjprog --memrd 512002 --w 8 | cut -d ' ' -f 2
nrfjprog --memrd 512003 --w 8 | cut -d ' ' -f 2
nrfjprog --memrd 512004 --w 8 | cut -d ' ' -f 2
nrfjprog --memrd 512005 --w 8 | cut -d ' ' -f 2
nrfjprog --memrd 512006 --w 8 | cut -d ' ' -f 2
echo checksum
nrfjprog --memrd 512007 --w 8 | cut -d ' ' -f 2

echo softresetting...
nrfjprog -d
