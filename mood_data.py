# Mood mappings and data for The Unhelpful Mood Mixer

# Map emotions to their opposites
EMOTION_OPPOSITES = {
    "happy": "sad",
    "sad": "happy", 
    "angry": "calm",
    "calm": "angry",
    "fear": "confident",
    "confident": "fear", 
    "surprise": "bored",
    "bored": "surprise",
    "disgust": "satisfied",
    "satisfied": "disgust",
    "neutral": "excited",
    "excited": "neutral"
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
        ],
        "calm": [
            "Your serene demeanor is quite... admirable, really. 🧘",
            "Such peaceful tranquility you're radiating today. 🌊",
            "Your zen-like composure is truly inspiring. ✨"
        ],
        "confident": [
            "Your self-assured presence is quite... noticeable. 💫",
            "Such bold confidence you're displaying today. 👑",
            "Your unwavering certainty is most impressive. 🌟"
        ],
        "bored": [
            "Your lack of enthusiasm is quite... apparent. 😴",
            "Such delightful disinterest you're showing. 📱",
            "Your apathy is truly remarkable today. 🥱"
        ],
        "satisfied": [
            "Your contentment is quite... evident. 😌",
            "Such pleased satisfaction you're radiating. ☺️",
            "Your fulfillment is most apparent. 🌈"
        ],
        "excited": [
            "Your enthusiasm is quite... energetic. ⚡",
            "Such animated excitement you're displaying. 🎉",
            "Your exuberance is truly vibrant today. 🎊"
        ],
        "content": [
            "Your comfortable satisfaction is quite... cozy. 🏠",
            "Such pleasant contentment you're showing. ☕",
            "Your peaceful happiness is most charming. 🌻"
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
        ],
        "calm": [
            "Zen master over here! Save some peace for the rest of us. 🧘",
            "You're so chill, I'm worried you might fall asleep standing up. 😴",
            "That's the face of someone who just discovered meditation apps. 📱"
        ],
        "confident": [
            "Somebody's feeling themselves today! Tone it down a notch. 😎",
            "That confidence could probably be seen from space. 🚀",
            "You look like you just discovered self-help books. 📚"
        ],
        "bored": [
            "Exciting! You look like you're watching paint dry. 🎨",
            "That's the face of someone scrolling social media for the 47th time today. 📱",
            "You're giving off strong 'mandatory meeting' energy. 💼"
        ],
        "satisfied": [
            "Someone's pleased with themselves! How nice for you. 😌",
            "That's the look of someone who just finished their to-do list. ✅",
            "You seem satisfied... did you finally find the TV remote? 📺"
        ],
        "excited": [
            "Whoa there, energizer bunny! Save some enthusiasm for tomorrow. 🔋",
            "That excitement level is illegal in some countries. 🚨",
            "You look like you just discovered caffeine exists. ☕"
        ],
        "content": [
            "Living your best life, I see. How inspirational. 🌈",
            "That's the face of someone who just found their favorite snack on sale. 🍿",
            "You look comfy... maybe too comfy. 🛋️"
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
        ],
        "calm": [
            "You're so zen, I'm worried you might transcend into another dimension. 🌌",
            "That level of calmness could put a meditation guru to shame. 🧘‍♀️",
            "You look like you just achieved inner peace... or gave up on life entirely. 🕯️"
        ],
        "confident": [
            "Your confidence is so bright, NASA might mistake it for a new star. ⭐",
            "That self-assurance could power a small city. Have you considered renewable ego? 🔋",
            "You're radiating so much confidence, I need sunglasses just to look at you. 🕶️"
        ],
        "bored": [
            "You look more bored than someone watching grass grow in slow motion. 🌱",
            "That expression screams 'I've seen every Netflix show twice.' 📺",
            "You appear to have reached peak boredom. Scientists should study you. 🔬"
        ],
        "satisfied": [
            "You look like a cat who just knocked everything off a table. 🐱",
            "That satisfaction is so smug, it should come with a warning label. ⚠️",
            "You seem pleased with yourself... did you finally adult correctly? 🎓"
        ],
        "excited": [
            "Your excitement could probably be measured on the Richter scale. 📊",
            "That energy level is so high, you're basically human espresso. ☕",
            "You look like you just discovered the meaning of life... or found $20. 💰"
        ],
        "content": [
            "You're so content, you could be a stock photo for 'happiness.' 📸",
            "That peaceful expression suggests you've either found enlightenment or good WiFi. 📶",
            "You look like you just solved all your life problems... or ordered pizza. 🍕"
        ]
    }
}

# YouTube playlists organized by mood (for opposite mood recommendations)
YOUTUBE_PLAYLISTS = {
    "happy": {
        "title": "Sad Songs to Balance Your Joy",
        "url": "https://www.youtube.com/playlist?list=PLhInz4M-OzRFvT5Jzm8fV-pZBzKpyfGoN",
        "description": "Melancholy hits to bring you back down to earth"
    },
    "sad": {
        "title": "Happy Pop Hits",
        "url": "https://www.youtube.com/playlist?list=PLMC9KNkIncKtsacKpgMb0CVqNcC5aNquZ",
        "description": "Upbeat bangers to lift your spirits"
    },
    "calm": {
        "title": "Rage Rock & Metal",
        "url": "https://www.youtube.com/playlist?list=PLFgquLnL59alCl_2TQvOiD5Vgm1hCaGSI",
        "description": "Aggressive anthems to wake up your inner beast"
    },
    "confident": {
        "title": "Awkward Slow Jams",
        "url": "https://www.youtube.com/playlist?list=PLDcnymzs18LU4Kexrs91TVdfnplU3I5zs",
        "description": "Uncomfortable ballads to humble your confidence"
    },
    "bored": {
        "title": "Crazy Energetic Hits",
        "url": "https://www.youtube.com/playlist?list=PLMC9KNkIncKtPzgY-5rmhvj7fax8fdxoj",
        "description": "High-octane tracks to shock you awake"
    },
    "satisfied": {
        "title": "Soft Love Songs",
        "url": "https://www.youtube.com/playlist?list=PLDcnymzs18LVXfO_x0Ei0R24qDbVtyy66",
        "description": "Gentle romantic tunes for contentment"
    },
    "excited": {
        "title": "Slow Ambient Chill",
        "url": "https://www.youtube.com/playlist?list=PL6CkCZH2y3b9y60AfsK5TJepowSIzVoF_",
        "description": "Peaceful soundscapes to calm your energy"
    },
    "angry": {
        "title": "Calm Chillhop Beats",
        "url": "https://www.youtube.com/playlist?list=PLbpi6ZahtOH7WpVEeSgCEStx9a3aIbKCd",
        "description": "Smooth lo-fi beats to cool your anger"
    },
    "fear": {
        "title": "Confident Pop Anthems",
        "url": "https://www.youtube.com/playlist?list=PLzAUj6cOd3wB5-xQONtXwn_sksRrpy5Rj",
        "description": "Bold tracks to boost your courage"
    },
    "content": {
        "title": "Cringe Bangers",
        "url": "https://www.youtube.com/playlist?list=PLQog_FHUHAFUckxL7F9AgzRdxP-VZMCjY",
        "description": "Hilariously awkward hits to shake up your contentment"
    }
}

# Emojis for each emotion
EMOTION_EMOJIS = {
    "happy": "😊",
    "sad": "😢", 
    "angry": "😠",
    "calm": "😌",
    "fear": "😨",
    "confident": "😎",
    "surprise": "😲",
    "bored": "😴",
    "disgust": "🤢",
    "satisfied": "😌",
    "neutral": "😐",
    "excited": "🤩",
    "content": "😊"
}