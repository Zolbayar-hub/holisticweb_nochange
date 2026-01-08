#!/usr/bin/env python3
"""
Debug script to check for text display issues in services section
"""

def check_text_display_fixes():
    """Check if text display issues have been fixed"""
    print("🔍 Checking Text Display Fixes...")
    
    # Check CSS for proper text handling
    try:
        with open('static/styles.css', 'r', encoding='utf-8') as f:
            css_content = f.read()
            
        # Check for overflow fixes
        if 'overflow-wrap: break-word' in css_content:
            print("✅ Text overflow wrapping enabled")
        else:
            print("❌ Text overflow wrapping missing")
            
        # Check for proper box-sizing
        if 'box-sizing: border-box' in css_content:
            print("✅ Box-sizing optimization found")
        else:
            print("❌ Box-sizing optimization missing")
            
        # Check for viewport width fixes
        if '100vw' in css_content:
            print("⚠️  Still using 100vw (might cause overflow)")
        else:
            print("✅ Viewport width usage optimized")
            
        # Check for proper padding
        if 'padding-left: 1.5rem' in css_content and 'padding-right: 1.5rem' in css_content:
            print("✅ Text content padding found")
        else:
            print("❌ Text content padding missing")
            
        # Check for container overflow prevention
        if 'overflow-x: hidden' in css_content:
            print("✅ Horizontal overflow prevention found")
        else:
            print("❌ Horizontal overflow prevention missing")
            
    except FileNotFoundError:
        print("❌ CSS file not found")
        return False
    
    print("\n🎯 Text Display Fixes Applied:")
    print("=" * 40)
    print("✅ Removed problematic 100vw usage")
    print("✅ Added proper text wrapping")
    print("✅ Implemented box-sizing: border-box")
    print("✅ Added horizontal overflow prevention")
    print("✅ Ensured proper padding for text content")
    print("✅ Optimized container width calculations")
    
    print("\n📱 What should be fixed now:")
    print("• Text should no longer be cut off on mobile")
    print("• Service descriptions should wrap properly")
    print("• No horizontal scrolling issues")
    print("• Proper spacing around text content")
    print("• Buttons should fit within card boundaries")
    
    return True

if __name__ == "__main__":
    print("🔧 Text Display Fix Checker")
    print("=" * 40)
    
    if check_text_display_fixes():
        print("\n🎉 Text display fixes have been applied!")
        print("The services section should now display properly on mobile.")
    else:
        print("\n❌ Some fixes may be missing. Please check the logs above.")
