
# Website Screenshot and Status Checker

This script checks the status of specified websites and takes a screenshot if the status is 200 (OK). It then sends a notification and the screenshot to a specified Telegram chat.

## Prerequisites

1. **Python 3.10** - The script is written in Python.
2. **Required Libraries** - Install the necessary Python libraries using:
    ```bash
    pip install aiohttp requests
    ```
3. **cutycapt** - A tool to capture screenshots.
    ```bash
    sudo apt-get update
    sudo apt-get install cutycapt
    ```
4. **xvfb** - X Virtual FrameBuffer, used for taking screenshots in headless mode.
    ```bash
    sudo apt-get install xvfb
    ```

## Setup

1. **Telegram Bot**:
    - Start a chat with the [BotFather](https://telegram.me/botfather) on Telegram.
    - Create a new bot.
    - Save the bot token provided by BotFather.
    - Start a chat with your new bot.
    - Add the bot to the Telegram group or channel where you want notifications.

2. **Get Chat ID**:
    - Forward a message from your group or channel to [Json Dump Bot](https://telegram.me/jsondumpbot).
    - Note down the chat ID.

3. **Script Configuration**:
    - Open `ss.py`.
    - Replace the `websites` list with the URLs you want to monitor.
    - Replace `chat_id` and `bot_token` with your Telegram chat ID and bot token.

## Running the Script

Execute the script manually:
```bash
python3 ss.py
```

## Automating with Cron

To run this script every day at a specified time (e.g., 8 am CST), set up a cron job:

1. Open crontab:
    ```bash
    crontab -e
    ```

2. Add the following line to run the script at 8 am CST daily:
    ```bash
    0 8 * * * /usr/bin/python3 /path/to/ss.py >> /path/to/ss.log 2>&1
    ```

## License

MIT

## Contributors

- Fabian Anguiano

