"""
BAHO Coffee Strategy Agent - Consumer Agent
This agent uses the Coffee Trends Agent via A2A to provide strategic insights
specifically tailored for BAHO COFFEE COMPANY, a Rwandan specialty coffee producer.
"""

import os
from google.adk.agents import LlmAgent
from google.adk.agents.remote_a2a_agent import (
    RemoteA2aAgent,
    AGENT_CARD_WELL_KNOWN_PATH,
)
from google.adk.models.google_llm import Gemini
from google.genai import types


# Configure retry options
retry_config = types.HttpRetryOptions(
    attempts=5,
    exp_base=7,
    initial_delay=1,
    http_status_codes=[429, 500, 503, 504],
)


# Create a RemoteA2aAgent that connects to the Coffee Trends Agent
remote_coffee_trends_agent = RemoteA2aAgent(
    name="coffee_trends_agent",
    description="Remote coffee trends and market intelligence agent that provides "
                "global coffee trends, Rwandan coffee information, and strategic insights.",
    # Point to the agent card URL
    agent_card=f"http://localhost:8001{AGENT_CARD_WELL_KNOWN_PATH}",
)

print("✅ Remote Coffee Trends Agent proxy created!")
print(f"   Connected to: http://localhost:8001")
print(f"   Agent card: http://localhost:8001{AGENT_CARD_WELL_KNOWN_PATH}")


# Create the BAHO Coffee Strategy Agent
baho_strategy_agent = LlmAgent(
    model=Gemini(model="gemini-2.5-flash-lite", retry_options=retry_config),
    name="baho_strategy_agent",
    description="Strategic advisor for BAHO COFFEE COMPANY, a Rwandan specialty coffee producer. "
                "Provides market insights, competitive positioning, and growth strategies based on "
                "global coffee trends and Rwandan coffee characteristics.",
    instruction="""
    You are a strategic advisor for BAHO COFFEE COMPANY, a premium Rwandan specialty coffee producer.
    
    Your role is to help BAHO make informed business decisions by:
    1. Analyzing global coffee market trends
    2. Understanding Rwandan coffee's unique position in the specialty market
    3. Providing actionable strategic recommendations
    4. Identifying opportunities for growth and differentiation
    
    When asked questions:
    - Always consult the coffee_trends_agent sub-agent for current market intelligence
    - Focus on actionable insights specific to BAHO's position as a Rwandan specialty producer
    - Consider BAHO's strengths: unique terroir, quality, sustainability, direct trade
    - Provide strategic recommendations that are practical and implementable
    - Think about pricing, positioning, distribution channels, and marketing
    
    Key areas to address:
    - Market trends and opportunities
    - Competitive positioning
    - Pricing strategies
    - Distribution channels (D2C, wholesale, subscriptions)
    - Marketing and brand positioning
    - Product development (processing methods, roast profiles)
    - Sustainability and direct trade narratives
    
    Always be strategic, data-driven, and focused on BAHO's success as a Rwandan specialty coffee producer.
    Be enthusiastic about Rwanda's unique coffee story and BAHO's potential in the global market.
    """,
    sub_agents=[remote_coffee_trends_agent],  # Use the remote agent via A2A!
)

print("\n✅ BAHO Strategy Agent created!")
print("   Model: gemini-2.5-flash-lite")
print("   Sub-agents: 1 (remote Coffee Trends Agent via A2A)")
print("   Ready to provide strategic insights for BAHO COFFEE COMPANY!")

