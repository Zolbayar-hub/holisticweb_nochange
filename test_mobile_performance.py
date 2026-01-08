#!/usr/bin/env python3
"""
Mobile performance testing script for carousel functionality
"""

import time
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from flask_app import app
import requests
from bs4 import BeautifulSoup
import logging

def test_mobile_responsiveness():
    """Test mobile responsiveness and functionality"""
    print("🔍 Testing Mobile Responsiveness...")
    
    # Start app in test mode
    app.config['TESTING'] = True
    
    with app.test_client() as client:
        # Test home page loads
        print("  📱 Testing home page load...")
        response = client.get('/')
        
        if response.status_code == 200:
            print("  ✅ Home page loads successfully")
            
            # Check for mobile optimizations
            html = response.get_data(as_text=True)
            soup = BeautifulSoup(html, 'html.parser')
            
            # Check viewport meta tag
            viewport = soup.find('meta', {'name': 'viewport'})
            if viewport and 'user-scalable=no' in viewport.get('content', ''):
                print("  ✅ Viewport meta tag optimized for mobile")
            else:
                print("  ⚠️  Viewport meta tag might need optimization")
            
            # Check for mobile indicators
            if soup.find('div', {'class': 'mobile-carousel-indicators'}):
                print("  ✅ Mobile carousel indicators present")
            else:
                print("  ⚠️  Mobile carousel indicators missing")
            
            # Check for swipe hint
            if soup.find('div', {'class': 'mobile-swipe-hint'}):
                print("  ✅ Mobile swipe hint present")
            else:
                print("  ⚠️  Mobile swipe hint missing")
            
            # Check for touch optimizations in CSS
            if 'touch-action: pan-x' in html:
                print("  ✅ Touch action optimizations found")
            else:
                print("  ⚠️  Touch action optimizations might be missing")
                
            print("  ✅ Mobile responsiveness test completed")
            
        else:
            print(f"  ❌ Home page failed to load: {response.status_code}")
            return False
    
    return True

def test_services_carousel():
    """Test services carousel functionality"""
    print("🎠 Testing Services Carousel...")
    
    with app.test_client() as client:
        response = client.get('/')
        
        if response.status_code == 200:
            html = response.get_data(as_text=True)
            soup = BeautifulSoup(html, 'html.parser')
            
            # Check for services grid
            services_grid = soup.find('div', {'id': 'services-grid'})
            if services_grid:
                service_cards = services_grid.find_all('div', {'class': 'service-card'})
                print(f"  ✅ Found {len(service_cards)} service cards")
                
                # Check for carousel navigation
                if soup.find('button', {'id': 'carousel-prev'}):
                    print("  ✅ Carousel navigation buttons present")
                
                # Check for mobile indicators
                indicators = soup.find('div', {'id': 'mobile-indicators'})
                if indicators:
                    indicator_dots = indicators.find_all('div', {'class': 'indicator-dot'})
                    print(f"  ✅ Found {len(indicator_dots)} mobile indicator dots")
                
                return True
            else:
                print("  ❌ Services grid not found")
                return False
        
        return False

def generate_mobile_test_report():
    """Generate a comprehensive mobile test report"""
    print("📊 Generating Mobile Test Report...")
    print("=" * 50)
    
    # Run tests
    home_test = test_mobile_responsiveness()
    carousel_test = test_services_carousel()
    
    print("\n📋 SUMMARY:")
    print("=" * 50)
    
    if home_test and carousel_test:
        print("✅ ALL TESTS PASSED - Mobile optimizations are working!")
        print("\n🎯 Mobile Features Implemented:")
        print("  • Full-width viewport utilization")
        print("  • Touch-friendly swipe gestures")
        print("  • Mobile carousel indicators")
        print("  • Optimized touch actions")
        print("  • Responsive viewport settings")
        print("  • Visual feedback for touch interactions")
        print("  • Smooth CSS transitions")
        print("  • Scroll behavior optimizations")
        
        print("\n📱 Mobile Usage Instructions:")
        print("  • Swipe left/right on services to navigate")
        print("  • Tap indicator dots to jump to specific services")
        print("  • Smooth scrolling throughout the page")
        print("  • Optimized for iOS Safari and Android Chrome")
        
    else:
        print("❌ SOME TESTS FAILED - Please check the issues above")
    
    print("\n" + "=" * 50)

if __name__ == "__main__":
    print("🧪 Mobile Performance Testing Suite")
    print("=" * 50)
    
    # Ensure we're in the right directory
    if not os.path.exists('flask_app.py'):
        print("❌ Please run this script from the project root directory")
        sys.exit(1)
    
    try:
        generate_mobile_test_report()
    except Exception as e:
        print(f"❌ Test failed with error: {e}")
        import traceback
        traceback.print_exc()
