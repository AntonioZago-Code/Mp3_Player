# MP3 Player

A simple Python application to play MP3 songs and manipulate playback with basic controls.

## Features

- **Play MP3 Files**: Load and play MP3 audio files from a designated folder
- **Playback Controls**: Pause, resume, and stop songs during playback
- **File Management**: List available MP3 files and select songs by number
- **User-Friendly Interface**: Simple command-line menu for easy navigation
- **Error Handling**: Validates files and directories to prevent unexpected errors
- **Cross-Platform**: Uses pygame for audio playback, compatible with Windows, macOS, and Linux

## Requirements

- Python 3.14.0
- pygame library

## Installation

1. Clone the repository:
```bash
git clone https://github.com/AntonioZago-Code/Mp3_Player.git
cd Mp3_Player
```

2. Create a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install pygame
```

## Usage

1. Add your MP3 files to the `Version_1.2/songs/` folder

2. Run the application:
```bash
python Version_1.2/mp3Player.py
```

3. Select a song by entering its number from the displayed list

4. Use the following commands during playback:
   - **P**: Pause the current song
   - **R**: Resume the paused song
   - **B**: Begin/Replay the current song from the start
   - **S**: Stop the current song

5. Additional features:
   - Press **R** from the menu to play a random song
   - Press **Q** from the menu to quit the application

## Project Structure

```
Mp3_Player/
├── README.md
├── LICENSE
├── Version_1.0/
│   ├── main.py              # Version 1.0 application file
│   └── songs/               # Folder for MP3 files
├── Version_1.1/
│   ├── main.py              # Version 1.1 application file
│   └── songs/               # Folder for MP3 files
├── Version_1.2/
│   ├── mp3Player.py         # Main application file (Latest)
│   ├── fileControler.py     # File management module
│   ├── songControler.py     # Song playback module
│   └── songs/               # Folder for MP3 files
└── .venv/                   # Virtual environment (optional)
```

## How It Works

Version 1.2 uses a modular architecture with three main components:

1. **mp3Player.py** - Main application controller
   - Handles user interface and menu system
   - Manages song selection and playback flow
   - Uses Files and Song classes for operations

2. **fileControler.py** - File management module
   - Scans and lists MP3 files from directory
   - Validates file existence and paths
   - Returns file paths for playback

3. **songControler.py** - Song playback module
   - Manages pygame mixer initialization
   - Handles play, pause, resume, replay, and stop operations
   - Processes user commands during playback

**Workflow**:
1. **Initialization**: Mp3Player initializes with Files class pointing to songs folder
2. **File Discovery**: Files class scans directory and returns list of MP3 files
3. **Song Selection**: User selects song by number or requests random selection
4. **Playback Control**: Song class handles all playback operations and user commands
5. **Error Handling**: Each module validates data and handles errors gracefully

## Version History

### Version 1.2 (Current)
- Complete code refactor with modular architecture
- **mp3Player.py**: Main application controller
- **songControler.py**: Handles song playback operations
- **fileControler.py**: Manages file and directory operations
- Improved separation of concerns and code maintainability
- Enhanced error handling and user interface
- Object-oriented design for better scalability

### Version 1.1
- Added replay/begin command to restart current song
- Random song selection feature
- Improved user menu interface
- Enhanced event handling for song completion

### Version 1.0
- Initial release
- Basic MP3 playback functionality
- Play, pause, resume, and stop controls
- Song selection from directory

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.

## Author

**Antonio Zago** - [GitHub Profile](https://github.com/AntonioZago-Code)

## Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests

## Future Improvements

- Implement playlist functionality
- Add song shuffle and repeat modes
- Display song lyrics during playback
- Create a graphical user interface (GUI)
- Display current playback time and song duration
- Add support for additional audio formats

---

**Enjoy your music!** 🎵

