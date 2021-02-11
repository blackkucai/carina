# getfile script
# created by blackkucai 2021
#############################
import os
                                                                            
def mixin(infile, infile1, outfile):
    print('merging.....')                                                                               
    os.system(f"ffmpeg -y -loglevel repeat+info -i {infile} -i {infile1} -c copy -map 0:v:0 -map 1:a:0 {outfile}")

def audio2mp3(file, out):
    print('converting...')                                         
    os.system(f'ffmpeg -y -loglevel repeat+info -i {file} {out}')
                
def cdir():
    dire = 'False'
    print('checking download directory')
    sc = os.system('find . -name download >> _isok')
    with open('_isok', 'r') as f:
         a = f.read()
         if a == '':
            dire = 'True'
            print('creating directory..')
            os.mkdir('download')
            os.mkdir('download/mayang')
            os.mkdir('download/audio')
            os.mkdir('download/video')
            os.mkdir('download/dist')
            f.close()
            os.system('rm _isok')
            print('creating dirs done')
         else:                     
            print(dire)
            os.system('rm _isok')

                  
 
