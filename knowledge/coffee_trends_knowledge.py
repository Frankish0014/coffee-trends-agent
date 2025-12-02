"""
Coffee Trends Knowledge Base
Comprehensive database of global coffee trends relevant for specialty coffee producers
"""

from typing import Dict, List, Optional
from datetime import datetime

# Global Coffee Market Trends Database
COFFEE_TRENDS_DB = {
    # Market Trends
    "specialty_coffee_growth": {
        "trend": "Specialty Coffee Market Growth",
        "description": "The specialty coffee market is experiencing 13-15% annual growth globally, driven by consumer demand for quality, origin stories, and sustainable practices.",
        "impact": "High - Directly relevant for BAHO as a specialty producer",
        "opportunity": "Position BAHO as a premium Rwandan specialty brand with unique origin story",
        "data_points": [
            "Specialty coffee represents 37% of US coffee market (up from 15% in 2015)",
            "Premium coffee segment growing 2x faster than commodity coffee",
            "Consumers willing to pay 20-40% premium for specialty coffee"
        ],
        "relevance_to_baho": "BAHO can leverage Rwanda's unique terroir and processing methods to command premium pricing"
    },
    
    "sustainability_demand": {
        "trend": "Sustainability and Ethical Sourcing",
        "description": "Consumers increasingly prioritize sustainable, ethically sourced coffee with transparent supply chains. Fair trade and direct trade models are gaining traction.",
        "impact": "Critical - Essential for market access and premium positioning",
        "opportunity": "Highlight BAHO's direct relationships with Rwandan farmers and sustainable practices",
        "data_points": [
            "68% of consumers prefer brands with strong environmental values",
            "Carbon-neutral and regenerative agriculture practices are differentiators",
            "Traceability from farm to cup is now expected by premium consumers"
        ],
        "relevance_to_baho": "Rwanda's smallholder farmer model aligns perfectly with direct trade and sustainability narratives"
    },
    
    "origin_story_importance": {
        "trend": "Origin Story and Terroir Focus",
        "description": "Coffee drinkers want to know where their coffee comes from. Single-origin, terroir-driven coffees command premium prices. Rwanda's unique volcanic soil and high altitude create distinctive flavor profiles.",
        "impact": "High - Core differentiator for BAHO",
        "opportunity": "Emphasize Rwanda's unique terroir: volcanic soil, high altitude (1500-2000m), ideal climate",
        "data_points": [
            "Single-origin coffees growing 25% annually",
            "Consumers value unique flavor profiles tied to geography",
            "Rwandan coffee known for bright acidity, floral notes, and clean cup"
        ],
        "relevance_to_baho": "BAHO can differentiate through Rwanda's unique terroir and processing methods (washed, natural, honey)"
    },
    
    "processing_methods": {
        "trend": "Innovative Processing Methods",
        "description": "Natural, honey, and experimental processing methods are gaining popularity. Consumers seek unique flavor profiles beyond traditional washed coffees.",
        "impact": "Medium-High - Opportunity for product diversification",
        "opportunity": "Offer variety: washed (clean, bright), natural (fruity, complex), honey (balanced)",
        "data_points": [
            "Natural processed coffees growing 30% annually",
            "Honey processed coffees gaining traction in specialty market",
            "Experimental processing creates premium positioning"
        ],
        "relevance_to_baho": "BAHO can offer diverse processing methods to appeal to different consumer preferences"
    },
    
    "roast_preferences": {
        "trend": "Lighter Roast Preferences",
        "description": "Specialty coffee market shifting toward lighter roasts that preserve origin characteristics. Medium-light to light roasts dominate specialty segment.",
        "impact": "Medium - Affects product positioning",
        "opportunity": "Position BAHO coffees as light-medium roast to highlight origin flavors",
        "data_points": [
            "Light roast specialty coffee growing 18% annually",
            "Consumers want to taste origin, not roast",
            "Lighter roasts preserve Rwanda's bright, floral characteristics"
        ],
        "relevance_to_baho": "BAHO should emphasize light-medium roasts to showcase Rwanda's unique flavor profile"
    },
    
    "direct_to_consumer": {
        "trend": "Direct-to-Consumer (D2C) Growth",
        "description": "Coffee producers are increasingly selling directly to consumers via online platforms, subscription services, and e-commerce. This model offers higher margins and direct customer relationships.",
        "impact": "High - Revenue diversification opportunity",
        "opportunity": "BAHO can establish D2C channels: website, subscription service, online marketplace",
        "data_points": [
            "D2C coffee sales growing 35% annually",
            "Subscription coffee services have 60% retention rate",
            "Higher margins (40-60%) vs wholesale (20-30%)"
        ],
        "relevance_to_baho": "BAHO can build direct relationships with consumers, tell origin stories, and capture more value"
    },
    
    "cold_brew_nitro": {
        "trend": "Cold Brew and Nitro Coffee",
        "description": "Cold brew and nitro coffee continue to grow, especially in ready-to-drink (RTD) formats. These products command premium prices and appeal to younger demographics.",
        "impact": "Medium - Product extension opportunity",
        "opportunity": "Consider RTD cold brew products featuring BAHO coffee",
        "data_points": [
            "Cold brew market growing 25% annually",
            "Nitro coffee premium of 30-40% over regular cold brew",
            "RTD coffee segment worth $5.5B globally"
        ],
        "relevance_to_baho": "BAHO could explore RTD products to reach new consumer segments"
    },
    
    "functional_coffee": {
        "trend": "Functional and Health-Focused Coffee",
        "description": "Coffee with added functional benefits (adaptogens, probiotics, vitamins) is emerging. However, specialty coffee purists prefer clean, high-quality beans without additives.",
        "impact": "Low-Medium - Niche opportunity",
        "opportunity": "Focus on natural health benefits of high-quality Rwandan coffee (antioxidants, natural energy)",
        "data_points": [
            "Functional coffee segment growing but still niche",
            "Specialty consumers prefer clean, additive-free coffee",
            "Natural health benefits of quality coffee are sufficient differentiator"
        ],
        "relevance_to_baho": "BAHO should emphasize natural quality and health benefits rather than additives"
    },
    
    "price_premiums": {
        "trend": "Premium Pricing Acceptance",
        "description": "Consumers are increasingly accepting of premium pricing for specialty coffee, especially when tied to quality, origin story, and sustainability.",
        "impact": "High - Revenue opportunity",
        "opportunity": "BAHO can command premium pricing ($18-30/lb) for specialty Rwandan coffee",
        "data_points": [
            "Specialty coffee average price: $18-25/lb retail",
            "Ultra-premium single-origin: $25-40/lb",
            "Consumers pay premium for transparency and quality"
        ],
        "relevance_to_baho": "BAHO's specialty positioning allows for premium pricing, especially with direct trade model"
    },
    
    # Rwanda-Specific Trends
    "rwanda_coffee_reputation": {
        "trend": "Rwandan Coffee Market Position",
        "description": "Rwandan coffee is gaining recognition in specialty markets for its quality, unique flavor profile, and compelling origin story. The country's focus on quality and women's empowerment in coffee is a strong narrative.",
        "impact": "Critical - Core brand positioning",
        "opportunity": "Leverage Rwanda's growing reputation and unique story (post-genocide recovery, women in coffee)",
        "data_points": [
            "Rwandan coffee Cup of Excellence winners increasing",
            "Known for bright acidity, floral notes, tea-like body",
            "Women's cooperatives in Rwanda are industry leaders"
        ],
        "relevance_to_baho": "BAHO can highlight Rwanda's unique story and quality to differentiate in market"
    },
    
    "african_coffee_rising": {
        "trend": "African Coffee Origin Recognition",
        "description": "African coffee origins (Ethiopia, Kenya, Rwanda, Burundi) are gaining prominence in specialty markets. Consumers are discovering unique flavor profiles from the continent.",
        "impact": "High - Market tailwind",
        "opportunity": "Position BAHO as part of rising African specialty coffee movement",
        "data_points": [
            "African coffee exports growing 8% annually",
            "Specialty roasters seeking unique African origins",
            "Rwanda positioned as premium African origin"
        ],
        "relevance_to_baho": "BAHO benefits from broader African coffee trend while maintaining Rwanda-specific differentiation"
    },
    
    # Consumer Behavior Trends
    "home_brewing": {
        "trend": "Home Brewing Equipment Investment",
        "description": "Consumers are investing in quality home brewing equipment (pour-over, espresso machines, grinders). This creates demand for whole bean specialty coffee.",
        "impact": "High - Direct market opportunity",
        "opportunity": "BAHO should focus on whole bean sales and provide brewing guides",
        "data_points": [
            "Home coffee equipment market growing 12% annually",
            "Whole bean sales growing faster than ground coffee",
            "Consumers want to replicate café quality at home"
        ],
        "relevance_to_baho": "BAHO should prioritize whole bean offerings and provide brewing education"
    },
    
    "subscription_models": {
        "trend": "Coffee Subscription Services",
        "description": "Subscription coffee services are popular, offering convenience and discovery. Consumers subscribe to receive regular deliveries of specialty coffee.",
        "impact": "High - Recurring revenue opportunity",
        "opportunity": "BAHO can offer subscription service with rotating single-origins and processing methods",
        "data_points": [
            "Coffee subscription market worth $2.1B",
            "Average subscription: $20-30/month",
            "High retention rates (60%+) for quality providers"
        ],
        "relevance_to_baho": "Subscription model provides predictable revenue and customer relationships"
    },
    
    "social_media_influence": {
        "trend": "Social Media and Coffee Culture",
        "description": "Instagram, TikTok, and coffee-focused social media drive discovery and purchase decisions. Visual storytelling and origin narratives perform well.",
        "impact": "High - Marketing channel",
        "opportunity": "BAHO should invest in visual storytelling: farm photos, processing videos, origin stories",
        "data_points": [
            "68% of coffee consumers discover new brands via social media",
            "Visual content (photos, videos) drives engagement",
            "Origin stories and behind-the-scenes content perform best"
        ],
        "relevance_to_baho": "BAHO can leverage Rwanda's visual appeal and story for social media marketing"
    },
    
    # Competitive Landscape
    "competition_intensity": {
        "trend": "Specialty Coffee Competition",
        "description": "Specialty coffee market is competitive with many roasters and producers. Differentiation through quality, story, and direct relationships is key.",
        "impact": "High - Requires strong positioning",
        "opportunity": "BAHO must differentiate through: Rwanda-specific terroir, direct trade, quality, and story",
        "data_points": [
            "Thousands of specialty roasters globally",
            "Competition intensifying but market growing",
            "Quality and story are key differentiators"
        ],
        "relevance_to_baho": "BAHO needs clear positioning: premium Rwandan specialty coffee with direct trade model"
    },
    
    # Technology Trends
    "blockchain_traceability": {
        "trend": "Blockchain and Supply Chain Transparency",
        "description": "Some producers are using blockchain to provide complete traceability from farm to cup. This appeals to consumers who value transparency.",
        "impact": "Low-Medium - Future consideration",
        "opportunity": "Consider implementing traceability technology to show farm-to-cup journey",
        "data_points": [
            "Traceability technology still emerging",
            "Appeals to premium consumers",
            "Can command 10-15% price premium"
        ],
        "relevance_to_baho": "BAHO could explore traceability tech as premium differentiator"
    },
    
    "ai_roasting": {
        "trend": "AI and Precision Roasting",
        "description": "AI-assisted roasting is emerging but specialty market still values human expertise and artisanal approach.",
        "impact": "Low - Not critical for BAHO",
        "opportunity": "Emphasize artisanal, human-driven quality over automation",
        "data_points": [
            "AI roasting still niche",
            "Specialty consumers value human expertise",
            "Artisanal approach is differentiator"
        ],
        "relevance_to_baho": "BAHO should emphasize human expertise and artisanal quality"
    }
}

# Rwandan Coffee Specific Information
RWANDA_COFFEE_INFO = {
    "terroir": {
        "altitude": "1500-2000 meters above sea level",
        "soil": "Volcanic, rich in minerals",
        "climate": "Tropical highland with distinct wet/dry seasons",
        "flavor_profile": "Bright acidity, floral notes (jasmine, bergamot), tea-like body, clean cup"
    },
    "processing_methods": {
        "washed": "Most common, produces clean, bright cup with floral notes",
        "natural": "Less common but growing, produces fruity, complex flavors",
        "honey": "Emerging, produces balanced, sweet cup"
    },
    "regions": {
        "nyamasheke": "Known for complex, wine-like flavors",
        "huye": "Bright, citrusy, tea-like",
        "muhanga": "Balanced, sweet, floral",
        "karongi": "Full-bodied, chocolate notes"
    },
    "quality_grades": {
        "specialty": "85+ points (SCAA), premium pricing",
        "premium": "80-84 points, good quality",
        "standard": "Below 80, commodity pricing"
    },
    "market_positioning": {
        "strengths": [
            "Unique terroir and flavor profile",
            "Growing reputation in specialty markets",
            "Compelling origin story (post-conflict recovery)",
            "Women's empowerment in coffee sector",
            "Focus on quality and sustainability"
        ],
        "challenges": [
            "Lesser known than Ethiopia/Kenya",
            "Smaller production volume",
            "Infrastructure and logistics",
            "Price volatility"
        ],
        "opportunities": [
            "Rising specialty coffee demand",
            "African origin trend",
            "Direct trade relationships",
            "Premium pricing acceptance",
            "D2C channels"
        ]
    }
}


def get_coffee_trend(trend_key: str) -> Dict:
    """
    Get detailed information about a specific coffee trend.
    
    Args:
        trend_key: Key identifying the trend (e.g., "specialty_coffee_growth")
    
    Returns:
        Dictionary with trend information
    """
    if trend_key.lower() in COFFEE_TRENDS_DB:
        return COFFEE_TRENDS_DB[trend_key.lower()]
    else:
        available_trends = list(COFFEE_TRENDS_DB.keys())
        return {
            "error": f"Trend '{trend_key}' not found.",
            "available_trends": available_trends
        }


def search_coffee_trends(query: str) -> List[Dict]:
    """
    Search for coffee trends matching a query.
    
    Args:
        query: Search query (e.g., "sustainability", "pricing", "Rwanda")
    
    Returns:
        List of matching trends
    """
    query_lower = query.lower()
    matches = []
    
    for key, trend_data in COFFEE_TRENDS_DB.items():
        # Search in trend name, description, and relevance
        searchable_text = f"{trend_data['trend']} {trend_data['description']} {trend_data.get('relevance_to_baho', '')}".lower()
        
        if query_lower in searchable_text or query_lower in key:
            matches.append({
                "key": key,
                **trend_data
            })
    
    return matches


def get_rwanda_coffee_info(category: Optional[str] = None) -> Dict:
    """
    Get information about Rwandan coffee.
    
    Args:
        category: Optional category (terroir, processing_methods, regions, quality_grades, market_positioning)
    
    Returns:
        Dictionary with Rwandan coffee information
    """
    if category:
        if category.lower() in RWANDA_COFFEE_INFO:
            return RWANDA_COFFEE_INFO[category.lower()]
        else:
            return {
                "error": f"Category '{category}' not found.",
                "available_categories": list(RWANDA_COFFEE_INFO.keys())
            }
    else:
        return RWANDA_COFFEE_INFO


def get_trends_for_baho_strategy() -> Dict:
    """
    Get strategic insights combining all trends relevant to BAHO COFFEE COMPANY.
    
    Returns:
        Comprehensive strategic analysis
    """
    high_impact_trends = [
        trend for trend in COFFEE_TRENDS_DB.values()
        if trend.get("impact") in ["High", "Critical"]
    ]
    
    return {
        "summary": "Strategic Coffee Trends Analysis for BAHO COFFEE COMPANY",
        "date": datetime.now().strftime("%Y-%m-%d"),
        "high_impact_trends": high_impact_trends,
        "key_opportunities": [
            "Premium pricing through specialty positioning",
            "Direct-to-consumer channels for higher margins",
            "Leverage Rwanda's unique terroir and story",
            "Sustainability and direct trade narratives",
            "Subscription service for recurring revenue",
            "Social media storytelling for brand building"
        ],
        "strategic_recommendations": [
            "Position as premium Rwandan specialty coffee with unique terroir",
            "Establish D2C channels (website, subscription)",
            "Emphasize direct trade and sustainability",
            "Offer diverse processing methods (washed, natural, honey)",
            "Focus on whole bean sales with brewing education",
            "Invest in visual storytelling and origin narratives",
            "Target light-medium roasts to showcase origin flavors",
            "Build relationships with specialty roasters and cafés"
        ],
        "market_positioning": RWANDA_COFFEE_INFO["market_positioning"]
    }

