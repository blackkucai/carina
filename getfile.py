# getfile.py
# created by blackkucai
import os
                       
                                                  
def mixin(infile, infile1, outfile):                                                                          
    os.system(f"ffmpeg -y -loglevel repeat+info -i {infile} -i {infile1} -c copy -map 0:v:0 -map 1:a:0 {outfile}")