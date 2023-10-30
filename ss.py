import asyncio
import requests
import aiohttp
import subprocess
import os

async def check_website_status(url):
    print(f"Checking status for {url}...")
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            print(f"Status for {url} is {response.status}")
            return response.status

def send_message_to_telegram(message, chat_id, bot_token):
    print("Sending message to Telegram...")
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    response = requests.post(url, data={'chat_id': chat_id, 'text': message})
    if response.status_code != 200:
        print(f"Failed to send message to chat ID {chat_id}: {response.status_code}")

def send_screenshot_to_telegram(file_path, chat_id, bot_token):
    if os.path.exists(file_path):
        print("Sending screenshot to Telegram...")
        url = f"https://api.telegram.org/bot{bot_token}/sendPhoto"
        with open(file_path, 'rb') as file:
            response = requests.post(url, data={'chat_id': chat_id}, files={'photo': file})
            if response.status_code == 200:
                print(f"Screenshot sent to chat ID {chat_id}")
            else:
                print(f"Failed to send screenshot to chat ID {chat_id}: {response.status_code}")

def capture_screenshot_with_cutycapt(url, save_path):
    try:
        subprocess.check_call(['xvfb-run', 'cutycapt', '--url=' + url, '--out=' + save_path])
        print(f"Screenshot saved to {save_path}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to capture screenshot: {e}")

async def main(websites, chat_id, bot_token):
    for website in websites:
        screenshot_path = f"{website.replace('https://', '').replace('/', '_')}.png"
        status = await check_website_status(website)
        if status == 200:
            capture_screenshot_with_cutycapt(website, screenshot_path)
            send_screenshot_to_telegram(screenshot_path, chat_id, bot_token)
            send_message_to_telegram(f"{website} is returning 200, all systems OK", chat_id, bot_token)
        else:
            send_message_to_telegram(f"Alert: {website} is not returning a 200 status. Current status: {status}", chat_id, bot_token)

if __name__ == '__main__':
    websites = ['https://www.example.com']  # Replace with your actual websites
    chat_id = '-100'  # Replace with your chat ID
    bot_token = '100'  # Replace with your bot token
    asyncio.run(main(websites, chat_id, bot_token))
