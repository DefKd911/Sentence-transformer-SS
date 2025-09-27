"""
Git Setup Script for Render Deployment
This script handles the Git operations needed for deployment
"""

import subprocess
import sys
import os

def run_command(command, description):
    """Run a Git command and handle errors"""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ {description} completed")
            if result.stdout.strip():
                print(f"   Output: {result.stdout.strip()}")
        else:
            print(f"❌ {description} failed")
            print(f"   Error: {result.stderr.strip()}")
            return False
        return True
    except Exception as e:
        print(f"❌ {description} failed: {e}")
        return False

def main():
    """Main Git setup process"""
    print("🚀 Git Setup for Render Deployment")
    print("=" * 40)
    
    # Step 1: Add all files
    if not run_command("git add .", "Adding all files"):
        return False
    
    # Step 2: Commit files
    if not run_command('git commit -m "Initial commit for Render deployment"', "Committing files"):
        return False
    
    # Step 3: Check if remote exists
    result = subprocess.run("git remote -v", shell=True, capture_output=True, text=True)
    if "origin" not in result.stdout:
        print("⚠️  No remote repository found.")
        print("   Please add your GitHub repository:")
        print("   git remote add origin https://github.com/yourusername/your-repo-name.git")
        return False
    
    # Step 4: Push to GitHub
    if not run_command("git push -u origin main", "Pushing to GitHub"):
        return False
    
    print("\n✅ Git setup completed successfully!")
    print("🎯 Ready for Render deployment!")
    print("\n📋 Next steps:")
    print("1. Go to https://render.com")
    print("2. Sign up with GitHub")
    print("3. Click 'New +' → 'Web Service'")
    print("4. Connect your GitHub repository")
    print("5. Configure and deploy!")
    
    return True

if __name__ == "__main__":
    main()
