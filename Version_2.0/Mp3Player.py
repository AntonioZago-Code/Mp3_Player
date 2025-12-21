from fileControler import Files
from songControler import Song
import customtkinter as ctk



class App(ctk.CTk):

    def __init__(self):
        super().__init__()


        self.title("Mp3 Player")
        self.geometry('600x700')
        self.resizable(width=False, height=False)

        self.grid_columnconfigure(0, weight=1)
        # self.grid_rowconfigure((0, 1), weight=1)


        self.folder = Files('Version_2.0/songs')
        self.mp3_files = self.folder.mp3_files()

        self.songFunctions = Song()


        self.app_title = ctk.CTkLabel(
            self,
            text="Mp3 Player",
            text_color='#00f',
            font=('Arial', 32, "bold")
        )

        self.app_title.grid(
            row=0,
            column=0,
            padx=10,
            pady=20
        )

        self.songs = SongsList(self, self.mp3_files, self.songFunctions)
        self.songs.grid(row=2, column=0, pady=10)

        self.commands = Commands(self, self.songFunctions)
        self.commands.grid(row=3, column=0, pady=10)



    
class SongsList(ctk.CTkScrollableFrame):

    def __init__(self, master, mp3_files, song_functions,
                 width=550, height=500, corner_radius=20):

        super().__init__(
            master,
            width=width,
            height=height,
            corner_radius=corner_radius
        )

        self.grid_columnconfigure(0, weight=1)

        self.mp3_files = mp3_files
        self.songFunctions = song_functions
        self.song_buttons = []

        for index, song in enumerate(self.mp3_files, start=1):

            song_index = index - 1

            button = ctk.CTkButton(
                self,
                text=f"{index}. {song}",
                font=('Arial', 24),
                anchor="w",
                fg_color="transparent",
                hover_color="#333",
                command=lambda i=song_index: self.songFunctions.play(i)
            )

            button.grid(
                row=index,
                column=0,
                padx=50,
                pady=5,
                sticky="w"
            )

            self.song_buttons.append(button)



class Commands(ctk.CTkFrame):

    def __init__(self, master, song_functions):
        super().__init__(master)

        self.songFunctions = song_functions


        self.paused = False


        # REPLAY BUTTOM
        self.replay_button = ctk.CTkButton(
            self,
            text="⏮",
            width=40,
            command=lambda: self.songFunctions.replay()
        )
        self.replay_button.grid(row=0, column=0, padx=10)

        # PAUSE BUTTOM
        self.pause_button = ctk.CTkButton(
            self,
            text="⏸",
            width=40,
            command=lambda: self.toggle_pause()
        )
        self.pause_button.grid(row=0, column=1, padx=10)

    
    def toggle_pause(self):
        if self.paused:
            self.songFunctions.unpause()
            self.pause_button.configure(text="⏸")
        else:
            self.songFunctions.pause()
            self.pause_button.configure(text="▶")

        self.paused = not self.paused



if __name__ == "__main__":

    app = App()
    app.mainloop()