# ☕ Coffee Trends Agent - A2A Communication System

A multi-agent system built with Google ADK that provides comprehensive coffee market intelligence and strategic insights for **BAHO COFFEE COMPANY**, a Rwandan specialty coffee producer.

## 🎯 Overview

This system demonstrates **Agent2Agent (A2A) Communication** using the Google Agent Development Kit (ADK). It consists of two agents:

1. **Coffee Trends Agent** (Exposed via A2A)
   - Provides global coffee market trends and intelligence
   - Specializes in specialty coffee, sustainability, pricing, and consumer behavior
   - Includes comprehensive information about Rwandan coffee characteristics
   - Served as an A2A-compatible service on port 8001

2. **BAHO Strategy Agent** (Consumer)
   - Strategic advisor for BAHO COFFEE COMPANY
   - Consumes the Coffee Trends Agent via A2A protocol
   - Provides actionable insights and recommendations tailored for BAHO
   - Focuses on market positioning, pricing, distribution, and growth strategies

## 🏗️ Architecture

```
┌─────────────────────────┐           ┌─────────────────────────┐
│  BAHO Strategy Agent    │  ─A2A──▶  │  Coffee Trends Agent    │
│  (Consumer)             │           │  (Exposed Service)      │
│  localhost:8000         │           │  localhost:8001         │
└─────────────────────────┘           └─────────────────────────┘
```

## 📋 Features

### Coffee Trends Agent Capabilities

- **Global Market Trends**: Specialty coffee growth, sustainability, pricing, consumer behavior
- **Rwandan Coffee Intelligence**: Terroir, processing methods, flavor profiles, regions
- **Strategic Analysis**: Market positioning, competitive landscape, opportunities
- **Trend Search**: Search trends by topic (sustainability, pricing, specialty, etc.)
- **BAHO-Specific Insights**: Strategic recommendations tailored for Rwandan specialty producers

### BAHO Strategy Agent Capabilities

- **Strategic Planning**: Market positioning and competitive analysis
- **Pricing Strategy**: Recommendations based on market trends
- **Distribution Channels**: D2C, wholesale, subscription models
- **Marketing Insights**: Brand positioning and storytelling
- **Product Development**: Processing methods, roast profiles
- **Growth Opportunities**: Actionable recommendations for expansion

## 🚀 Quick Start

### Prerequisites

1. **Python 3.8+**
2. **Google API Key** (Gemini API)
   - Get your API key from [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Set it as an environment variable:
     - **Windows PowerShell**: `$env:GOOGLE_API_KEY = "your-key-here"`
     - **Windows CMD**: `set GOOGLE_API_KEY=your-key-here`
     - **Linux/Mac**: `export GOOGLE_API_KEY='your-key-here'`

### Installation

1. **Clone or download this repository**

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Demo

**Option 1: Run the complete demo script**
```bash
python demo_a2a_coffee_trends.py
```

This will:
- Start the Coffee Trends Agent server on port 8001
- Display the agent card
- Run several test queries through the BAHO Strategy Agent
- Demonstrate A2A communication in action

**Option 2: Run components separately**

1. **Start the Coffee Trends Agent server**:
   ```bash
   python run_server.py
   # Or using uvicorn directly:
   uvicorn servers.coffee_trends_server:app --host localhost --port 8001
   ```

2. **In a separate terminal, use the BAHO Strategy Agent**:
   ```python
   from agents import baho_strategy_agent
   from google.adk.runners import Runner
   from google.adk.sessions import InMemorySessionService
   from google.genai import types
   import asyncio
   
   # Your code to interact with baho_strategy_agent
   ```

## 📚 Knowledge Base

The system includes a comprehensive coffee trends knowledge base covering:

- **Market Trends**: 15+ key trends including specialty growth, sustainability, pricing, D2C
- **Rwandan Coffee Info**: Terroir, processing methods, regions, quality grades, market positioning
- **Strategic Insights**: High-impact trends, opportunities, and recommendations for BAHO

### Available Trends

- Specialty coffee market growth
- Sustainability and ethical sourcing
- Origin story and terroir focus
- Processing methods (washed, natural, honey)
- Roast preferences
- Direct-to-consumer growth
- Cold brew and nitro coffee
- Functional coffee
- Premium pricing acceptance
- Rwandan coffee reputation
- African coffee origin recognition
- Home brewing equipment
- Subscription models
- Social media influence
- Competition intensity
- Blockchain traceability
- AI roasting

## 🧪 Example Queries

Try asking the BAHO Strategy Agent:

- "What are the most important coffee trends for BAHO to focus on?"
- "How should BAHO position itself in the specialty coffee market?"
- "What pricing strategy should BAHO use for its Rwandan specialty coffee?"
- "What are the opportunities for BAHO in direct-to-consumer sales?"
- "How can BAHO differentiate itself from other specialty coffee producers?"
- "What are the key trends in Rwandan coffee that BAHO should leverage?"

## 🔧 Configuration

### Environment Variables

- `GOOGLE_API_KEY`: Required. Your Gemini API key from Google AI Studio.

### Port Configuration

- **Coffee Trends Agent**: Port 8001 (configurable in `coffee_trends_agent.py`)
- **BAHO Strategy Agent**: Uses the Coffee Trends Agent via A2A

### Model Configuration

Both agents use `gemini-2.5-flash-lite` by default. You can modify this in:
- `coffee_trends_agent.py` (Coffee Trends Agent)
- `baho_strategy_agent.py` (BAHO Strategy Agent)

## 📖 Understanding A2A Communication

### What is A2A?

**Agent2Agent (A2A) Protocol** is a standardized protocol that allows agents to:
- Communicate over networks (agents can be on different machines)
- Use each other's capabilities (one agent can call another like a tool)
- Work across frameworks (language/framework agnostic)
- Maintain formal contracts (agent cards describe capabilities)

### How It Works

1. **Coffee Trends Agent** is exposed via A2A using `to_a2a()`
   - Creates a FastAPI/Starlette server
   - Auto-generates an agent card at `/.well-known/agent-card.json`
   - Handles A2A protocol endpoints

2. **BAHO Strategy Agent** consumes it using `RemoteA2aAgent`
   - Acts as a client-side proxy
   - Reads the remote agent's card
   - Translates sub-agent calls into A2A protocol requests
   - Handles all protocol details transparently

3. **Communication Flow**:
   - User asks BAHO Strategy Agent a question
   - BAHO Agent needs coffee trends data
   - BAHO Agent calls Coffee Trends Agent via A2A (HTTP POST to `/tasks`)
   - Coffee Trends Agent processes and responds
   - BAHO Agent formulates final answer
   - User receives comprehensive strategic insight

## 🎓 Learning Resources

- [ADK Documentation](https://github.com/google/adk)
- [A2A Protocol Specification](https://a2a.dev/)
- [Introduction to A2A in ADK](https://github.com/google/adk)
- [Exposing Agents Quickstart](https://github.com/google/adk)
- [Consuming Agents Quickstart](https://github.com/google/adk)

## 🚀 Production Deployment

For production deployment:

1. **Deploy Coffee Trends Agent** to a cloud service:
   - Google Cloud Run
   - Agent Engine
   - GKE
   - Any containerized service

2. **Update agent card URL** in `baho_strategy_agent.py`:
   ```python
   agent_card=f"https://your-production-url.com{AGENT_CARD_WELL_KNOWN_PATH}"
   ```

3. **Add authentication** (API keys, OAuth) between agents

4. **Implement error handling** and retries for network failures

## 📝 File Structure

```
coffee-trends-agent/
├── agents/                        # Agent implementations
│   ├── coffee_trends_agent.py     # Coffee Trends Agent (A2A service)
│   └── baho_strategy_agent.py     # BAHO Strategy Agent (consumer)
├── knowledge/                     # Knowledge base
│   └── coffee_trends_knowledge.py # Coffee trends database
├── servers/                       # Server implementations
│   └── coffee_trends_server.py   # Server entry point
├── demos/                         # Demo scripts
│   ├── demo_a2a_coffee_trends.py  # Complete demo
│   └── interactive_demo.py       # Interactive chat
├── run_server.py                  # 🚀 Start server
├── run_demo.py                    # 🚀 Run demo
├── run_interactive.py             # 🚀 Interactive chat
├── requirements.txt               # Python dependencies
└── README.md                      # This file
```

## 🎯 Impact for BAHO COFFEE COMPANY

This system provides BAHO with:

✅ **Market Intelligence**: Real-time access to global coffee trends  
✅ **Strategic Insights**: Data-driven recommendations for growth  
✅ **Competitive Positioning**: Understanding of market dynamics  
✅ **Opportunity Identification**: Actionable opportunities for expansion  
✅ **Rwandan Coffee Expertise**: Deep knowledge of Rwanda's unique position  

## 🤝 Contributing

This is a demonstration project. Feel free to:
- Extend the knowledge base with more trends
- Add more specialized agents
- Integrate with real data sources
- Deploy to production environments

## 📄 License

This project is for educational and demonstration purposes.

## 🙏 Acknowledgments

- Built with [Google Agent Development Kit (ADK)](https://github.com/google/adk)
- Uses [A2A Protocol](https://a2a.dev/) for agent communication
- Designed for **BAHO COFFEE COMPANY** - Rwandan Specialty Coffee Producer

---

**☕ Built with passion for coffee and AI!**



You can run a full DEMO.
BY;
cd C:\Users\byiri\coffee-trends-agent\coffee-trends-agent
$env:GOOGLE_API_KEY = "AIzaSyDyk8e7iGvc1nAa_kSXyGPzEieth8LRxLs"
python run_demo.py


You can use the recommended interactive chat with my ai agent.
BY;
cd C:\Users\byiri\coffee-trends-agent\coffee-trends-agent
$env:GOOGLE_API_KEY = "AIzaSyDyk8e7iGvc1nAa_kSXyGPzEieth8LRxLs"
python run_interactive.py

Use the helper script if you want!
BY
cd C:\Users\byiri\coffee-trends-agent\coffee-trends-agent
.\run_interactive_with_env.ps1