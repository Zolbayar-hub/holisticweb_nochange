# QR Code Directory

## Google Review QR Code Setup

To add your Google QR code to the website:

1. **Get your Google QR Code:**
   - Go to your Google Business Profile
   - Click on "Get more reviews"
   - Generate or download your review QR code
   - OR create a QR code that links to your Google Business Profile review page

2. **Upload the QR Code:**
   - Save your QR code image as `google-review-qr.png`
   - Place it in this directory: `/static/images/qr-codes/`
   - Recommended size: 300x300 pixels or larger (square format)
   - Supported formats: PNG, JPG, or SVG

3. **QR Code Placement:**
   - The QR code appears in the Contact section of your homepage
   - It's styled with a hover effect and mobile-responsive design
   - Includes instructional text for users

## Alternative QR Code Options

You can also use this section for:
- Google Maps location QR code
- WhatsApp contact QR code  
- Website URL QR code
- Social media profile QR code

Simply replace the image file and update the text in the template if needed.

## Technical Details

- File path: `static/images/qr-codes/google-review-qr.png`
- CSS class: `.google-qr-code`
- Template location: `templates/home.html` (Contact section)
- Fallback: Shows placeholder text if image is missing
