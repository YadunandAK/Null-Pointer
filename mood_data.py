# Mood mappings and data for The Unhelpful Mood Mixer

# Map emotions to their opposites
EMOTION_OPPOSITES = {
    "happy": "sad",
    "sad": "happy", 
    "angry": "calm",
    "fear": "confident",
    "surprise": "bored",
    "disgust": "satisfied",
    "neutral": "excited"
}

# Mocking messages by style and emotion
MOCKING_MESSAGES = {
    "polite": {
        "happy": [
            "Oh wonderful, another person radiating joy. How... refreshing. 🙄",
            "Your happiness is truly inspiring. I'm sure everyone around you is thrilled. 😊",
            "What a delightfully cheerful disposition you have today. Bless your heart. 💫"
        ],
        "sad": [
            "My sincere condolences for whatever tragedy has befallen your day. 🎭",
            "I do hope this melancholy phase passes swiftly for you, dear soul. 💙", 
            "Your sorrowful expression is quite... artistic, really. 🎨"
        ],
        "angry": [
            "What a passionate display of emotions you're showing today. 🔥",
            "I can see you're having quite the spirited moment. How invigorating. ⚡",
            "Your intensity is truly remarkable. I'm sure it's very productive. 💪"
        ],
        "fear": [
            "Your cautious nature is quite endearing, really. 🦌",
            "Such a thoughtful, vigilant expression. Safety first, as they say. 🛡️",
            "Your concern for potential dangers is... commendable. 👀"
        ],
        "surprise": [
            "Oh my, what an unexpectedly animated expression! 🎪",
            "Your astonishment is quite... pronounced, isn't it? 😲",
            "Such delightful bewilderment you're displaying today. 🎭"
        ],
        "disgust": [
            "Your refined sensibilities are clearly offended by something. 🧐",
            "What an exquisite look of distaste you're wearing. 👑",
            "Your discerning nature is truly showing today. 💎"
        ],
        "neutral": [
            "How wonderfully... unreadable you are today. 😐",
            "Your poker face is absolutely magnificent, dear. 🃏",
            "Such masterful emotional restraint you're displaying. 🗿"
        ]
    },
    "sassy": {
        "happy": [
            "Okay, we get it. You're happy. No need to blind us with that smile. ✨",
            "Someone clearly had their coffee today. Tone it down a notch! ☕",
            "Your joy is so bright, I might need sunglasses. 😎"
        ],
        "sad": [
            "Well, aren't you just a ray of sunshine today? 🌧️",
            "Did someone cancel your favorite TV show or something? 📺",
            "That face could make a funeral director jealous. ⚰️"
        ],
        "angry": [
            "Whoa there, tiger! Save some rage for tomorrow. 🐅",
            "Someone woke up and chose violence today, huh? 💥",
            "Is that your angry face or did you smell something funky? 👃"
        ],
        "fear": [
            "Did you just see a spider or is that your everyday expression? 🕷️",
            "Relax! It's just a photo, not a job interview. 📸",
            "You look like you've seen a ghost... or your credit card bill. 👻"
        ],
        "surprise": [
            "Plot twist! Your face has emotions! Who knew? 🎬",
            "Did someone just tell you about taxes? 💸",
            "That's the look of someone who just realized it's Monday. 📅"
        ],
        "disgust": [
            "Did you just smell someone's lunch from last week? 🥪",
            "That's the face of someone who just opened a dating app. 💔",
            "You look like you just tasted decaf coffee. ☕"
        ],
        "neutral": [
            "Wow, such emotion! I'm practically crying over here. 😴",
            "Are you a robot or just really good at hiding feelings? 🤖",
            "That's the most enthusiastic neutral face I've ever seen. 📱"
        ]
    },
    "roastmaster": {
        "happy": [
            "Your happiness is so intense, I'm worried you might pull a muscle. Stretch first! 🤸",
            "Congratulations! You've achieved maximum human joy. Please leave some for the rest of us. 🏆",
            "That smile could power a small village. Have you considered renewable energy? ⚡"
        ],
        "sad": [
            "You look like a sad emoji that came to life and regretted it immediately. 😢",
            "That expression screams 'I just remembered I have responsibilities.' 📋",
            "You're giving off strong 'Monday morning meeting' vibes. 📊"
        ],
        "angry": [
            "Calm down there, Hulk. The camera isn't your enemy... probably. 📸",
            "You look angry enough to write a strongly worded Yelp review. ⭐",
            "That face could scare a GPS into giving better directions. 🗺️"
        ],
        "fear": [
            "You look like you just realized you left the oven on... three states away. 🔥",
            "That's the face of someone who just got a text saying 'we need to talk.' 💬",
            "You appear to be experiencing an existential crisis. Welcome to adulthood! 🎓"
        ],
        "surprise": [
            "You look more shocked than someone who just found out pineapple belongs on pizza. 🍕",
            "That's the expression of someone who just discovered their age in dog years. 🐕",
            "You seem surprised... did you forget you had a face? 🤔"
        ],
        "disgust": [
            "You look like you just witnessed someone put ketchup on a steak. 🥩",
            "That's the face of someone who just realized they've been pronouncing 'gif' wrong. 💻",
            "You appear disgusted... did you just see your browser history? 📂"
        ],
        "neutral": [
            "Your emotional range is truly impressive... said no one ever. 😑",
            "You've mastered the art of looking like a default avatar. Congratulations! 👤",
            "That's the most expressive expressionless face I've seen today. 🎭"
        ]
    }
}

# YouTube playlists organized by mood (for opposite mood recommendations)
YOUTUBE_PLAYLISTS = {
    "happy": {
        "title": "Upbeat Energy Boosters",
        "url": "https://www.youtube.com/playlist?list=PLrAl6w4vEIJhJ2nPUG7dI8Qo0RO_3p4x8",
        "description": "High-energy songs to lift your spirits"
    },
    "sad": {
        "title": "Melancholy Mood Music", 
        "url": "https://www.youtube.com/playlist?list=PLrAl6w4vEIJhJ2nPUG7dI8Qo0RO_3p4x9",
        "description": "Somber tunes for contemplative moments"
    },
    "calm": {
        "title": "Peaceful Relaxation Sounds",
        "url": "https://www.youtube.com/playlist?list=PLrAl6w4vEIJhJ2nPUG7dI8Qo0RO_3p4x1",
        "description": "Soothing sounds for tranquility"
    },
    "confident": {
        "title": "Boss Mode Anthems",
        "url": "https://www.youtube.com/playlist?list=PLrAl6w4vEIJhJ2nPUG7dI8Qo0RO_3p4x2", 
        "description": "Empowering tracks to boost confidence"
    },
    "bored": {
        "title": "Monotone Minimalism",
        "url": "https://www.youtube.com/playlist?list=PLrAl6w4vEIJhJ2nPUG7dI8Qo0RO_3p4x3",
        "description": "Understated background music"
    },
    "satisfied": {
        "title": "Content & Cozy Vibes",
        "url": "https://www.youtube.com/playlist?list=PLrAl6w4vEIJhJ2nPUG7dI8Qo0RO_3p4x4",
        "description": "Comfortable tunes for satisfaction"
    },
    "excited": {
        "title": "Hype Train Express",
        "url": "https://www.youtube.com/playlist?list=PLrAl6w4vEIJhJ2nPUG7dI8Qo0RO_3p4x5",
        "description": "Explosive energy for maximum excitement"
    }
}

# Emojis for each emotion
EMOTION_EMOJIS = {
    "happy": "😊",
    "sad": "😢", 
    "angry": "😠",
    "fear": "😨",
    "surprise": "😲",
    "disgust": "🤢",
    "neutral": "😐"
}