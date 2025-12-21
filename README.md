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
# MP3 Player

A simple Python application to play MP3 songs with a command-line interface and basic playback controls.

## Features

- **Play MP3 Files**: Load and play MP3 audio files from a designated folder
- **Playback Controls**: Pause, resume, replay and stop songs during playback
- **File Management**: List available MP3 files and select songs by number
- **Random Playback**: Play a random song from the collection
- **Modular Design**: Clear separation between file handling and playback logic
- **Cross-Platform**: Uses `pygame` for audio playback, compatible with Windows, macOS, and Linux

## Requirements

- Python 3.8+ (Python 3.14 recommended)
- `pygame` library

## Installation

1. Clone the repository:
```bash
git clone https://github.com/AntonioZago-Code/Mp3_Player.git
cd Mp3_Player
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install pygame
```

## Usage

1. Add your MP3 files to the `Version_2.0/songs/` folder.

2. Run the application:
```bash
python Version_2.0/Mp3Player.py
```

3. From the menu you can:
   - Select a song by number
   - Press `R` to play a random song
   - Press `Q` to quit

4. During playback use these controls:
   - `P`: Pause the current song
   - `R`: Resume the paused song
   - `B`: Begin/Replay the current song from the start
   - `S`: Stop the current song

## Project Structure

```
Mp3_Player/
├── README.md
├── LICENSE
├── Version_1.0/
│   ├── main.py
│   └── songs/
├── Version_1.1/
│   ├── main.py
│   └── songs/
├── Version_1.2/
│   ├── mp3Player.py
│   ├── fileControler.py
│   ├── songControler.py
│   └── songs/
├── Version_2.0/
│   ├── Mp3Player.py        # Main application (Current)
│   ├── fileControler.py     # File management module
│   ├── songControler.py     # Song playback module
│   └── songs/               # Folder for MP3 files
└── .venv/                   # Virtual environment (optional)
```

## How It Works

Version 2.0 continues the modular architecture and improves the main runner and controls:

1. **Mp3Player.py** - Main application controller
   - Presents the command-line menu
   - Handles song selection, random selection and playback flow
   - Orchestrates `Files` and `Song` classes

2. **fileControler.py** - File management module
   - Scans and lists MP3 files from the `songs/` directory
   - Validates file existence and returns playable paths

3. **songControler.py** - Song playback module
   - Initializes and manages `pygame.mixer`
   - Handles play, pause, resume, replay and stop operations
   - Processes user commands during playback

**Workflow**:
1. **Initialization**: `Mp3Player` initializes `Files` pointing to `Version_2.0/songs/`
2. **File Discovery**: `Files` scans the folder and returns available MP3 paths
3. **Song Selection**: User selects a song or requests a random selection
4. **Playback Control**: `Song` manages playback and user controls

## Version History

### Version 2.0 (Current)

- Main runner renamed to `Mp3Player.py` and improved CLI
- Better modularization and clearer separation between file handling and playback
- Improved input handling and robustness
- Preserves play/pause/resume/replay/stop and random selection features
- Updated README and project structure

### Version 1.2

- Complete code refactor with modular architecture
- `mp3Player.py`: Main application controller
- `songControler.py`: Handles song playback operations
- `fileControler.py`: Manages file and directory operations

### Version 1.1

- Added replay/begin command to restart current song
- Random song selection feature
- Improved user menu interface

### Version 1.0

- Initial release with basic MP3 playback functionality

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
- Add shuffle and repeat modes
- Display song duration and playback position
- Add support for additional audio formats

---

Enjoy your music! 🎵

