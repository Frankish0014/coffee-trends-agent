"""
Interactive Demo for Coffee Trends Agent
Simple script to interact with the BAHO Strategy Agent
"""

import os
import asyncio
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types

import sys
from pathlib import Path

# Add parent directory to path for imports
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

# Import the BAHO Strategy Agent
from agents import baho_strategy_agent


async def chat_with_baho_agent():
    """Interactive chat with BAHO Strategy Agent."""
    print("=" * 80)
    print("☕ BAHO Coffee Strategy Agent - Interactive Demo")
    print("=" * 80)
    print("\nThis agent provides strategic insights for BAHO COFFEE COMPANY")
    print("by consulting the Coffee Trends Agent via A2A protocol.")
    print("\nType 'quit' or 'exit' to end the conversation.\n")
    print("=" * 80)
    
    # Setup session
    session_service = InMemorySessionService()
    app_name = "baho_strategy_app"
    user_id = "interactive_user"
    session_id = "interactive_session"
    
    await session_service.create_session(
        app_name=app_name, user_id=user_id, session_id=session_id
    )
    
    runner = Runner(
        agent=baho_strategy_agent,
        app_name=app_name,
        session_service=session_service
    )
    
    print("\n💬 Start asking questions about coffee trends and BAHO strategy!\n")
    
    while True:
        try:
            user_input = input("\n👤 You: ").strip()
            
            if user_input.lower() in ['quit', 'exit', 'q']:
                print("\n👋 Goodbye! Thank you for using BAHO Strategy Agent.")
                break
            
            if not user_input:
                continue
            
            print("\n🎯 BAHO Strategy Agent:")
            print("-" * 80)
            
            # Create message
            test_content = types.Content(parts=[types.Part(text=user_input)])
            
            # Run agent
            async for event in runner.run_async(
                user_id=user_id, session_id=session_id, new_message=test_content
            ):
                if event.is_final_response() and event.content:
                    for part in event.content.parts:
                        if hasattr(part, "text"):
                            print(part.text)
            
            print("-" * 80)
            
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"\n❌ Error: {e}")
            print("Make sure the Coffee Trends Agent server is running on port 8001.")


if __name__ == "__main__":
    # Check if server is running
    import requests
    try:
        response = requests.get("http://localhost:8001/.well-known/agent-card.json", timeout=2)
        if response.status_code == 200:
            print("✅ Coffee Trends Agent server is running!")
            asyncio.run(chat_with_baho_agent())
        else:
            print("❌ Coffee Trends Agent server is not responding.")
            print("   Please start it first: python servers/coffee_trends_server.py")
    except requests.exceptions.RequestException:
        print("❌ Coffee Trends Agent server is not running.")
        print("   Please start it first:")
        print("   python servers/coffee_trends_server.py")
        print("\n   Or in a separate terminal:")
        print("   uvicorn servers.coffee_trends_server:app --host localhost --port 8001")

