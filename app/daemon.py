import os
import subprocess
import sys
from queue import SimpleQueue

import pyperclip
import simpleaudio as sa
from pynput import keyboard

from logger import Logger


logger = Logger("Daemon", stream=True).get() # TODO: Remove 'stream=True' for releases.

"""Sound & Notifies"""
def play_notify(sound_path):
    """Cross-platform Sound"""
    if sys.platform.startswith("linux"):
        try:
            subprocess.run(
                ["paplay", sound_path],
                check=False
            )
        except Exception as e:
            logger.warning(f"Error playing paplay sound: {e}")
    try:
        wave_obj = sa.WaveObject.from_wave_file(sound_path)
        wave_obj.play()
    except Exception as e:
        logger.warning(f"Error playing simpleaudio sound: {e}")


def notify_linux(text: str):
    """Extra popup notification for linux."""
    try:
        subprocess.run(
            ["notify-send", "PropClip Says!", text[:80]],
            check=False
        )
    except Exception as e:
        logger.warning(f"Error sending notification: {e}")


"""Hotkey, Clipboard & Compatibility"""
HOTKEY = "<ctrl>+<alt>+v" # TODO: Add global option in config!
NOTIFY_SOUND = "src/assets/whistleronic.wav"
latest_clip = [None]  # Mutable without global


def is_compatible() -> bool:
    if sys.platform.startswith("linux"):
        logger.debug("Linux Detected.")
        x11 = "DISPLAY" in os.environ
        if x11:
            logger.debug("DISPLAY X11 Detected.")
        return x11
    elif sys.platform.startswith("win32"):
        logger.debug("Windows Detected.")
        return True
    elif sys.platform.startswith("darwin"):
        logger.debug("MacOS Detected.")
        logger.warning("Program not tested on MacOS.")
        return True  # MacOS
    return False  # Something else


def on_activate(queue, callback=None):
    text = pyperclip.paste()
    if latest_clip[0] == text:
        logger.warning("Skipping repeated paste")
        notify_linux("❌ -> Prop already in queue!")
        print("Prop already added!")
        return
    latest_clip[0] = text
    play_notify(NOTIFY_SOUND)
    notify_linux("✅ -> Prop added!")
    print("Prop added!")
    logger.info(f"Clipboard content below:\n\"\"\"\n{text}\n\"\"\" <-")
    
    queue.put(text)
    if callback:
        callback(text)


def main():
    if not is_compatible():
        logger.warning("Your system may have incompatibility problems.")

    queue = SimpleQueue()

    def test_callback(text: str):
        logger.info(f"Callback received text: length({len(text)})")

    logger.debug("Initializing listener.")

    try:
        with keyboard.GlobalHotKeys({
            HOTKEY: lambda: on_activate(queue, test_callback)
        }) as listener:
            play_notify(NOTIFY_SOUND)
            notify_linux("✅ -> Daemon Listening!!")
            listener.join()
    except KeyboardInterrupt:
        logger.info("Daemon stopped by user (CTRL+C).")


if __name__ == "__main__":
    main()
