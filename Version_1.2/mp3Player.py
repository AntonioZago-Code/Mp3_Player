from songControler import Song
from fileControler import Files

import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"


class Mp3Player():

    def __init__(self):
        
        self.folder = Files('Version_1.2/songs')
        self.mp3_files = self.folder.mp3_files()


    def display_songs(self):

        for index, song in enumerate(self.mp3_files, start=1):
            print(f"{index}. {song}")

        print("\nEnter the song number to play;")
        print("Enter 'R' to play a random song;")
        print("Or 'Q' to quit)\n")


    def get_choice(self):

        choice_input = input("\n> ")

        if choice_input.upper() == "Q":

            print("\nApp Closed!\n")
            return False
        
        if choice_input.upper() == "R":

            print("\nA random song is playing...\n")

            random_choice = int(os.urandom(1)[0]) % len(self.mp3_files)
            return random_choice
        
        else:
            return choice_input


    def start_app(self):

        print("\n==================== MP3 PLAYER ====================\n")

        while True:

            

            self.display_songs()

            choice = self.get_choice()
            if choice == "":
                continue

            if not choice:
                break


            try:

                choice = int(choice) - 1

                if 0 <= choice < len(self.mp3_files):
                    
                    file_path = self.folder.file_path(choice)

                    song = Song(file_path)

                    song.run()
                
                else:
                    print("Invalid choice!! Try again.")

            except:

                print("Enter a valid number!!")
                continue




if __name__ == "__main__":

    app = Mp3Player()
    app.start_app()