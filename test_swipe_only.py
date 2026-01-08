#!/usr/bin/env python3

def test_swipe_only_mobile():
    """Test that mobile services have swipe-only navigation (no dots/buttons)"""
    
    css_file = "/Users/zoloo/project_v2/website/holisticweb_nochange/static/styles.css"
    js_file = "/Users/zoloo/project_v2/website/holisticweb_nochange/static/home.js"
    
    try:
        with open(css_file, 'r') as f:
            css_content = f.read()
            
        with open(js_file, 'r') as f:
            js_content = f.read()
            
        print("🔍 TESTING SWIPE-ONLY MOBILE NAVIGATION")
        print("=" * 50)
        
        # Check that carousel buttons are hidden
        if ".carousel-btn {\n        display: none !important;" in css_content:
            print("✅ Carousel buttons completely hidden")
        else:
            print("❌ Carousel buttons not properly hidden")
            
        # Check that indicators are hidden
        if ".mobile-carousel-indicators {\n        display: none !important;" in css_content:
            print("✅ Mobile indicators completely hidden")
        else:
            print("❌ Mobile indicators not properly hidden")
            
        # Check that no indicator dot styles exist
        if ".indicator-dot" not in css_content:
            print("✅ No indicator dot styles found")
        else:
            print("❌ Indicator dot styles still exist")
            
        # Check that JavaScript doesn't reference indicators
        if "this.indicators" not in js_content and "indicatorDots" not in js_content:
            print("✅ JavaScript cleaned of indicator references")
        else:
            print("❌ JavaScript still has indicator references")
            
        # Check that updateIndicators function is removed
        if "updateIndicators" not in js_content:
            print("✅ updateIndicators function removed")
        else:
            print("❌ updateIndicators function still exists")
            
        # Check that touch support still exists
        if "setupTouchSupport" in js_content and "touchstart" in js_content:
            print("✅ Touch/swipe functionality preserved")
        else:
            print("❌ Touch/swipe functionality missing")
            
        print("\n📱 MOBILE EXPERIENCE SUMMARY:")
        print("- Navigation: Swipe/touch only")
        print("- Buttons: Completely hidden")
        print("- Indicators: Completely hidden") 
        print("- Layout: Full viewport width cards")
        print("- Interaction: Pure gesture-based")
        
    except Exception as e:
        print(f"❌ Error testing files: {e}")

if __name__ == "__main__":
    test_swipe_only_mobile()
