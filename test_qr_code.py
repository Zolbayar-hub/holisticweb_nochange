#!/usr/bin/env python3
"""
Quick test to verify QR code implementation
"""

import os
from flask_app import app

def test_qr_code():
    # Check if QR code file exists
    qr_path = os.path.join(app.static_folder, 'images', 'qr-codes', 'google-review-qr.png')
    print(f"Checking QR code file: {qr_path}")
    
    if os.path.exists(qr_path):
        file_size = os.path.getsize(qr_path)
        print(f"✅ QR code file found! Size: {file_size} bytes")
        
        # Check if file is readable
        try:
            with open(qr_path, 'rb') as f:
                header = f.read(8)
                if header.startswith(b'\x89PNG'):
                    print("✅ Valid PNG file detected")
                else:
                    print("⚠️ File might not be a valid PNG")
        except Exception as e:
            print(f"❌ Error reading file: {e}")
            
    else:
        print("❌ QR code file not found!")
        print(f"Looking in: {qr_path}")
        
        # Check directory
        qr_dir = os.path.dirname(qr_path)
        if os.path.exists(qr_dir):
            print(f"Directory exists, contents: {os.listdir(qr_dir)}")
        else:
            print("Directory doesn't exist!")

if __name__ == '__main__':
    with app.app_context():
        test_qr_code()
        
    print("\nStarting Flask server...")
    print("🌐 Visit: http://127.0.0.1:5000")
    print("📱 Look for QR code in the Contact section")
    print("Press Ctrl+C to stop")
    
    app.run(host='127.0.0.1', port=5000, debug=True)
