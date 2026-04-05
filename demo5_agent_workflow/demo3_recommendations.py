# Demo 3: Add Recommendations → Decision Layer.
# Concept: Now we simulate reasoning pipeline (closer to agent thinking).

# Set env vars from config.py.
import sys
import os

# Add the folder path (use absolute or relative path).
folder_path = os.path.join(os.path.dirname(__file__), '../..')
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

# TODO: Define a text input for a customer feedback report.
text = """
___
"""

# TODO: Simulate a reasoning pipeline with 3 steps:
# 1. Summarize the input text.
# 2. Extract key insights.
# 3. Recommend actions based on insights.
# For each step, define a separate method that will:
# - Take the output of the previous step as input.
# - Call the LLM to perform the task.
#   - The LLM client object's model and messages parameters should be set.
#   - Define 2 messages for "system" and" user".
#   - The "system" message should set the role
#   - The "user" message should include the text input and instructions for
#     the task to summarize, extract insights or recommend actions.
# - Each method should return the LLM response content.

# Step 1: Summarize input.
def summarize(text):
    print("\n summarize()...")
    
    response = ___
    
    return ___ 


# Step 2: Extract insights.
def extract_insights(summary):
    print("\n extract_insights()...")

    response = ___
    
    return ___ 


# Step 3: Recommend actions.
def recommend(insights):
    print("\n recommend()...")
    response = ___
    
    return ___ 


# TODO: Call the methods in sequence to simulate the reasoning pipeline.
# Pass the output of each step as input to the next step.
# Pass the "text" variable as input to the first step.
summary = ___
insights = ___
actions = ___

# TODO: Print the output of each step.
___
