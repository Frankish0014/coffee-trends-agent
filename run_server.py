"""
Main entry point to run the Coffee Trends Agent server
"""

from servers.coffee_trends_server import app
import uvicorn

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8001)

