import os
import random
import time
import argparse
from pydub import AudioSegment
from pydub.playback import play

# Path to sounds folder
SOUNDS_DIR = os.path.join(os.path.dirname(__file__), "sounds")

# Available sounds (map short name -> filename + description)
SOUND_MAP = {
    "chains": ("chains.mp3", "Creepy Chains"),
    "ghost": ("ghost.wav", "Ghostly Wail"),
    "spiders": ("spiders.mp3", "Crawling Spiders"),
    "axe": ("axe.wav", "Distant Axe Chop"),
    "heartbeat": ("heartbeat.mp3", "Heartbeat in the Dark"),
    "fog": ("fog.wav", "Whispering Fog"),
}

def play_sound(key: str):
    """Play a sound by its key from SOUND_MAP."""
    filename, description = SOUND_MAP[key]
    filepath = os.path.join(SOUNDS_DIR, filename)

    if not os.path.exists(filepath):
        print(f"⚠️ File not found: {filepath} (placeholder only)")
        return

    print(f"Random sound chosen: {filename}")
    print(f"🔊 Playing {description}...\n")

    sound = AudioSegment.from_file(filepath)
    play(sound)


def random_mode():
    """Play random sounds forever with random delays (5–30s)."""
    print("🎃 Horror Box Activated 🎃\n")
    try:
        while True:
            # Pick a random sound
            key = random.choice(list(SOUND_MAP.keys()))
            delay = random.randint(5, 30)

            print(f"Waiting {delay}s...")
            time.sleep(delay)
            play_sound(key)

    except KeyboardInterrupt:
        print("\n👻 Stopping Horror Box. Until next time... 🎃")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Play spooky sounds randomly or by choice.")
    parser.add_argument("--sound", choices=SOUND_MAP.keys(), help="Play a specific sound instead of random mode")
    args = parser.parse_args()

    if args.sound:
        play_sound(args.sound)
    else:
        random_mode()