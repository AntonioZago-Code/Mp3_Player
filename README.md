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

1. Add your MP3 files to the `Version_1.0/songs/` folder

2. Run the application:
```bash
python Version_1.0/main.py
```

3. Select a song by entering its number from the displayed list

4. Use the following commands during playback:
   - **P**: Pause the current song
   - **R**: Resume the paused song
   - **S**: Stop the current song
   - **Q**: Quit the application

## Project Structure

```
Mp3_Player/
├── README.md
├── LICENSE
├── Version_1.0/
│   ├── main.py              # Main application file
│   └── songs/               # Folder for MP3 files
└── .venv/                   # Virtual environment (optional)
```

## How It Works

The application uses the pygame library to handle audio playback:

1. **Initialization**: Initializes the pygame mixer for audio support
2. **File Discovery**: Scans the `songs/` folder for MP3 files
3. **Song Selection**: Displays available songs and waits for user input
4. **Playback Control**: Allows users to pause, resume, or stop playback
5. **Error Handling**: Validates file existence and directory integrity

## Version History

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

