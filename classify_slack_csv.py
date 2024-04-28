import os
import csv
from openai import OpenAI

# Load OpenAI
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY', 'Specified environment variable is not set')

client = OpenAI(api_key=OPENAI_API_KEY)

# Define the messages to send to GPT-4
sales_intent_classifiction_prompt = """
Provided below is a Slack message from a sales team member from our company. 
If the below text message is about a customer making a purchase decision about a product, providing reason for a sales decision, or dropping from sales discussion, respond with "TRUE", otherwise respond with "FALSE". 
Don't get confused between general feedback and sales intent.

SLACK MESSAGE:
"""

base_message_list = [
    {"role": "system", "content": "You are an accurate and precise sales assistant who specializes in understanding sales-specific intent from text."}
]

# Input and output file names
input_csv = 'slack_messages_userfeedback.csv'
output_csv = 'slack_messages_userfeedback_with_intent.csv'

def analyze_text_with_gpt4(text):
    chatgpt_message_list = base_message_list.copy()
    chatgpt_message_list.append(
        {"role": "user", "content": sales_intent_classifiction_prompt + text}
    )

    chat_response = client.chat.completions.create(
        model="gpt-4-turbo",
        # prompt=send_prompt,
        messages=chatgpt_message_list,
        temperature=0,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        
    )
    return chat_response.choices[0].message.content.strip()

# Read the existing CSV and append a new column with GPT-4 responses
with open(input_csv, mode='r', newline='', encoding='utf-8') as infile, \
     open(output_csv, mode='w', newline='', encoding='utf-8') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    
    # Read the header and append a new column name
    headers = next(reader)
    headers.append('GPT-4 Output')
    writer.writerow(headers)
    
    # Process each row
    for row in reader:
        text = row[2]  # Assuming the text is in the third column
        gpt_output = analyze_text_with_gpt4(text)
        row.append(gpt_output)
        writer.writerow(row)

print("Processing complete. Output saved to", output_csv)
