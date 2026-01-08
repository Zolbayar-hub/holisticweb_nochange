#!/usr/bin/env python3

import subprocess
import sys
import os
import time

def start_server_and_test():
    """Start the Flask server and provide testing instructions"""
    
    print("🚀 STARTING SERVER FOR MOBILE TESTING")
    print("=" * 50)
    
    # Change to the correct directory
    os.chdir("/Users/zoloo/project_v2/website/holisticweb_nochange")
    
    print("\n📋 TESTING CHECKLIST:")
    print("1. ✅ Full viewport width cards (100vw)")
    print("2. ✅ No horizontal scrolling")
    print("3. ✅ Images fully visible (250px height)")
    print("4. ✅ Touch/swipe navigation only")
    print("5. ✅ No cut-off content")
    print("6. ✅ Centered indicators")
    print("7. ✅ Premium app-like experience")
    
    print("\n🔧 RECENT CHANGES:")
    print("- Services container: 100vw width, extends beyond padding")
    print("- Service cards: Full viewport width, no margins")
    print("- Images: 250px height, cover fit, no crop")
    print("- Navigation: Hidden buttons, swipe-only on mobile")
    print("- Text: Centered with proper padding")
    
    print("\n📱 MOBILE TESTING INSTRUCTIONS:")
    print("1. Open the website on your mobile device")
    print("2. Navigate to the Services section")
    print("3. Verify cards fill the entire screen width")
    print("4. Check that images are fully visible")
    print("5. Test swipe navigation between services")
    print("6. Confirm no content is cut off")
    
    print("\n🌐 Starting server...")
    
    try:
        # Start the Flask server
        subprocess.run([sys.executable, "start_app.py"], check=True)
    except KeyboardInterrupt:
        print("\n⏹️  Server stopped by user")
    except Exception as e:
        print(f"❌ Server error: {e}")
        print("\n🔄 Try running manually:")
        print("cd /Users/zoloo/project_v2/website/holisticweb_nochange")
        print("python start_app.py")

if __name__ == "__main__":
    start_server_and_test()
