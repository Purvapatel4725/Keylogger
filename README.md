# Keylogger Script

## Overview

Welcome to the **Keylogger** repository! This project contains two Python scripts designed for capturing keystrokes. These scripts are intended for educational and ethical use only. Please ensure you have the proper authorization before running these scripts.

## Repository Structure

This repository contains the following files:

- `basic_keylogger.py`
- `advanced_keylogger.py`
- `requirements.txt`

## How to Clone the Repository

To get started with this repository, clone it using the following command:

```bash
git clone https://github.com/Purvapatel4725/Keylogger.git
```

## Installation Requirements

Before running the scripts, make sure to install the necessary dependencies. You can do this by creating a virtual environment and installing the requirements listed in `requirements.txt`.

### Install Dependencies

1. **Create a Virtual Environment (Optional but recommended):**

    ```bash
    python -m venv venv
    ```

2. **Activate the Virtual Environment:**

    - On Windows:

      ```bash
      venv\Scripts\activate
      ```

    - On macOS/Linux:

      ```bash
      source venv/bin/activate
      ```

3. **Install Required Packages:**

    ```bash
    pip install -r requirements.txt
    ```

## Scripts Overview

### `basic_keylogger.py`

This script captures keystrokes and logs them to a local file named `keys.txt`. It uses the `pynput` library to listen to keyboard events and log each key press.

### `advanced_keylogger.py`

The advanced keylogger script is more feature-rich. It captures keystrokes and performs the following:

- Sends the captured keystrokes to a specified IP address and port.
- Writes the captured keystrokes to a local file named `keystrokes.txt`.
- Periodically sends the data to the server at intervals defined by `time_interval`.

## Ethical and Educational Use Warning

**WARNING:** This repository is intended for educational purposes only. Unauthorized use of these keylogging scripts can be illegal and unethical. Use these scripts responsibly and only on systems for which you have explicit permission. The author, `Purva Patel`, is not responsible for any misuse or illegal activities performed with these scripts.

## Author

This repository is maintained by `Purva Patel`.

