# -*- coding: cp1251 -*-
# клиент: IMESc[.exe] Program.nc [<IP стойки станка>]

# IP порт на котором висит IMESd
PORT = 1234

import os,sys,time,socket,winsound

# имя файла с программой передается в командной строке первым параметром
NCFILE=sys.argv[1] # r'E:\IMES\FTP\F.nc'
# IP адрес станка
try:
	CNCIP = sys.argv[2]
except IndexError:
	CNCIP = '192.168.255.18' # IMES4820

# загружаем файл .nc
# открываем файл программы на чтение и читаем файл
F=open(NCFILE,'r')
NC=F.read()
# закрываем файл
F.close()

# открываем сокет клиента
S=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# устанавливаем таймаут на соединение
S.settimeout(1)
# цепляемся на станок
try:
	S.connect((CNCIP,PORT))
	# посылаем файл программы на активный сокет
	S.send(NC)
	# закрываем сокет
	S.close()
	# выходим с кодом 0 сообщая что ошибок не было
	# (при каких-то сбоях/исключениях рантайм питона завершает программу с ненулевым кодом)
	winsound.Beep(440,500)
	print NC
	raw_input('.')
	sys.exit(0)
except socket.timeout:
	winsound.Beep(888,1500)
	print '\nERROR: %s:%s socket.timeout\n'%(CNCIP,PORT)
	raw_input('.')
	sys.exit(-1)

