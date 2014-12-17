# -*- coding: cp1251 -*-
# ������: IMESc[.exe] Program.nc [<IP ������ ������>]

# IP ���� �� ������� ����� IMESd
PORT = 1234

import os,sys,time,socket,winsound

# ��� ����� � ���������� ���������� � ��������� ������ ������ ����������
NCFILE=sys.argv[1] # r'E:\IMES\FTP\F.nc'
# IP ����� ������
try:
	CNCIP = sys.argv[2]
except IndexError:
	CNCIP = '192.168.255.18' # IMES4820

# ��������� ���� .nc
# ��������� ���� ��������� �� ������ � ������ ����
F=open(NCFILE,'r')
NC=F.read()
# ��������� ����
F.close()

# ��������� ����� �������
S=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# ������������� ������� �� ����������
S.settimeout(1)
# ��������� �� ������
try:
	S.connect((CNCIP,PORT))
	# �������� ���� ��������� �� �������� �����
	S.send(NC)
	# ��������� �����
	S.close()
	# ������� � ����� 0 ������� ��� ������ �� ����
	# (��� �����-�� �����/����������� ������� ������ ��������� ��������� � ��������� �����)
	winsound.Beep(440,500)
	print NC
	raw_input('.')
	sys.exit(0)
except socket.timeout:
	winsound.Beep(888,1500)
	print '\nERROR: %s:%s socket.timeout\n'%(CNCIP,PORT)
	raw_input('.')
	sys.exit(-1)

