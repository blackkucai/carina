############################################
# carina script Youtube downloader   
# made by blackkucai 2021           
############################################                           
banner = '''\x1b[1;91m
       ▄▄·  ▄▄▄· ▄▄▄  ▪   ▐ ▄  ▄▄▄· \n      ▐█ ▌▪▐█ ▀█ ▀▄ █·██ •█▌▐█▐█ ▀█ \n      ██ ▄▄▄█▀▀█ ▐▀▀▄ ▐█·▐█▐▐▌▄█▀▀█ \n      ▐███▌▐█ ▪▐▌▐█•█▌▐█▌██▐█▌▐█ ▪▐▌\n      ·▀▀▀  ▀  ▀ .▀  ▀▀▀▀▀▀ █▪ ▀  ▀ \n'
\x1b[0m'''      
                 
try:
    import pafy, os, sys, time
    from mixin import merge, audiomp3
    from getfile import cdir
                       
except ModuleNotFoundError:
    os.system('pip install pafy')

else:        
    brs = '-'
               
    def anim(s):  
        for x in s + '\n':
            sys.stdout.write(x);sys.stdout.flush();time.sleep(0.1)
                                                                                                                                                                                                                                                   
    def menu():
        try:                                                                                                                   
            cdir()
            os.system('clear')            
            print('     ', banner)                                                      
            anim('---------[ YOUTUBE DOWNLOADER ]--------')
            anim('             [1]. Video ')
            anim('             [2]. Audio')
            anim('             [3]. Downloads')
            anim('             [4]. Mixing')
            anim('             [5]. audio2mp3')
            anim('             [q]. Exit')       
            anim('---------------------------------------')
            plh = input('CHOICES >>')        
            if plh == '1':
                 video()
            elif plh == '2':
                 audio()
            elif plh == '3':
                 download()
            elif plh == '4':
                 merge()
            elif plh == '5':
                 audiomp3()
            elif plh == 'q' or plh == 'Q':                       
                 sys.exit('\x1b[1;91mThanks For Coming\x1b[0m')
            else:      
                 print('ERROR: Invalid Choices')
                 time.sleep(2)
                 return menu()
                                                                                                                                                  
        except Exception as exceptions:              
            os.system('clear')                   
            print('\x1b[1;92mERROR:\x1b[0m%s' %(exceptions))
            time.sleep(5)                  
            return menu()
                           
        except(KeyboardInterrupt):                            
            print('\x1b[1;91mERROR:\x1b[0mInterrupted by User')                         
                                  
    def video():           
        os.system('clear')         
        url = input('Input Address >>')
        video = pafy.new(url)
        videostreams = video.videostreams
        print('getting filesize.')
        video.getbest()
        for i in videostreams:
            print('file size is %s' % i.get_filesize())
        else:
            print('downloading....')
            try:                         
                videostreams[3].download(filepath='download/video/')
            except Exception as exceptions:
                sys.exit(f'\x1b[1;96mERROR:\x1b[0m {exceptions}')
            else:                
                 print('download successfull')
                 time.sleep(2)
                 return menu()
                    
                                   
    def audio():
        os.system('clear')
        url = input('Input Address >>')
        audio = pafy.new(url)
        audiostreams = audio.audiostreams
        print('start collecting audio files..')
        print('getting file size')
        audio.getbest()
        for i in audiostreams:
            print('filesize is %s' % i.get_filesize())
        else:
            print('downloading.....')
            try:          
                audiostreams[3].download(filepath='download/audio/')
            except Exception as exceptions:                            
                sys.exit(f'\x1b[1;96mERROR:\x1b[0m {exceptions}')
            else:
                print('download successfull')
                time.sleep(2)
                return menu()
                           

    def download():
        os.system('clear')         
        url = input('Input Address >>')
        video = pafy.new(url)
        videostreams = video.videostreams
        print('getting filesize.')
        video.getbest()
        for i in videostreams:
            print('filesize is %s' % i.get_filesize())
        else:
            print('done')
            print('file downloading....')
            try:
                videostreams[3].download(filepath='download/video/')
            except ConnectionEtror:
                sys.exit('bad connection ')
            else:
                print('download successfull')
                time.sleep(1)
                print('downloading audio file..')
                audio = pafy.new(url)
                audiostreams = audio.audiostreams
                print('getting file size')
                audio.getbest()
                for i in audiostreams:
                    print('filesize is %s' % i.get_filesize())
                else:
                    print('done')
                    print('downloading.....')
                    try:
                        audiostreams[3].download(filepath='download/audio/')
                    except ConnectionError:
                        sys.exit('bad connection')
                    else:
                        print('download successfull')
                        print('start mixing files....')
                        print('mixing files....')
                        os.system('python mixin.py')

       
    if __name__ == '__main__':
       menu()