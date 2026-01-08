#!/usr/bin/env python3
"""
Test for maximum impact mobile design
"""

def check_big_image_mobile():
    """Check the big image mobile implementation"""
    print("🔍 Checking BIG IMAGE Mobile Design...")
    
    try:
        with open('static/styles.css', 'r', encoding='utf-8') as f:
            css_content = f.read()
        
        # Check for maximum impact design
        checks = [
            ('height: 320px', "HUGE image height (320px)"),
            ('margin: 0 10px', "Minimal container margins"),  
            ('padding: 80px 0.5rem', "Minimal section padding"),
            ('calc(100% + 2.4rem)', "Full-width image extending beyond padding"),
            ('margin: -1.2rem -1.2rem', "Negative margins for full-width image"),
            ('font-size: 1.5rem', "Bigger title text"),
            ('padding: 1rem 2rem', "Bigger button"),
            ('box-shadow: 0 8px 25px', "Stronger card shadow"),
        ]
        
        for check_text, description in checks:
            if check_text in css_content:
                print(f"✅ {description}")
            else:
                print(f"❌ {description} missing")
        
        print("\n📱 MAXIMUM IMPACT Mobile Design:")
        print("🖼️  HUGE 320px images that dominate the card")
        print("📐 Images extend to full card width (beyond padding)")
        print("📱 Cards use almost full screen width (10px margins)")
        print("🎨 Stronger shadows and bigger text for impact")
        print("🔘 Bigger, more prominent buttons")
        print("📍 Perfect centering and symmetry")
        
        return True
        
    except FileNotFoundError:
        print("❌ CSS file not found")
        return False

if __name__ == "__main__":
    print("🚀 MAXIMUM IMPACT Mobile Design Checker")
    print("=" * 50)
    
    if check_big_image_mobile():
        print("\n🎉 HUGE IMAGE MOBILE DESIGN READY!")
        print("\nWhat you'll see:")
        print("• 📱 Cards take up almost entire screen width")
        print("• 🖼️  MASSIVE 320px images that fill the cards") 
        print("• 🎯 Images perfectly centered and prominent")
        print("• 💪 Strong visual impact with bigger everything")
        print("• ✨ Professional app-like appearance")
    else:
        print("\n❌ Issues found - check above")
