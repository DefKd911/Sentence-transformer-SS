"""
Test script for the Semantic Similarity API
This script tests the API endpoint to ensure it works correctly.
"""

import requests
import json

def test_api():
    """
    Test the semantic similarity API endpoint.
    """
    # API endpoint URL (adjust if running on different host/port)
    base_url = "http://localhost:5000"
    
    # Test data
    test_cases = [
        {
            "text1": "The International Space Station orbits Earth.",
            "text2": "A space station is circling our planet.",
            "expected_range": (0.7, 1.0)  # Should be highly similar
        },
        {
            "text1": "Machine learning is fascinating.",
            "text2": "I love programming in Python.",
            "expected_range": (0.0, 0.5)  # Should be less similar
        },
        {
            "text1": "The cat sat on the mat.",
            "text2": "A feline was sitting on the rug.",
            "expected_range": (0.6, 1.0)  # Should be similar
        },
        {
            "text1": "Python is a programming language.",
            "text2": "Java is also a programming language.",
            "expected_range": (0.5, 0.9)  # Should be moderately similar
        }
    ]
    
    print("Testing Semantic Similarity API...")
    print("=" * 50)
    
    # Test health endpoint first
    try:
        health_response = requests.get(f"{base_url}/health")
        if health_response.status_code == 200:
            print("✓ Health check passed")
            print(f"  Response: {health_response.json()}")
        else:
            print("✗ Health check failed")
            return
    except requests.exceptions.ConnectionError:
        print("✗ Cannot connect to API. Make sure the server is running.")
        print("  Run: python app.py")
        return
    
    print("\nTesting similarity endpoint...")
    print("-" * 30)
    
    # Test each case
    for i, test_case in enumerate(test_cases, 1):
        print(f"\nTest Case {i}:")
        print(f"  Text 1: {test_case['text1']}")
        print(f"  Text 2: {test_case['text2']}")
        
        # Prepare request data
        data = {
            "text1": test_case["text1"],
            "text2": test_case["text2"]
        }
        
        try:
            # Make API request
            response = requests.post(
                f"{base_url}/similarity",
                json=data,
                headers={'Content-Type': 'application/json'}
            )
            
            if response.status_code == 200:
                result = response.json()
                similarity_score = result.get("similarity score", 0)
                
                print(f"  ✓ API Response: {similarity_score}")
                
                # Check if score is in expected range
                min_expected, max_expected = test_case["expected_range"]
                if min_expected <= similarity_score <= max_expected:
                    print(f"  ✓ Score is in expected range [{min_expected:.1f}, {max_expected:.1f}]")
                else:
                    print(f"  ⚠ Score {similarity_score:.4f} is outside expected range [{min_expected:.1f}, {max_expected:.1f}]")
                
            else:
                print(f"  ✗ API Error: {response.status_code}")
                print(f"  Response: {response.text}")
                
        except requests.exceptions.RequestException as e:
            print(f"  ✗ Request failed: {e}")
    
    print("\n" + "=" * 50)
    print("API testing completed!")

def test_api_with_curl_examples():
    """
    Print curl examples for testing the API.
    """
    print("\nCurl Examples:")
    print("-" * 20)
    
    curl_example = '''curl -X POST http://localhost:5000/similarity \\
  -H "Content-Type: application/json" \\
  -d '{
    "text1": "The International Space Station orbits Earth.",
    "text2": "A space station is circling our planet."
  }'
'''
    print(curl_example)
    
    health_curl = '''curl -X GET http://localhost:5000/health
'''
    print(health_curl)

if __name__ == "__main__":
    test_api()
    test_api_with_curl_examples()