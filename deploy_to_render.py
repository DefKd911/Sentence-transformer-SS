"""
Deploy to Render - Quick Setup Script
This script helps you prepare for Render deployment
"""

import os
import subprocess
import sys

def check_files():
    """Check if all required files exist"""
    required_files = [
        'app.py',
        'requirements_deploy.txt',
        'render.yaml',
        'templates/index.html',
        'DataNeuron_Text_Similarity.csv'
    ]
    
    print("Checking required files...")
    missing_files = []
    
    for file in required_files:
        if os.path.exists(file):
            print(f"✅ {file}")
        else:
            print(f"❌ {file} - MISSING")
            missing_files.append(file)
    
    if missing_files:
        print(f"\n❌ Missing files: {missing_files}")
        return False
    else:
        print("\n✅ All required files present!")
        return True

def check_git():
    """Check if git is initialized"""
    if os.path.exists('.git'):
        print("✅ Git repository initialized")
        return True
    else:
        print("❌ Git not initialized")
        return False

def init_git():
    """Initialize git repository"""
    try:
        subprocess.run(['git', 'init'], check=True)
        subprocess.run(['git', 'add', '.'], check=True)
        subprocess.run(['git', 'commit', '-m', 'Initial commit for Render deployment'], check=True)
        print("✅ Git initialized and files committed")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Git initialization failed: {e}")
        return False

def main():
    """Main deployment preparation"""
    print("🚀 Render Deployment Preparation")
    print("=" * 40)
    
    # Check files
    if not check_files():
        print("\n❌ Cannot proceed - missing required files")
        return
    
    # Check git
    if not check_git():
        print("\n📝 Initializing Git repository...")
        if not init_git():
            print("❌ Git initialization failed")
            return
    
    print("\n✅ Ready for Render deployment!")
    print("\n📋 Next steps:")
    print("1. Go to https://render.com")
    print("2. Sign up with GitHub")
    print("3. Click 'New +' → 'Web Service'")
    print("4. Connect your GitHub repository")
    print("5. Configure:")
    print("   - Name: semantic-similarity-api")
    print("   - Environment: Python 3")
    print("   - Build Command: pip install -r requirements_deploy.txt")
    print("   - Start Command: gunicorn app:app")
    print("   - Python Version: 3.10.0")
    print("6. Click 'Create Web Service'")
    print("7. Wait for deployment (5-10 minutes)")
    print("8. Get your URL: https://your-app-name.onrender.com")
    
    print("\n🧪 Test your deployment:")
    print("python test_render.py")
    print("# Enter your Render URL when prompted")

if __name__ == "__main__":
    main()
