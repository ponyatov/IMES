import os,sys,time,re
cmd=''
for i in sys.argv: cmd += '"%s" '%i
open('log.log','w').write(cmd)
os.system('IMESc.py %s'%cmd)
