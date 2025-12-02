"""
Coffee Trends Agent - Exposed via A2A
This agent provides comprehensive information about global coffee trends,
Rwandan coffee characteristics, and market insights.
"""

import os
import sys
from pathlib import Path

# Add parent directory to path for imports
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from knowledge import (
    get_coffee_trend,
    search_coffee_trends,
    get_rwanda_coffee_info,
    get_trends_for_baho_strategy
)
from google.adk.agents import LlmAgent
from google.adk.a2a.utils.agent_to_a2a import to_a2a
from google.adk.models.google_llm import Gemini
from google.genai import types


# Configure retry options
retry_config = types.HttpRetryOptions(
    attempts=5,
    exp_base=7,
    initial_delay=1,
    http_status_codes=[429, 500, 503, 504],
)


def get_coffee_trend_info(trend_key: str) -> str:
    """
    Get detailed information about a specific coffee trend.
    
    Args:
        trend_key: Key identifying the trend (e.g., "specialty_coffee_growth", "sustainability_demand")
    
    Returns:
        Formatted string with trend information
    """
    trend_data = get_coffee_trend(trend_key)
    
    if "error" in trend_data:
        return f"❌ {trend_data['error']}\nAvailable trends: {', '.join(trend_data.get('available_trends', []))}"
    
    result = f"📊 {trend_data['trend']}\n\n"
    result += f"Description: {trend_data['description']}\n\n"
    result += f"Impact Level: {trend_data['impact']}\n"
    result += f"Opportunity: {trend_data['opportunity']}\n\n"
    
    if trend_data.get('data_points'):
        result += "Key Data Points:\n"
        for point in trend_data['data_points']:
            result += f"  • {point}\n"
        result += "\n"
    
    result += f"Relevance to BAHO: {trend_data.get('relevance_to_baho', 'N/A')}\n"
    
    return result


def search_trends(query: str) -> str:
    """
    Search for coffee trends matching a query.
    
    Args:
        query: Search query (e.g., "sustainability", "pricing", "Rwanda", "specialty")
    
    Returns:
        Formatted string with matching trends
    """
    matches = search_coffee_trends(query)
    
    if not matches:
        return f"❌ No trends found matching '{query}'. Try searching for: sustainability, pricing, specialty, Rwanda, processing, etc."
    
    result = f"🔍 Found {len(matches)} trend(s) matching '{query}':\n\n"
    
    for i, match in enumerate(matches, 1):
        result += f"{i}. {match['trend']} (Key: {match['key']})\n"
        result += f"   Impact: {match['impact']}\n"
        result += f"   {match['description'][:150]}...\n\n"
    
    return result


def get_rwanda_info(category: str = None) -> str:
    """
    Get information about Rwandan coffee characteristics.
    
    Args:
        category: Optional category (terroir, processing_methods, regions, quality_grades, market_positioning)
                  If None, returns all information
    
    Returns:
        Formatted string with Rwandan coffee information
    """
    rwanda_data = get_rwanda_coffee_info(category)
    
    if "error" in rwanda_data:
        return f"❌ {rwanda_data['error']}\nAvailable categories: {', '.join(rwanda_data.get('available_categories', []))}"
    
    if category:
        # Single category
        result = f"🇷🇼 Rwandan Coffee - {category.title()}:\n\n"
        if isinstance(rwanda_data, dict):
            for key, value in rwanda_data.items():
                if isinstance(value, list):
                    result += f"{key.replace('_', ' ').title()}:\n"
                    for item in value:
                        result += f"  • {item}\n"
                else:
                    result += f"{key.replace('_', ' ').title()}: {value}\n"
        return result
    else:
        # All categories
        result = "🇷🇼 Comprehensive Rwandan Coffee Information:\n\n"
        for cat, data in rwanda_data.items():
            result += f"\n{cat.replace('_', ' ').title()}:\n"
            if isinstance(data, dict):
                for key, value in data.items():
                    if isinstance(value, list):
                        result += f"  {key.replace('_', ' ').title()}:\n"
                        for item in value:
                            result += f"    • {item}\n"
                    else:
                        result += f"  {key.replace('_', ' ').title()}: {value}\n"
            else:
                result += f"  {data}\n"
        return result


def get_baho_strategy_insights() -> str:
    """
    Get comprehensive strategic insights for BAHO COFFEE COMPANY.
    
    Returns:
        Formatted string with strategic analysis
    """
    strategy = get_trends_for_baho_strategy()
    
    result = f"🎯 {strategy['summary']}\n"
    result += f"Date: {strategy['date']}\n\n"
    
    result += "📈 HIGH IMPACT TRENDS:\n"
    for i, trend in enumerate(strategy['high_impact_trends'], 1):
        result += f"\n{i}. {trend['trend']}\n"
        result += f"   Impact: {trend['impact']}\n"
        result += f"   {trend['description'][:200]}...\n"
    
    result += "\n\n💡 KEY OPPORTUNITIES:\n"
    for i, opp in enumerate(strategy['key_opportunities'], 1):
        result += f"{i}. {opp}\n"
    
    result += "\n\n🎯 STRATEGIC RECOMMENDATIONS:\n"
    for i, rec in enumerate(strategy['strategic_recommendations'], 1):
        result += f"{i}. {rec}\n"
    
    result += "\n\n📊 MARKET POSITIONING:\n"
    mp = strategy['market_positioning']
    result += "\nStrengths:\n"
    for strength in mp['strengths']:
        result += f"  • {strength}\n"
    result += "\nChallenges:\n"
    for challenge in mp['challenges']:
        result += f"  • {challenge}\n"
    result += "\nOpportunities:\n"
    for opp in mp['opportunities']:
        result += f"  • {opp}\n"
    
    return result


# Create the Coffee Trends Agent
coffee_trends_agent = LlmAgent(
    model=Gemini(model="gemini-2.5-flash-lite", retry_options=retry_config),
    name="coffee_trends_agent",
    description="Global coffee trends and market intelligence agent specializing in specialty coffee, "
                "Rwandan coffee characteristics, and strategic insights for coffee producers.",
    instruction="""
    You are a coffee industry expert specializing in global coffee trends, market intelligence, 
    and strategic insights for specialty coffee producers, particularly Rwandan coffee.
    
    Your expertise includes:
    - Global coffee market trends (specialty coffee growth, sustainability, pricing, consumer behavior)
    - Rwandan coffee characteristics (terroir, processing methods, flavor profiles, regions)
    - Strategic insights for coffee producers
    - Market positioning and competitive analysis
    
    When asked about coffee trends:
    1. Use get_coffee_trend_info() for specific trends
    2. Use search_trends() to find trends by topic
    3. Use get_rwanda_info() for Rwandan coffee specifics
    4. Use get_baho_strategy_insights() for comprehensive strategic analysis
    
    Always provide:
    - Clear, actionable insights
    - Data-driven information
    - Relevance to specialty coffee producers
    - Strategic implications
    
    Be professional, knowledgeable, and helpful. Focus on actionable intelligence.
    """,
    tools=[
        get_coffee_trend_info,
        search_trends,
        get_rwanda_info,
        get_baho_strategy_insights
    ],
)

print("✅ Coffee Trends Agent created successfully!")
print("   Model: gemini-2.5-flash-lite")
print("   Tools: get_coffee_trend_info, search_trends, get_rwanda_info, get_baho_strategy_insights")
print("   Ready to be exposed via A2A...")

# Convert to A2A-compatible application
coffee_trends_a2a_app = to_a2a(
    coffee_trends_agent,
    port=8001  # Port where this agent will be served
)

print("\n✅ Coffee Trends Agent is now A2A-compatible!")
print("   Agent will be served at: http://localhost:8001")
print("   Agent card will be at: http://localhost:8001/.well-known/agent-card.json")

