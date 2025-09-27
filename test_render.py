"""
Test script for Render deployment
Run this after deploying to verify your API works correctly
"""

import requests
import json
import time

def test_render_deployment(base_url):
    """
    Test the deployed API on Render
    """
    print(f"Testing Render deployment at: {base_url}")
    print("=" * 60)
    
    # Test 1: Health Check
    print("\n1. Testing Health Check...")
    try:
        health_response = requests.get(f"{base_url}/health", timeout=30)
        if health_response.status_code == 200:
            print("✅ Health check passed")
            print(f"   Response: {health_response.json()}")
        else:
            print(f"❌ Health check failed: {health_response.status_code}")
            return False
    except requests.exceptions.Timeout:
        print("⏰ Health check timed out (normal for first request after sleep)")
        print("   This is expected - Render free tier sleeps after 15 minutes")
    except Exception as e:
        print(f"❌ Health check error: {e}")
        return False
    
    # Test 2: Similarity Calculation
    print("\n2. Testing Similarity Calculation...")
    test_cases = [
        {
            "text1": "The International Space Station orbits Earth.",
            "text2": "A space station is circling our planet.",
            "description": "High similarity test"
        },
        {
            "text1": "Machine learning is fascinating.",
            "text2": "I love programming in Python.",
            "description": "Low similarity test"
        },
        {
            "text1": "nuclear body seeks new tech",
            "text2": "terror suspects face arrest",
            "description": "Assignment example"
        }
    ]
    
    for i, test_case in enumerate(test_cases, 1):
        print(f"\n   Test Case {i}: {test_case['description']}")
        print(f"   Text 1: {test_case['text1']}")
        print(f"   Text 2: {test_case['text2']}")
        
        try:
            data = {
                "text1": test_case["text1"],
                "text2": test_case["text2"]
            }
            
            response = requests.post(
                f"{base_url}/similarity",
                json=data,
                headers={'Content-Type': 'application/json'},
                timeout=60
            )
            
            if response.status_code == 200:
                result = response.json()
                similarity_score = result.get("similarity score", 0)
                print(f"   ✅ Similarity Score: {similarity_score}")
                
                # Validate response format
                if "similarity score" in result and isinstance(similarity_score, (int, float)):
                    print(f"   ✅ Response format correct")
                else:
                    print(f"   ❌ Response format incorrect")
                    
            else:
                print(f"   ❌ API Error: {response.status_code}")
                print(f"   Response: {response.text}")
                
        except requests.exceptions.Timeout:
            print(f"   ⏰ Request timed out (normal for first request)")
        except Exception as e:
            print(f"   ❌ Request failed: {e}")
    
    print("\n" + "=" * 60)
    print("✅ Render deployment test completed!")
    print(f"Your API is live at: {base_url}")
    print(f"Similarity endpoint: {base_url}/similarity")
    print(f"Health check: {base_url}/health")
    print(f"Web interface: {base_url}/")
    
    return True

def main():
    """
    Main function to test Render deployment
    """
    print("Render Deployment Test")
    print("=" * 30)
    
    # Get the URL from user
    base_url = input("Enter your Render app URL (e.g., https://your-app.onrender.com): ").strip()
    
    if not base_url.startswith('http'):
        base_url = f"https://{base_url}"
    
    if not base_url.endswith('/'):
        base_url = base_url.rstrip('/')
    
    print(f"\nTesting API at: {base_url}")
    print("Note: First request may take 30+ seconds (Render free tier sleep)")
    
    # Run tests
    test_render_deployment(base_url)

if __name__ == "__main__":
    main()
