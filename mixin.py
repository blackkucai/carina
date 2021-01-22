# mixin.py
# created by blackkucai
from getfile import mixin
import time, os             
os.system('ls download/video/ >> notempty')
with open('notempty') as f:
    a = f.read()          
    if a != '':
        infile = 'download/video/*'    
        infile1 = 'download/audio/*'
        outfile = 'outcarina.mkv'
        ml = mixin(infile, infile1, outfile)
        print('mixing complete')
        print('clearing directory ..!')
        os.system('mv -f download/audio/* download/mayang/')
        os.system('mv -f download/video/* download/mayang/')
        os.system('rm notempty')
    else:
        os.system('clear')
        print('    ', 'Directory Empty or File Not Found')
time.sleep(5)
os.system('python carina.pyc')