"""Simple test script to verify Tavily API key is working."""

import os
from tavily import TavilyClient

def test_tavily_connection():
    """Test if Tavily API key is configured and working."""
    
    # Check if API key is set
    api_key = os.environ.get("TAVILY_API_KEY")
    
    if not api_key:
        print("❌ TAVILY_API_KEY not found in environment variables")
        print("Please set it using: set TAVILY_API_KEY=your_api_key")
        return False
    
    print(f"✓ TAVILY_API_KEY found: {api_key[:10]}...")
    
    # Try to initialize client
    try:
        tavily_client = TavilyClient(api_key=api_key)
        print("✓ TavilyClient initialized successfully")
    except Exception as e:
        print(f"❌ Failed to initialize TavilyClient: {e}")
        return False
    
    # Try a simple search
    try:
        print("\nTesting search with query: 'Python programming'...")
        result = tavily_client.search("Python programming", max_results=2)
        
        if "results" in result:
            print(f"✓ Search successful! Found {len(result['results'])} results")
            print("\nFirst result:")
            if result['results']:
                first = result['results'][0]
                print(f"  Title: {first.get('title', 'N/A')}")
                print(f"  URL: {first.get('url', 'N/A')}")
                print(f"  Content preview: {first.get('content', 'N/A')[:100]}...")
            return True
        else:
            print(f"❌ Unexpected response format: {result}")
            return False
            
    except Exception as e:
        print(f"❌ Search failed: {e}")
        return False

if __name__ == "__main__":
    print("=" * 60)
    print("Testing Tavily API Configuration")
    print("=" * 60)
    
    success = test_tavily_connection()
    
    print("\n" + "=" * 60)
    if success:
        print("✅ All tests passed! Tavily API is working correctly.")
    else:
        print("❌ Tests failed. Please check your API key and internet connection.")
    print("=" * 60)
