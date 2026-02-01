#!/usr/bin/env python3
"""
Quick QR Code Test Script
Run this to start the server and test your QR code
"""

import os
import sys
from flask_app import app

def main():
    print("🧪 QR Code Implementation Test")
    print("=" * 50)
    
    # Check if QR code file exists
    qr_path = os.path.join(app.static_folder, 'images', 'qr-codes', 'google-review-qr.png')
    if os.path.exists(qr_path):
        file_size = os.path.getsize(qr_path)
        print(f"✅ QR code file found: {file_size} bytes")
    else:
        print("❌ QR code file not found!")
        return
    
    print("\n🌐 Starting Flask server...")
    print("📍 Visit these URLs to test:")
    print("   • Main site: http://127.0.0.1:5000/")
    print("   • QR test page: http://127.0.0.1:5000/qr-test")
    print("   • Direct image: http://127.0.0.1:5000/static/images/qr-codes/google-review-qr.png")
    print("   • File status: http://127.0.0.1:5000/test-qr-direct")
    print("\n📱 Your QR code contains: https://g.page/r/CfJVDfj9QwsaEBM/")
    print("=" * 50)
    print("Press Ctrl+C to stop the server")
    print()
    
    # Start the Flask server
    app.run(host='127.0.0.1', port=5000, debug=True)

if __name__ == '__main__':
    main()
