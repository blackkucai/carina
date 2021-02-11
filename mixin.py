############################################
# mixing script made by                    #
# blackkucai 2021                          #
############################################  
import time, os                
                 
      
def merge():            
    # getting modules
    from getfile import mixin        
    from carina import menu, anim                         

    # checking availability file
    os.system('ls download/video/ >> _isempty')
    with open('_isempty', 'r') as f:
         a = f.read()             
         if a != '':                             
            infile = 'download/video/*'  
            infile1 = 'download/audio/*'                             
            outfile = '{}.mkv'.format(infile).replace('*','outcarina')
            ml = mixin(infile, infile1, outfile)
            print('mixing complete')

            # deleting moving files downloaded
            print('clearing directory ..!')
            os.system('mv -f download/audio/* download/mayang/')
            os.system('mv -f download/video/* download/mayang/')
            os.system('rm _isempty')
            time.sleep(3); return menu()                                              

         else:
            #printing non exist file                           
            print('checked file availablity.')
            anim('\x1b[1;91mDirectory Empty or File Not Found\x1b[0m')
                                              
            # deleting temporary file
            os.system('rm _isempty') 
            time.sleep(3);return menu()

def audiomp3():                
    # getting modules
    from getfile import audio2mp3
    from carina import menu, anim   

    # checking availablity source                                
    print('cheking source file..')
    os.system('ls download/audio/ >> _isexist')
    time.sleep(2)                    
    with open('_isexist', 'r') as f:
         a = f.read()       
         if a == '':                                      
            anim('\x1b[1;91mAudio file doesnt exist\x1b[0m')
            os.system('rm _isexist')                     
            time.sleep(3);return menu()
                                                        
         else:                                   
            # converting file
            file = 'download/audio/*'  
            out = '{}.mp3'.format(file).replace('*','out')
            mp3 = audio2mp3(file,out)
            print('converting completed');print('moving file & removing..')    
            
            # deleting files and move 
            os.system('rm _isexist')
            os.system('mv download/audio/*.mp3 download/dist/')
            print('done'); time.sleep(3); return menu()


