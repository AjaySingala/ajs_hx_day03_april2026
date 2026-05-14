# Demo 5: LangGraph with Tools (@tool) + Agent Decision.
# Human-in-the-loop.

# Set env vars from config.py.
import sys
import os

# Add the folder path (use absolute or relative path).
folder_path = os.path.join(os.path.dirname(__file__), '../')
sys.path.insert(0, folder_path)

import config

# Start.
import os
from dotenv import load_dotenv

from langchain_openai import AzureChatOpenAI
from langchain_core.tools import tool
from langgraph.graph import StateGraph, END

load_dotenv()

# ===== LLM =====
llm = AzureChatOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    deployment_name=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
    api_version="2024-02-15-preview",
)

# ===== TOOLS =====
# TODO: Use the tool decorator to define the summarize tool.
___
def summarize_tool(text: str) -> str:
    """Summarizes business input"""
    print(f"\n summarize_tool()...")

    # TODO: Define a prompt that instructs the LLM to summarize the given text.
    # Specify the role clearly.
    # Pass the text input as part of the prompt.
    # Specify the output format.
    prompt = f"""
    ___
    """

    return llm.invoke(prompt).content

# TODO: Use the tool decorator to define the summarize tool.
___
def insights_tool(text: str) -> str:
    """Extracts insights"""
    print(f"\n insights_tool()...")

    # TODO: Define a prompt that instructs the LLM to extract insights.
    # Specify the role clearly.
    # Pass the text input as part of the prompt.
    # Specify the output format.
    prompt = f"""
    ___
    """

    return llm.invoke(prompt).content

@tool
def recommend_tool(text: str) -> str:
    """Recommends actions"""
    print(f"\n recommend_tool()...")

    # TODO: Define a prompt that instructs the LLM to recommend actions.
    # Specify the role clearly.
    # Pass the text input as part of the prompt.
    # Specify the output format.
    prompt = f"""
    ___
    """

    return llm.invoke(prompt).content


# ===== STATE =====
from typing import TypedDict

class AgentState(TypedDict):
    input: str
    summary: str
    insights: str
    actions: str
    approved: str 

# ===== NODES =====

def summarize_node(state: AgentState):
    print(f"\n summarize_node()...")
    # Step 1: summarize input
    # TODO: Call the summarize tool with the input text from the state.
    result = ___
    print("\n🔹 Summary:\n", result)

    # TODO: Return the summary as a key-value pair, where:
    # - The key is "summary"
    # - The value is the result from the summarize tool.
    return ___


def insights_node(state: AgentState):
    print(f"\n insights_node()...")
    # Step 2: extract insights
    # TODO: Call the insights tool with the summary from the state.
    result = ___
    print("\n🔹 Insights:\n", result)

    # TODO: Return the insights as a key-value pair, where:
    # - The key is "insights"
    # - The value is the result from the insights tool.
    return ___


def recommend_node(state: AgentState):
    print(f"\n recommend_node()...")
    # Step 3: generate recommendations
    # TODO: Call the recommend tool with the insights from the state.
    result = ___
    print("\n🔹 Recommendations:\n", result)

    # TODO: Return the actions as a key-value pair, where:
    # - The key is "actions"
    # - The value is the result from the recommend tool.
    return ___


def human_approval_node(state: AgentState):
    print(f"\n human_approval_node()...")
    # Human-in-the-loop decision point
    print("\n🤖 Proposed Actions:\n", state["actions"])

    # TODO: Simulate a human decision.
    # Ask the user if they approve the proposed actions.
    decision = ___

    return {"approved": decision}


# ===== ROUTER =====

def approval_router(state: AgentState):
    print(f"\n approval_router()...")
    # If approved → END
    if state["approved"] == "yes":
        print(f"\n THE END!...")
        return "end"
    # If not approved → restart from summarize
    return "retry"


# ===== BUILD GRAPH =====

graph = StateGraph(AgentState)

# TODO: Add nodes to the graph for these nodes:
# - summarize node
# - insights node
# - recommend node
# - human approval node
___

# Define linear flow
# TODO: Set the summarize node as the entry point of the graph.
___

# TODO: Add edges to define the flow between the nodes.
# summarize -> insights -> recommend -> human approval.
___

# Add human decision loop
graph.add_conditional_edges(
    "human",
    approval_router,
    {
        "retry": "summarize",  # loop again
        "end": END             # exit
    }
)

# Compile graph
app = graph.compile()


# ===== RUN =====

input_data = {
    "input": """
    Customer complaints increased by 25%.
    Delivery delays and poor support are major issues.
    Customer churn risk is rising significantly.
    """
}

app.invoke(input_data)
