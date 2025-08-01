#!/bin/bash

echo "🎭 Starting The Unhelpful Mood Mixer Demo..."
echo "=============================================="

# Check if virtual environment exists
if [ ! -d "mood_mixer_env" ]; then
    echo "Creating virtual environment..."
    python3 -m venv mood_mixer_env
fi

# Activate virtual environment
echo "Activating virtual environment..."
source mood_mixer_env/bin/activate

# Install dependencies if not already installed
echo "Checking dependencies..."
pip install gradio opencv-python Pillow numpy -q

# Start the application
echo "Launching The Unhelpful Mood Mixer Demo!"
echo "========================================="
echo "🌐 The app will open in your browser shortly..."
echo "📱 You can also visit: http://localhost:7860"
echo "🛑 Press Ctrl+C to stop the application"
echo ""

python simple_app.py