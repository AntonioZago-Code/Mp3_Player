import os


class Files():

    def __init__(self, folder):
        
        if not os.path.isdir(folder):

            print(f"Fouder {folder} not found!")
            self.folder = ""

        self.folder = folder


    def mp3_files(self) -> list:

        mp3_files = [file for file in os.listdir(self.folder) if file.endswith(".mp3")]

        if not mp3_files:

            print("No .mp3 file found!")
            mp3_files = []
        
        return mp3_files


    def file_path(self, index) -> str:

        mp3_files = self.mp3_files()

        file_path = os.path.join(self.folder, mp3_files[index])

        if not os.path.exists(file_path):

            print("File not found")
            file_path = ""

        return file_path    