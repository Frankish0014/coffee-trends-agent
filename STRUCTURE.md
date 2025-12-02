# 📁 Project Structure

```
coffee-trends-agent/
│
├── agents/                          # Agent implementations
│   ├── __init__.py                  # Package exports
│   ├── coffee_trends_agent.py       # Coffee Trends Agent (A2A service)
│   └── baho_strategy_agent.py       # BAHO Strategy Agent (consumer)
│
├── knowledge/                       # Knowledge base
│   ├── __init__.py                  # Package exports
│   └── coffee_trends_knowledge.py   # Coffee trends database & functions
│
├── servers/                         # Server implementations
│   ├── __init__.py                  # Package exports
│   └── coffee_trends_server.py     # Coffee Trends Agent server
│
├── demos/                           # Demo scripts
│   ├── __init__.py                  # Package exports
│   ├── demo_a2a_coffee_trends.py    # Complete A2A demo
│   └── interactive_demo.py          # Interactive chat demo
│
├── config/                          # Configuration (future use)
│   └── __init__.py
│
├── run_server.py                    # 🚀 Main entry: Start server
├── run_demo.py                      # 🚀 Main entry: Run demo
├── run_interactive.py               # 🚀 Main entry: Interactive chat
│
├── requirements.txt                 # Python dependencies
├── README.md                        # Full documentation
├── QUICKSTART.md                    # Quick start guide
├── PROJECT_SUMMARY.md               # Project overview
└── STRUCTURE.md                     # This file
```

## 🎯 Quick Commands

### Start the Server
```bash
python run_server.py
```

### Run the Demo
```bash
python run_demo.py
```

### Interactive Chat
```bash
python run_interactive.py
```

## 📦 Package Structure

### `agents/`
Contains all agent implementations:
- **coffee_trends_agent.py**: The Coffee Trends Agent exposed via A2A
- **baho_strategy_agent.py**: The BAHO Strategy Agent that consumes Coffee Trends Agent

### `knowledge/`
Contains the knowledge base:
- **coffee_trends_knowledge.py**: Database of coffee trends, Rwandan coffee info, and lookup functions

### `servers/`
Contains server implementations:
- **coffee_trends_server.py**: Uvicorn server for the Coffee Trends Agent

### `demos/`
Contains demo and example scripts:
- **demo_a2a_coffee_trends.py**: Complete demonstration of A2A communication
- **interactive_demo.py**: Interactive chat interface

## 🔧 Import Paths

All modules use relative imports from the project root:

```python
# From agents
from agents import coffee_trends_agent, baho_strategy_agent

# From knowledge
from knowledge import get_coffee_trend, search_coffee_trends

# From servers
from servers.coffee_trends_server import app
```

## 📝 Adding New Components

### Adding a New Agent
1. Create file in `agents/`
2. Export in `agents/__init__.py`
3. Import where needed

### Adding New Knowledge
1. Add to `knowledge/coffee_trends_knowledge.py` or create new file
2. Export in `knowledge/__init__.py`

### Adding a New Demo
1. Create file in `demos/`
2. Create entry point in root if needed

