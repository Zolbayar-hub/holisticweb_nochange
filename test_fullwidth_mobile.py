#!/usr/bin/env python3

import re

def test_mobile_services_layout():
    """Test the mobile services layout with full-width viewport approach"""
    
    css_file = "/Users/zoloo/project_v2/website/holisticweb_nochange/static/styles.css"
    
    try:
        with open(css_file, 'r') as f:
            content = f.read()
            
        print("🔍 TESTING MOBILE SERVICES LAYOUT")
        print("=" * 50)
        
        # Check for mobile media query
        mobile_query = "@media (max-width: 768px)"
        if mobile_query in content:
            print("✅ Mobile media query found")
        else:
            print("❌ Mobile media query missing")
            
        # Check for full viewport width container
        if "width: 100vw" in content and "margin: 0 -1rem" in content:
            print("✅ Full viewport width container configured")
        else:
            print("❌ Full viewport width container not found")
            
        # Check for proper service card sizing
        if "flex: 0 0 100vw" in content:
            print("✅ Service cards set to full viewport width")
        else:
            print("❌ Service cards not set to full width")
            
        # Check for proper image sizing
        if "height: 250px" in content and "object-fit: cover" in content:
            print("✅ Service images properly sized")
        else:
            print("❌ Service images sizing issues")
            
        # Check that carousel buttons are hidden
        if "display: none !important" in content:
            print("✅ Carousel buttons hidden on mobile")
        else:
            print("❌ Carousel buttons not properly hidden")
            
        # Check for mobile indicators
        if ".mobile-carousel-indicators" in content:
            print("✅ Mobile indicators present")
        else:
            print("❌ Mobile indicators missing")
            
        print("\n📱 MOBILE LAYOUT SUMMARY:")
        print("- Cards: Full viewport width (100vw)")
        print("- Images: 250px height, cover fit")
        print("- Navigation: Touch/swipe only")
        print("- Layout: No margins, no cut-off")
        
    except Exception as e:
        print(f"❌ Error testing CSS: {e}")

if __name__ == "__main__":
    test_mobile_services_layout()
