# Demo 1: Basic Task → Summarization (Single-step AI).
# Concept: This is NOT an agent. Just a task.

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

# Initialize Azure OpenAI client.
client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version="2024-02-15-preview",
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
)

deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT")

# Sample business input (simulate SME data).
text = """
Customer complaints have increased by 25% in the last quarter.
Delivery delays and poor support response times are the main issues.
Customer churn is expected to increase if not addressed immediately.
"""

# Simple LLM call for summarization.
response = client.chat.completions.create(
    model=deployment,
    messages=[
        {"role": "system", "content": "You are a business analyst."},
        {"role": "user", "content": f"Summarize the following:\n{text}"}
    ]
)

print("\n🔹 Summary:\n", response.choices[0].message.content)
