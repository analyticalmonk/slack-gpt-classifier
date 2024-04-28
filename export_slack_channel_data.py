import requests
import csv
from datetime import datetime, timedelta

# Parameters
token = ''  # Slack OAuth token
channel_id = ''  # Slack channel ID
user_id = ''  # User ID of the sales rep
days_back = 60  # How many days back to fetch messages
csv_filename = ''  # Name of the CSV file to save messages

# Calculate the oldest timestamp
oldest = int((datetime.now() - timedelta(days=days_back)).timestamp())

def fetch_messages(token, channel_id, user_id, oldest):
    url = "https://slack.com/api/conversations.history"
    headers = {'Authorization': f'Bearer {token}'}
    params = {
        'channel': channel_id,
        'oldest': oldest
        # 'limit': 200  # Adjust based on your needs
    }

    with open(csv_filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['timestamp', 'user_id', 'text', 'image_urls'])  # Define your CSV columns

        while True:
            response = requests.get(url, headers=headers, params=params)
            if response.status_code == 200:
                data = response.json()
                if data['ok']:
                    messages = data['messages']
                    for msg in messages:
                        if msg.get('user') == user_id:
                            image_urls = [att['image_url'] for att in msg.get('attachments', []) if att.get('image_url')]
                            writer.writerow([msg['ts'], msg['user'], msg['text'], ';'.join(image_urls)])
                    if not data.get('has_more', False):
                        break
                    params['cursor'] = data['response_metadata']['next_cursor']
                else:
                    break
            else:
                raise Exception(f"Failed to fetch messages: {response.status_code}")
    print(f"Messages saved to {csv_filename}")

# Fetch and save messages
try:
    fetch_messages(token, channel_id, user_id, oldest)
except Exception as e:
    print(e)
