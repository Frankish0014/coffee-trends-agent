"""
Coffee Trends Agent - A2A Communication Demo
This script demonstrates the A2A communication between:
- Coffee Trends Agent (exposed via A2A on port 8001)
- BAHO Strategy Agent (consumer, uses Coffee Trends Agent via A2A)
"""

import os
import json
import requests
import subprocess
import time
import uuid
import asyncio
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types

import sys
from pathlib import Path

# Add parent directory to path for imports
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

# Import agents
from agents import coffee_trends_agent, baho_strategy_agent


def setup_environment():
    """Setup environment variables and verify API key."""
    if "GOOGLE_API_KEY" not in os.environ:
        print("⚠️  Warning: GOOGLE_API_KEY not found in environment variables.")
        print("\n   Please set it:")
        print("   Windows PowerShell: $env:GOOGLE_API_KEY = 'your-key-here'")
        print("   Windows CMD: set GOOGLE_API_KEY=your-key-here")
        print("   Linux/Mac: export GOOGLE_API_KEY='your-key-here'")
        return False
    
    print("✅ Environment setup complete.")
    return True


def start_coffee_trends_server():
    """Start the Coffee Trends Agent server in the background."""
    print("\n🚀 Starting Coffee Trends Agent server...")
    print("   Waiting for server to be ready...")
    
    # Start uvicorn server in background
    server_process = subprocess.Popen(
        [
            "uvicorn",
            "servers.coffee_trends_server:app",
            "--host",
            "localhost",
            "--port",
            "8001",
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        env={**os.environ},
    )
    
    # Wait for server to start
    max_attempts = 30
    for attempt in range(max_attempts):
        try:
            response = requests.get(
                "http://localhost:8001/.well-known/agent-card.json", timeout=1
            )
            if response.status_code == 200:
                print(f"\n✅ Coffee Trends Agent server is running!")
                print(f"   Server URL: http://localhost:8001")
                print(f"   Agent card: http://localhost:8001/.well-known/agent-card.json")
                return server_process
        except requests.exceptions.RequestException:
            time.sleep(1)
            print(".", end="", flush=True)
    
    print("\n⚠️  Server may not be ready yet. Check manually if needed.")
    return server_process


def view_agent_card():
    """View the auto-generated agent card."""
    try:
        response = requests.get(
            "http://localhost:8001/.well-known/agent-card.json", timeout=5
        )
        if response.status_code == 200:
            agent_card = response.json()
            print("\n📋 Coffee Trends Agent Card:")
            print(json.dumps(agent_card, indent=2))
            print("\n✨ Key Information:")
            print(f"   Name: {agent_card.get('name')}")
            print(f"   Description: {agent_card.get('description')}")
            print(f"   URL: {agent_card.get('url')}")
            print(f"   Skills: {len(agent_card.get('skills', []))} capabilities exposed")
            return True
        else:
            print(f"❌ Failed to fetch agent card: {response.status_code}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"❌ Error fetching agent card: {e}")
        return False


async def test_baho_strategy_agent(user_query: str):
    """
    Test the BAHO Strategy Agent with a user query.
    The agent will communicate with Coffee Trends Agent via A2A.
    """
    # Setup session management
    session_service = InMemorySessionService()
    
    # Session identifiers
    app_name = "baho_strategy_app"
    user_id = "demo_user"
    session_id = f"demo_session_{uuid.uuid4().hex[:8]}"
    
    # Create session
    session = await session_service.create_session(
        app_name=app_name, user_id=user_id, session_id=session_id
    )
    
    # Create runner
    runner = Runner(
        agent=baho_strategy_agent,
        app_name=app_name,
        session_service=session_service
    )
    
    # Create user message
    test_content = types.Content(parts=[types.Part(text=user_query)])
    
    # Display query
    print(f"\n👤 Question: {user_query}")
    print(f"\n🎯 BAHO Strategy Agent Response:")
    print("-" * 80)
    
    # Run the agent
    async for event in runner.run_async(
        user_id=user_id, session_id=session_id, new_message=test_content
    ):
        if event.is_final_response() and event.content:
            for part in event.content.parts:
                if hasattr(part, "text"):
                    print(part.text)
    
    print("-" * 80)


async def run_demo():
    """Run the complete A2A communication demo."""
    print("=" * 80)
    print("☕ Coffee Trends Agent - A2A Communication Demo")
    print("=" * 80)
    print("\nThis demo shows how:")
    print("  1. Coffee Trends Agent provides global coffee market intelligence")
    print("  2. BAHO Strategy Agent consumes it via A2A protocol")
    print("  3. Together they provide strategic insights for BAHO COFFEE COMPANY")
    print("=" * 80)
    
    # Setup
    if not setup_environment():
        return
    
    # Start server
    server_process = start_coffee_trends_server()
    
    # View agent card
    time.sleep(2)  # Give server a moment
    view_agent_card()
    
    # Run test queries
    print("\n" + "=" * 80)
    print("🧪 Testing A2A Communication with BAHO Strategy Agent")
    print("=" * 80)
    
    test_queries = [
        "What are the most important coffee trends for BAHO to focus on?",
        "How should BAHO position itself in the specialty coffee market?",
        "What pricing strategy should BAHO use for its Rwandan specialty coffee?",
        "What are the opportunities for BAHO in direct-to-consumer sales?",
        "How can BAHO differentiate itself from other specialty coffee producers?",
        "What are the key trends in Rwandan coffee that BAHO should leverage?",
    ]
    
    for i, query in enumerate(test_queries, 1):
        print(f"\n\n📊 Test {i}/{len(test_queries)}")
        await test_baho_strategy_agent(query)
        if i < len(test_queries):
            time.sleep(2)  # Brief pause between queries
    
    print("\n" + "=" * 80)
    print("✅ Demo Complete!")
    print("=" * 80)
    print("\n💡 The Coffee Trends Agent server is still running.")
    print("   You can continue asking questions or stop the server.")
    print("\n   To stop the server, press Ctrl+C or close this terminal.")
    
    # Keep server running (in production, you'd manage this differently)
    try:
        server_process.wait()
    except KeyboardInterrupt:
        print("\n\n🛑 Stopping server...")
        server_process.terminate()
        print("✅ Server stopped.")


if __name__ == "__main__":
    asyncio.run(run_demo())

