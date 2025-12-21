from pygame import mixer, error
from fileControler import Files


class Song():

    def __init__(self):
        
        try:
            mixer.init()

        except error as e:
            print("Audio initialization failed! ", e)
            return
        

        self.folder = Files('Version_2.0/songs')
        
        

    def play(self, index):

        file_path = self.folder.file_path(index)

        mixer.music.load(file_path)
        mixer.music.play()


    def pause(self):

        mixer.music.pause()


    def unpause(self):

        mixer.music.unpause()


    def replay(self):

        mixer.music.rewind()


    def stop(self):

        mixer.music.stop()
