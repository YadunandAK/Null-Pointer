# 🎭 The Unhelpful Mood Mixer

A humorous web application that analyzes your facial emotions and responds with witty, mildly mocking comments while recommending YouTube playlists for the *opposite* of your current mood. Because sometimes you need to be told your happiness is too loud! 😄

## 🌟 Features

### Core Functionality
- **Emotion Detection**: Uses DeepFace AI to analyze facial expressions from uploaded images
- **Witty Responses**: Three different roasting styles (Polite, Sassy, Roastmaster)
- **Opposite Mood Recommendations**: Suggests YouTube playlists that contradict your current emotional state
- **Real-time Analysis**: Upload selfies or use webcam for instant mood analysis

### UI Features
- **Beautiful Gradio Interface**: Modern, responsive web UI with gradient animations
- **Multiple Input Methods**: Upload images or capture directly from webcam
- **Customizable Roasting**: Choose your preferred level of sass
- **Reload Button**: Get fresh roasts for the same detected emotion
- **Animated Results**: Smooth slide-in animations for result panels

### Supported Emotions
- **Happy** → Recommends Sad music
- **Sad** → Recommends Happy music  
- **Angry** → Recommends Calm music
- **Fear** → Recommends Confident music
- **Surprise** → Recommends Bored music
- **Disgust** → Recommends Satisfied music
- **Neutral** → Recommends Excited music

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- A sense of humor
- Thick skin (optional but recommended)

### Installation

1. **Clone or download the project files**
2. **Create a virtual environment:**
   ```bash
   python3 -m venv mood_mixer_env
   source mood_mixer_env/bin/activate  # On Windows: mood_mixer_env\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install gradio opencv-python Pillow numpy
   ```

4. **Run the demo application:**
   ```bash
   python simple_app.py
   ```

5. **Open your browser** and navigate to the provided URL (typically `http://localhost:7860`)

### Full AI Version (Requires TensorFlow/DeepFace)

For the full version with real emotion detection:
```bash
pip install deepface tensorflow
python app.py
```
*Note: May require Python 3.8-3.11 for TensorFlow compatibility*

## 📁 Project Structure

```
unhelpful-mood-mixer/
├── app.py              # Full application with DeepFace AI emotion detection
├── simple_app.py       # Demo version with mock emotion detection
├── mood_data.py        # Emotion mappings, messages, and playlists
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## 🎯 How It Works

1. **Upload Your Face**: Use the image upload or webcam capture
2. **Choose Roasting Style**: Select from Polite, Sassy, or Roastmaster
3. **Get Analyzed**: AI detects your dominant emotion with confidence score
4. **Receive Your Roast**: Get a humorous comment based on your emotion and chosen style
5. **Discover Opposite Music**: Get a YouTube playlist recommendation for the opposite mood
6. **Reload for More**: Hit the reload button to get fresh roasts for the same emotion

## 🎭 Roasting Styles

### 😊 Polite
Backhanded compliments and passive-aggressive observations
> "Oh wonderful, another person radiating joy. How... refreshing. 🙄"

### 😏 Sassy  
Direct, witty commentary with attitude
> "Okay, we get it. You're happy. No need to blind us with that smile. ✨"

### 🔥 Roastmaster
Full roast mode with creative comparisons
> "Your happiness is so intense, I'm worried you might pull a muscle. Stretch first! 🤸"

## 🎵 Music Recommendations

The app includes real curated YouTube playlists for each mood:
- **Sad Songs to Balance Your Joy** (for when you're detected as happy)
- **Happy Pop Hits** (for when you're detected as sad)
- **Calm Chillhop Beats** (for when you're detected as angry)
- **Rage Rock & Metal** (for when you're detected as calm)
- **Confident Pop Anthems** (for when you're detected as fearful)
- **Awkward Slow Jams** (for when you're detected as confident)
- **Crazy Energetic Hits** (for when you're detected as bored)
- **Slow Ambient Chill** (for when you're detected as excited)
- **Soft Love Songs** (for when you're detected as disgusted/satisfied)
- **Cringe Bangers** (for when you're detected as content)

## 🛠 Technical Details

### Dependencies
- **Gradio**: Web interface framework
- **DeepFace**: Facial emotion analysis
- **OpenCV**: Image processing
- **TensorFlow**: AI model backend
- **Pillow**: Image handling
- **NumPy**: Numerical operations

### AI Model
Uses DeepFace's pre-trained emotion detection models with fallback handling for edge cases.

### Error Handling
- Graceful fallbacks if emotion detection fails
- Temporary file cleanup
- User-friendly error messages

## 🎨 Customization

### Adding New Emotions
Edit `mood_data.py` to add new emotion mappings:
```python
EMOTION_OPPOSITES["new_emotion"] = "opposite_emotion"
```

### Adding New Roasting Messages
Add messages to the `MOCKING_MESSAGES` dictionary:
```python
MOCKING_MESSAGES["your_style"]["emotion"].append("Your new roast message! 🔥")
```

### Adding New Playlists
Update the `YOUTUBE_PLAYLISTS` dictionary with new playlist data:
```python
YOUTUBE_PLAYLISTS["mood"] = {
    "title": "Playlist Name",
    "url": "https://youtube.com/playlist?list=...",
    "description": "Your description"
}
```

## 🚨 Disclaimers

- This app is designed for **entertainment purposes only**
- All roasts are meant to be **lighthearted and humorous**
- No actual mood therapy is provided (shocking, we know!)
- If you're having a genuinely tough day, please talk to someone who cares about you 💙
- The AI might occasionally be confused by your face (it happens to the best of us)
- **Demo Version**: The current `simple_app.py` uses mock emotion detection for demonstration. The full AI version requires TensorFlow compatibility.

## 🤝 Contributing

Feel free to contribute by:
- Adding more creative roasting messages
- Improving the emotion detection accuracy
- Creating better playlist recommendations
- Enhancing the UI/UX
- Fixing bugs (if you find any, which is impossible because this is perfect code)

## 📝 License

This project is open source and available under the MIT License. Use it, modify it, roast it - we don't care! 😄

## 🙏 Acknowledgments

- **DeepFace** team for the emotion detection models
- **Gradio** team for the amazing web interface framework
- Everyone who contributed roasting inspiration
- Your face, for being roastable

---

*Remember: Life's too short to take yourself seriously. Sometimes you need an AI to remind you of that!* 🎭✨