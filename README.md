# Offline Translate

This project provides offline language translation capabilities using the Argos Translate library. It allows users to translate text from one language to another without an internet connection.

## Key Features

*   **Offline Translation:** Translate text without requiring an internet connection.
*   **Language Detection:** Automatically detects the source language of the input text.
*   **Simple Interface:** Easy-to-use command-line interface for quick translations.
*   **Customizable:** Supports different language pairs by modifying the installation script.

## Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/versaagonon/offline-translate.git
    cd offline-translate
    ```

2.  **Install dependencies:**

    ```bash
    pip install argostranslate langdetect
    ```

3.  **Install the desired language model:**

    *   Run the `install.py` script.  By default, it installs the Indonesian to English (`id` to `en`) translation model.

        ```bash
        python install.py
        ```

    *   **Important:** To install a different language pair, modify the `install.py` script before running it.  Change the `from_code` and `to_code` values to the desired language codes.  For example, to install the Spanish to English model, change `"id"` to `"es"`.  You can find available language codes in the Argos Translate documentation.

## Usage

1.  **Run the `translate.py` script:**

    ```bash
    python translate.py
    ```

2.  **Enter the text you want to translate:** The script will automatically detect the source language and translate it to English (by default).

3.  **To exit the script, type `exit` and press Enter.**

### Example

```
Input (input 'exit' to exit): Halo dunia
Detected: id | Output: Hello World
Input (input 'exit' to exit): exit
```

## Tech Stack and Dependencies

*   **Python:** The project is written in Python.
*   **Argos Translate:**  The core library for offline translation.
*   **langdetect:**  A library for language detection.

## Suggestions for Improvements

1.  **Add support for specifying the target language:** Currently, the script only translates to English.  Allowing the user to specify the target language via a command-line argument would greatly increase its flexibility.

2.  **Implement error handling:** The script lacks proper error handling.  For example, it should handle cases where the language model for the detected source language is not installed or when the input text is empty.

3.  **Provide a more user-friendly interface:**  Consider creating a graphical user interface (GUI) or a web interface for easier interaction.  Alternatively, command-line arguments could be used to control the script's behavior without modifying the source code.
