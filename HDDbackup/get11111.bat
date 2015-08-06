rem on IMES:
rem sudo sh
rem mkfifo fifo
rem nc -l -p 11111 -e cat fifo &
rem dd if=/dev/sda of=fifo bs=512 count=1

nc64 192.168.255.1 11111 > dmesg.txt
pause

