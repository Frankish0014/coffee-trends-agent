"""
Main entry point to run the interactive demo
"""

import asyncio
from demos.interactive_demo import chat_with_baho_agent

if __name__ == "__main__":
    import requests
    try:
        response = requests.get("http://localhost:8001/.well-known/agent-card.json", timeout=2)
        if response.status_code == 200:
            print("✅ Coffee Trends Agent server is running!")
            asyncio.run(chat_with_baho_agent())
        else:
            print("❌ Coffee Trends Agent server is not responding.")
            print("   Please start it first: python run_server.py")
    except requests.exceptions.RequestException:
        print("❌ Coffee Trends Agent server is not running.")
        print("   Please start it first:")
        print("   python run_server.py")
        print("\n   Or in a separate terminal:")
        print("   uvicorn servers.coffee_trends_server:app --host localhost --port 8001")

