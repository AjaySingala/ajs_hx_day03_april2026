# Demo 4: Agent Workflow (Planner–Executor Pattern).
# Concept:Now this becomes an agent: it decides what steps to run.

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

# ===== TOOL FUNCTIONS (Agent capabilities) =====

def summarize(text):
    print("\n summarize()...")
    # Tool 1: Summarization
    return client.chat.completions.create(
        model=deployment,
        messages=[
            {"role": "system", "content": "Summarize business input."},
            {"role": "user", "content": text}
        ]
    ).choices[0].message.content


def extract_insights(summary):
    print("\n extract_insights()...")
    # Tool 2: Insight extraction
    return client.chat.completions.create(
        model=deployment,
        messages=[
            {"role": "system", "content": "Extract key insights."},
            {"role": "user", "content": summary}
        ]
    ).choices[0].message.content


def recommend(insights):
    print("\n recommend()...")
    # Tool 3: Action recommendation
    return client.chat.completions.create(
        model=deployment,
        messages=[
            {"role": "system", "content": "Recommend business actions."},
            {"role": "user", "content": insights}
        ]
    ).choices[0].message.content


# ===== PLANNER (decides steps dynamically) =====

def planner(user_input):
    print("\n planner()...")
    # Planner decides workflow steps
    plan = ["summarize", "extract_insights", "recommend"]
    return plan


# ===== EXECUTOR (runs steps one-by-one) =====

def executor(plan, input_text):
    print("\n exectutor()...")
    context = input_text

    for step in plan:
        # Dynamically execute steps like an agent
        if step == "summarize":
            context = summarize(context)
            print("\n🔹 After Summarize:\n", context)

        elif step == "extract_insights":
            context = extract_insights(context)
            print("\n🔹 After Insights:\n", context)

        elif step == "recommend":
            context = recommend(context)
            print("\n🔹 Final Recommendations:\n", context)

    return context


# ===== RUN AGENT =====

user_input = """
Customer complaints have increased by 25%.
Delivery delays and slow support are key issues.
Churn risk is rising.
"""

plan = planner(user_input)
executor(plan, user_input)
