import gradio as gr
import numpy as np
import random
import time
from PIL import Image
import cv2

from mood_data import (
    EMOTION_OPPOSITES, 
    MOCKING_MESSAGES, 
    YOUTUBE_PLAYLISTS, 
    EMOTION_EMOJIS
)

class MoodMixer:
    def __init__(self):
        self.last_emotion = None
        self.last_style = None
        
    def detect_emotion_mock(self, image):
        """Mock emotion detection for demonstration purposes"""
        # Simulate processing time
        time.sleep(0.5)
        
        # Randomly select an emotion for demonstration
        emotions = list(EMOTION_EMOJIS.keys())
        emotion = random.choice(emotions)
        confidence = random.uniform(0.7, 0.95)  # Mock confidence between 70-95%
        
        return emotion, confidence
    
    def get_mocking_message(self, emotion, style):
        """Get a random mocking message based on emotion and style"""
        try:
            messages = MOCKING_MESSAGES[style][emotion]
            return random.choice(messages)
        except KeyError:
            return "I'm too confused by your face to mock it properly. 🤷‍♀️"
    
    def get_opposite_playlist(self, emotion):
        """Get YouTube playlist for the opposite emotion"""
        try:
            opposite_emotion = EMOTION_OPPOSITES[emotion]
            playlist = YOUTUBE_PLAYLISTS[opposite_emotion]
            return opposite_emotion, playlist
        except KeyError:
            # Fallback playlist
            return "happy", YOUTUBE_PLAYLISTS["happy"]
    
    def analyze_mood(self, image, mocking_style):
        """Main function to analyze mood and return results"""
        if image is None:
            return "", "", ""
        
        # Add dramatic pause for effect
        time.sleep(1)
        
        # Mock emotion detection (replace with DeepFace when available)
        emotion, confidence = self.detect_emotion_mock(image)
        self.last_emotion = emotion
        self.last_style = mocking_style
        
        # Get mocking message
        mocking_message = self.get_mocking_message(emotion, mocking_style)
        
        # Get opposite mood playlist
        opposite_emotion, playlist = self.get_opposite_playlist(emotion)
        
        # Format results with emojis and styling
        emotion_result = f"📸 **Detected Mood:** {EMOTION_EMOJIS[emotion]} {emotion.title()} ({confidence:.1%} confidence)\n\n*Note: This is a demo using mock emotion detection. In the full version, this would use DeepFace AI.*"
        
        mocking_result = f"🎭 **{mocking_style.title()} Roast:** {mocking_message}"
        
        playlist_result = f"""🔗 **Opposite Mood Playlist:** 
Since you're feeling {emotion}, here's some {opposite_emotion} music to balance you out:
**[{playlist['title']}]({playlist['url']})**
*{playlist['description']}*"""
        
        return emotion_result, mocking_result, playlist_result
    
    def reload_message(self, mocking_style):
        """Generate a new mocking message for the same emotion"""
        if self.last_emotion and self.last_style:
            mocking_message = self.get_mocking_message(self.last_emotion, mocking_style or self.last_style)
            return f"🎭 **{(mocking_style or self.last_style).title()} Roast:** {mocking_message}"
        return "Upload an image first to get roasted! 📸"

# Initialize the mood mixer
mood_mixer = MoodMixer()

# Custom CSS for styling and animations
custom_css = """
.result-panel {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    border-radius: 15px;
    padding: 20px;
    margin: 10px 0;
    color: white;
    box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
    backdrop-filter: blur(4px);
    border: 1px solid rgba(255, 255, 255, 0.18);
    animation: slideIn 0.5s ease-out;
}

@keyframes slideIn {
    from {
        opacity: 0;
        transform: translateY(30px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.title-header {
    text-align: center;
    background: linear-gradient(45deg, #ff6b6b, #4ecdc4, #45b7d1, #96ceb4);
    background-size: 400% 400%;
    animation: gradient 3s ease infinite;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-size: 2.5em;
    font-weight: bold;
    margin-bottom: 20px;
}

@keyframes gradient {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

.demo-notice {
    background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 100%);
    border-radius: 10px;
    padding: 15px;
    margin: 20px 0;
    text-align: center;
    font-weight: bold;
    color: #333;
    border: 2px solid #ff6b6b;
}

.mood-emoji {
    font-size: 3em;
    text-align: center;
    margin: 20px 0;
}
"""

# Create Gradio interface
def create_interface():
    with gr.Blocks(css=custom_css, title="The Unhelpful Mood Mixer - Demo") as demo:
        
        # Header
        gr.HTML("""
        <div class="title-header">
            🎭 The Unhelpful Mood Mixer 🎭
        </div>
        <div style="text-align: center; font-size: 1.2em; color: #666; margin-bottom: 30px;">
            Upload your face, get roasted, and receive completely unhelpful mood recommendations! 😈
        </div>
        """)
        
        # Demo notice
        gr.HTML("""
        <div class="demo-notice">
            🎬 DEMO VERSION: This uses mock emotion detection for demonstration purposes.<br>
            The full version would use DeepFace AI for real facial emotion analysis!
        </div>
        """)
        
        with gr.Row():
            with gr.Column(scale=1):
                # Input section
                gr.HTML("<h3>📸 Upload Your Face for Analysis</h3>")
                image_input = gr.Image(
                    type="pil",
                    label="Upload a selfie or use webcam",
                    sources=["upload", "webcam"]
                )
                
                mocking_style = gr.Dropdown(
                    choices=["polite", "sassy", "roastmaster"],
                    value="sassy",
                    label="🎯 Choose Your Roasting Style",
                    info="How brutally honest should I be?"
                )
                
                with gr.Row():
                    analyze_btn = gr.Button(
                        "🔍 Analyze My Mood", 
                        variant="primary",
                        size="lg"
                    )
                    reload_btn = gr.Button(
                        "🔄 New Roast (Same Mood)",
                        variant="secondary"
                    )
            
            with gr.Column(scale=1):
                # Results section
                gr.HTML("<h3>🎭 Your Unhelpful Analysis</h3>")
                
                emotion_output = gr.Markdown(
                    label="Detected Emotion",
                    elem_classes=["result-panel"]
                )
                
                mocking_output = gr.Markdown(
                    label="Mocking Message", 
                    elem_classes=["result-panel"]
                )
                
                playlist_output = gr.Markdown(
                    label="Opposite Mood Playlist",
                    elem_classes=["result-panel"]
                )
        
        # Event handlers
        analyze_btn.click(
            fn=mood_mixer.analyze_mood,
            inputs=[image_input, mocking_style],
            outputs=[emotion_output, mocking_output, playlist_output]
        )
        
        reload_btn.click(
            fn=mood_mixer.reload_message,
            inputs=[mocking_style],
            outputs=[mocking_output]
        )
        
        # Footer
        gr.HTML("""
        <div style="text-align: center; margin-top: 40px; color: #888; font-style: italic;">
            Remember: This app is designed to be humorous and lighthearted. 
            If you're having a genuinely tough day, consider talking to someone who cares about you! 💙
        </div>
        <div style="text-align: center; margin-top: 20px; color: #999; font-size: 0.9em;">
            <b>Technical Note:</b> This demo uses random emotion selection. The full version would integrate DeepFace AI
            for actual facial emotion detection when TensorFlow compatibility is resolved.
        </div>
        """)
    
    return demo

if __name__ == "__main__":
    # Create and launch the interface
    demo = create_interface()
    demo.launch(
        share=True,
        server_name="0.0.0.0",
        server_port=7860,
        show_error=True
    )