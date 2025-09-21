# Language Translator

A Python-based real-time language translation application that uses speech recognition, Google Translate API, and text-to-speech capabilities to provide seamless voice translation between different languages.

## Features

- **Speech Recognition**: Convert spoken words to text using Google's speech recognition API
- **Real-time Translation**: Translate text between multiple languages using Google Translate
- **Text-to-Speech**: Convert translated text back to speech and play it automatically
- **Voice Activation**: Start translation by saying "Hello"
- **Multiple Language Support**: Support for various source and destination languages
- **Audio Output**: Save translated speech as MP3 files

## Files Overview

- `demo.py`: Basic demonstration script with English to Spanish translation
- `translate.py`: Interactive version allowing users to specify source and destination languages
- `captured_voice.mp3`: Audio output file (generated during execution)
- `translated.mp3`: Audio output file (generated during execution)

## Requirements

### Python Packages
```
speech_recognition
googletrans==4.0.0rc1
gTTS
pyaudio
```

### System Requirements
- Python 3.7+
- Microphone access
- Internet connection (for Google services)
- Audio playback capability

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Nortcele7/Language_Translator.git
   cd Language_Translator
   ```

2. **Install required packages:**
   ```bash
   pip install speech_recognition googletrans==4.0.0rc1 gTTS pyaudio
   ```

   **Note**: If you encounter issues installing `pyaudio` on Windows, you may need to install it using:
   ```bash
   pip install pipwin
   pipwin install pyaudio
   ```

3. **Verify microphone access:**
   Ensure your system has a working microphone and appropriate permissions.

## Usage

### Basic Demo (English to Spanish)
```bash
python demo.py
```
1. Say "Hello" to initiate the translator
2. Speak the sentence you want to translate
3. Listen to the Spanish translation

### Interactive Translation
```bash
python translate.py
```
1. Enter the source language code (e.g., 'en' for English)
2. Enter the destination language code (e.g., 'es' for Spanish)
3. Say "Hello" to start translation
4. Speak your sentence
5. Listen to the translated audio

### Supported Language Codes
- `en` - English
- `es` - Spanish
- `fr` - French
- `de` - German
- `it` - Italian
- `pt` - Portuguese
- `ru` - Russian
- `ja` - Japanese
- `ko` - Korean
- `zh` - Chinese
- And many more...

## How It Works

1. **Voice Capture**: The application listens for the wake word "Hello"
2. **Speech Recognition**: Converts your spoken words to text using Google's speech recognition API
3. **Translation**: Uses Google Translate API to translate the text to the target language
4. **Text-to-Speech**: Converts the translated text to speech using gTTS (Google Text-to-Speech)
5. **Audio Playback**: Plays the translated audio and saves it as an MP3 file

## Example Usage

```
$ python translate.py
Enter the source language: en
Enter the destination language: fr
Speak Hello to initiate the translator
[User says: "Hello"]
Speak to translate from en to fr
[User says: "Good morning, how are you?"]
Bonjour, comment allez-vous?
[Plays French audio]
```

## Troubleshooting

### Common Issues

1. **Microphone not recognized:**
   - Check microphone permissions
   - Ensure microphone is properly connected
   - Try adjusting the ambient noise duration

2. **Translation errors:**
   - Verify internet connection
   - Check if the language codes are correct
   - Ensure clear speech for better recognition

3. **Audio playback issues:**
   - Verify system audio settings
   - Check if MP3 files are being created
   - Ensure audio drivers are up to date

### Dependencies Issues
- If `googletrans` gives errors, make sure to install version `4.0.0rc1`
- For `pyaudio` installation issues on Windows, use `pipwin` as mentioned above

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Future Enhancements

- [ ] GUI interface using tkinter or PyQt
- [ ] Support for offline translation
- [ ] Multiple simultaneous language translation
- [ ] Voice selection options
- [ ] Translation history and favorites
- [ ] Real-time conversation mode
- [ ] Integration with other translation services

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Google Speech Recognition API
- Google Translate API
- Google Text-to-Speech (gTTS)
- Python Speech Recognition library

## Contact

Project Link: [https://github.com/Nortcele7/Language_Translator](https://github.com/Nortcele7/Language_Translator)

---

**Note**: This application requires an active internet connection as it uses Google's cloud services for speech recognition, translation, and text-to-speech functionality.