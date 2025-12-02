# 🚀 Quick Start Guide

Get your Coffee Trends Agent system up and running in 5 minutes!

## Prerequisites

1. **Python 3.8+** installed
2. **Google API Key** (Gemini API)
   - Get it from: https://makersuite.google.com/app/apikey
   - **Windows PowerShell**: `$env:GOOGLE_API_KEY = "your-key-here"`
   - **Windows CMD**: `set GOOGLE_API_KEY=your-key-here`
   - **Linux/Mac**: `export GOOGLE_API_KEY='your-key-here'`

## Installation

```bash
# Install dependencies
pip install -r requirements.txt
```

## Running the System

### Step 1: Start the Coffee Trends Agent Server

Open a terminal and run:

```bash
python run_server.py
```

Or using uvicorn directly:

```bash
uvicorn servers.coffee_trends_server:app --host localhost --port 8001
```

You should see:
```
✅ Coffee Trends Agent server is running!
   Server URL: http://localhost:8001
```

### Step 2: Use the BAHO Strategy Agent

**Option A: Run the complete demo**
```bash
# In a new terminal
python run_demo.py
```

**Option B: Interactive chat**
```bash
# In a new terminal (make sure server is running)
python run_interactive.py
```

**Option C: Use in your own code**
```python
from agents import baho_strategy_agent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types
import asyncio

# Your code here...
```

## Example Questions to Ask

- "What are the most important coffee trends for BAHO to focus on?"
- "How should BAHO position itself in the specialty coffee market?"
- "What pricing strategy should BAHO use?"
- "What are the opportunities for BAHO in direct-to-consumer sales?"
- "How can BAHO differentiate itself from competitors?"
- "What are the key trends in Rwandan coffee?"

## Troubleshooting

**Server won't start?**
- Check if port 8001 is already in use
- Verify GOOGLE_API_KEY is set correctly
- Make sure all dependencies are installed

**Agent not responding?**
- Ensure the Coffee Trends Agent server is running
- Check the server logs for errors
- Verify the agent card is accessible: http://localhost:8001/.well-known/agent-card.json

**Import errors?**
- Run: `pip install -r requirements.txt`
- Make sure you're in the project directory

## Next Steps

- Read the full [README.md](README.md) for detailed documentation
- Explore the knowledge base in `coffee_trends_knowledge.py`
- Customize the agents for your specific needs
- Deploy to production (Cloud Run, Agent Engine, etc.)

---

**☕ Happy brewing!**

