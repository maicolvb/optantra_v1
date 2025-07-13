#!/usr/bin/env python3
"""
Test script to verify OpenAI API configuration
Run this to check if your API key is working correctly
"""

import openai
import os
from dotenv import load_dotenv

def test_openai_api():
    """Test OpenAI API configuration"""
    print("🔧 Testing OpenAI API Configuration...")
    print("=" * 50)
    
    # Load environment variables
    load_dotenv()
    
    # Get API key
    api_key = os.getenv("OPENAI_API_KEY")
    
    if not api_key:
        print("❌ No API key found!")
        print("\n📝 To fix this:")
        print("1. Create a .env file in this directory")
        print("2. Add: OPENAI_API_KEY=your_actual_api_key")
        print("3. Or set environment variable: $env:OPENAI_API_KEY='your_key'")
        print("4. Or enter it directly in the app sidebar")
        return False
    
    if not api_key.startswith("sk-"):
        print("❌ Invalid API key format!")
        print("API key should start with 'sk-'")
        return False
    
    # Configure OpenAI
    openai.api_key = api_key
    
    try:
        print("🔄 Testing API connection...")
        
        # Test with a simple request
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": "Say 'Hello from Optantra!'"}],
            max_tokens=20
        )
        
        result = response.choices[0].message.content
        print(f"✅ API is working! Response: {result}")
        
        # Test with logistics prompt
        print("\n🔄 Testing logistics analysis...")
        logistics_response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a logistics expert."},
                {"role": "user", "content": "Briefly suggest one improvement for inventory management."}
            ],
            max_tokens=50
        )
        
        logistics_result = logistics_response.choices[0].message.content
        print(f"✅ Logistics analysis working! Suggestion: {logistics_result}")
        
        print("\n🎉 All tests passed! Your Optantra app should work perfectly.")
        return True
        
    except openai.error.AuthenticationError:
        print("❌ Authentication failed!")
        print("Check that your API key is correct and active.")
        return False
        
    except openai.error.RateLimitError:
        print("❌ Rate limit exceeded!")
        print("You may have exceeded your OpenAI usage limits.")
        return False
        
    except openai.error.APIError as e:
        print(f"❌ API Error: {e}")
        return False
        
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False

if __name__ == "__main__":
    success = test_openai_api()
    
    if success:
        print("\n🚀 You can now run: streamlit run optantra.py")
    else:
        print("\n🔧 Please fix the configuration issues above before running the app.") 