from pygame import mixer, error, event, USEREVENT

class Song():

    def __init__(self, file_path):
        
        try:
            mixer.init()

        except error as e:
            print("Audio initialization failed! ", e)
            return
        
        self.file_path = file_path

        self.MUSIC_END = USEREVENT + 1
        mixer.music.set_endevent(self.MUSIC_END)


    def play(self):

        mixer.music.load(self.file_path)
        mixer.music.play()


    def pause(self):

        mixer.music.pause()
        print("\nPAUSED")

    def unpause(self):

        mixer.music.unpause()
        print("\nRESUMED")

    def replay(self):

        mixer.music.rewind()
        print("\nREPLAYED")

    def stop(self):

        mixer.music.stop()
        print("\nSTOPED")


    def commands_menu(self):

        print("""
        Commands:
            [P] PAUSE
            [R] RESUME
            [B] BEGIN
            
            [L] NEXT
              
            [S] STOP

        """)


    def run(self):

        self.commands_menu()
        
        self.play()

        while True:

            command = input("> ").upper()

            if command == "P": self.pause()
            elif command == "R": self.unpause()
            elif command == "B": self.replay()
            elif command == "S": self.stop(); return False

            else: 
                print("Invalid command")

                
