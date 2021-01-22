# carina youtube downloader
# created by blackkucai
# stay cool
try:
    import pafy, os, sys, time
except ModuleNotFoundError:
    os.system('pip install pafy')
else:
    brs = '---------------------'

    def menu():
        try:
            os.system('clear')
            print('           ', 'YOUTUBE DOWNLODER')
            print('         ', brs)
            print('          ', '[1]. video ')
            print('          ', '[2]. audio')
            print('          ', '[3]. all')
            print('          ', '[4]. mixin')
            print('         ', brs)
            plh = input('          pilih :')
            if plh == '1':
                video()
            else:
                if plh == '2':
                    audio()
                else:
                    if plh == '3':
                        download()
                    else:
                        if plh == '4':
                            os.system('python mixin.pyc')
                        else:
                            if plh == 'q' or plh == 'Q':
                                sys.exit('thanks for coming')
                            else:
                                print('    ', 'pilihan[1,2,3 atau 4 dan q for exit] begoo !!')
                                time.sleep(2)
                                return menu()
        except ValueError:
            print('Not valid Value or Empty Input accured, try again.!')
            time.sleep(2)
            return menu()


    def video():
        url = input('          url:')
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
            except Error:
                sys.exit('bad connenction')
            else:
                print('download successfull')
                time.sleep(2)
                return menu()


    def audio():
        url = input('          url :')
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
            except Error:
                sys.exit('bad connection')
            else:
                print('download successfull')
                time.sleep(2)
                return menu()


    def download():
        url = input('          url:')
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