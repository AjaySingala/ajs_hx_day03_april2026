# Demo 3: Add Recommendations → Decision Layer.
# Concept: Now we simulate reasoning pipeline (closer to agent thinking).

# Set env vars from config.py.
import sys
import os

# Add the folder path (use absolute or relative path).
folder_path = os.path.join(os.path.dirname(__file__), '../')
sys.path.insert(0, folder_path)

import config

# Start.
import os
from openai import AzureOpenAI
from dotenv import load_dotenv

load_dotenv()

client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version="2024-02-15-preview",
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
)

deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT")

text = """
Customer complaints have increased by 25% in the last quarter.
Delivery delays and poor support response times are the main issues.
Customer churn is expected to increase if not addressed immediately.
"""

# Step 1: Summarize input.
def summarize(text):
    print("\n summarize()...")
    return client.chat.completions.create(
        model=deployment,
        messages=[
            {"role": "system", "content": "You are a business analyst."},
            {"role": "user", "content": f"Summarize:\n{text}"}
        ]
    ).choices[0].message.content

# Step 2: Extract insights.
def extract_insights(summary):
    print("\n extract_insights()...")
    return client.chat.completions.create(
        model=deployment,
        messages=[
            {"role": "system", "content": "You are a consultant."},
            {"role": "user", "content": f"Extract insights:\n{summary}"}
        ]
    ).choices[0].message.content

# Step 3: Recommend actions.
def recommend(insights):
    print("\n recommend()...")
    return client.chat.completions.create(
        model=deployment,
        messages=[
            {"role": "system", "content": "You are a strategy advisor."},
            {"role": "user", "content": f"Recommend actions based on:\n{insights}"}
        ]
    ).choices[0].message.content

summary = summarize(text)
insights = extract_insights(summary)
actions = recommend(insights)

print("\n🔹 Summary:\n", summary)
print("\n🔹 Insights:\n", insights)
print("\n🔹 Recommendations:\n", actions)
