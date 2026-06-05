# Educational Keylogger Lab

## Overview

This project is a simple keylogger built with Python and the `pynput` library. The script captures keystrokes, adds timestamps, formats special keys for readability, and logs everything to a text file.

The purpose of this project is to demonstrate keyboard event handling, file I/O, and ethical safeguards in a controlled, local-only environment.

## Project Objective

The objective of this lab was to create a safe, educational keylogger that:

- Captures every key press
- Adds a timestamp to each keystroke
- Converts special keys (`space`, `enter`, `backspace`, etc.) into human‑readable tags
- Writes keystrokes to a log file
- Stops cleanly when the **ESC** key is pressed
- Includes a clear ethical disclaimer

## Tools Used

- Python
- `pynput` library
- Visual Studio Code
- Windows / macOS / Linux (local machine only)

## How It Works

The script uses `pynput.keyboard.Listener` to monitor global keyboard events. Every time a key is pressed, the `on_press` function is called. It gets the current time, formats the key using `format_key()`, and appends the entry to `keylog.txt`.

Special keys are converted to readable tags like `[SPACE]` or `[ENTER]` so the log is easy to understand. The `format_key()` function includes a `try/except` block to handle exotic keys (media keys, function keys) without crashing.

The listener stops when the ESC key is released, thanks to the `on_release` function returning `False`.

## Screenshots

### Keylogger Source Code

![Keylogger source code](keylogger-code.png)

*The Python script showing the import statements, `format_key()` function, and the listener setup with ethical disclaimer.*

### Running the Keylogger

![Running the keylogger](terminal-output.png)

*Terminal output after starting the script. The disclaimer is shown, and the script waits for ESC to stop.*

### Sample Log File Output

![Sample keylog output](keylog-output.png)

*A portion of `keylog.txt` showing timestamped keystrokes, spaces as `[SPACE]`, and the ENTER key as `[ENTER]` followed by a newline.*

## Example Output

When the user types `hi my name is jaden` and then presses ENTER, the log file contains:

```text
00:29:54: 'h'
00:29:54: 'i'
00:29:55: [SPACE]
00:29:55: 'm'
00:29:55: 'y'
00:29:56: [SPACE]
00:29:56: 'n'
...
00:30:06: [ENTER]
