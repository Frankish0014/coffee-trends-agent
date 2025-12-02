"""
Coffee Trends Agent Server
Run this file to start the Coffee Trends Agent as an A2A service.
"""

import os
import sys
from pathlib import Path

# Add parent directory to path for imports
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from agents import coffee_trends_a2a_app

# The app is already configured in coffee_trends_agent.py
# This file just imports it for uvicorn to run
app = coffee_trends_a2a_app

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8001)

