# Slack Message Intent Classification

This repository contains Python scripts to extract messages from a specific Slack channel and user, and then classify those messages based on their intent using the OpenAI GPT-4 API.

## Overview

The project consists of two main scripts:

1. `export_slack_channel_data.py`: This script fetches messages from a specific Slack channel and user, and exports them to a CSV file.
2. `classify_slack_csv.py`: This script reads the exported CSV file, sends each message to the OpenAI GPT-4 API for intent classification, and appends the API response to a new CSV file.

## Use Case and Prompt Customization

The current implementation of the `classify_slack_csv.py` script is designed to classify Slack messages based on their sales intent. The script uses a predefined prompt to send messages to the OpenAI GPT-4 API for classification. The API response indicates whether the message is related to a customer's purchase decision, a sales decision, or a dropout from a sales discussion.

However, this use case is just one example, and the script can be easily adapted to classify messages based on different intents or purposes by modifying the prompt.

To customize the prompt, open the `classify_slack_csv.py` script and locate the following line:

```
sales_intent_classifiction_prompt = """
Provided below is a Slack message from a sales team member from our company. 
If the below text message is about a customer making a purchase decision about a product, providing reason for a sales decision, or dropping from sales discussion, respond with "TRUE", otherwise respond with "FALSE". 
Don't get confused between general feedback and sales intent.

SLACK MESSAGE:
"""
```

Here's how you can modify the prompt to classify customer support queries:

```
sales_intent_classification_prompt = """
Provided below is a Slack message from a team member. 
If the below text message is about a customer asking for support or reporting an issue, respond with "TRUE", otherwise respond with "FALSE". 
Ensure to distinguish between general inquiries and specific support requests.

SLACK MESSAGE:
"""
```

## Prerequisites

Before running the scripts, you'll need to have the following:

- Python 3.6 or later installed
- A Slack workspace and the necessary permissions to export data
- An OpenAI API key

## Installation

1. Clone the repository:

`git clone https://github.com/your-username/slack-message-intent-classification.git`

2. Install the required Python packages:

`pip install -r requirements.txt`

3. Set up the necessary environment variables:

export OPENAI_API_KEY='your_openai_api_key'

Replace `'your_openai_api_key'` with your OpenAI API key.

## Usage

1. Run the `export_slack_channel_data.py` script to export messages from a specific Slack channel and user to a CSV file:

2. Run the `python classify_slack_csv.py` script to read the previously exported CSV file, send each message to the GPT-4 API for intent classification, and append the API response to a new CSV file.

*Note: Make sure to replace the required variables in both files before executing them.*

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](https://opensource.org/license/mit).