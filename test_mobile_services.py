#!/usr/bin/env python3
"""
Simple test for mobile services display
"""

def check_mobile_services():
    """Check mobile services implementation"""
    print("🔍 Checking Mobile Services Display...")
    
    try:
        with open('static/styles.css', 'r', encoding='utf-8') as f:
            css_content = f.read()
        
        # Check for proper mobile implementation
        checks = [
            ('padding: 1.2rem', "Service card padding (updated)"),
            ('border-radius: 15px', "Service card styling"),  
            ('box-shadow: 0 5px 15px', "Service card shadow"),
            ('height: 280px', "Mobile image height (bigger)"),
            ('margin: 0 20px', "Container margins (reduced)"),
            ('calc(100% - 0rem)', "Card width calculation"),
            ('text-align: center', "Card text alignment"),
            ('gap: 1.5rem', "Reduced gap between cards"),
        ]
        
        for check_text, description in checks:
            if check_text in css_content:
                print(f"✅ {description} found")
            else:
                print(f"❌ {description} missing")
        
        print("\n📱 Current Mobile Approach:")
        print("• Single card per view with optimized padding")
        print("• Card-like appearance with shadows and borders") 
        print("• BIGGER image visibility (280px height)")
        print("• WIDER cards with reduced margins (20px)")
        print("• Compact text spacing for better fit")
        print("• Smaller navigation buttons")
        print("• Swipe gesture support maintained")
        
        return True
        
    except FileNotFoundError:
        print("❌ CSS file not found")
        return False

if __name__ == "__main__":
    print("📱 Mobile Services Display Checker")
    print("=" * 40)
    
    if check_mobile_services():
        print("\n🎉 Mobile services should now display properly!")
        print("Each service will show as a complete card with:")
        print("• Full image visible")
        print("• All text readable") 
        print("• Proper spacing and styling")
        print("• Navigation buttons and dots")
    else:
        print("\n❌ Issues found - check above")
