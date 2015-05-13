# quartirs
6.857 Final Project: QR-based User Authentication Replacement for Traditional Identification Reference System

How to use the application:
- In order to generate a QR code, you can go to jennya.scripts.mit.edu/6857/quartirs_app. You must have MIT certificates and be using a browser that supports certificates. 
- In order to see the list of people who have checked in with you, you can go to jennya.scripts.mit.edu/6857/quartirs_app/checkins. This site also requires MIT certificates.
- You can test out scanning a QR code by installing our Android app (which is the most secure way of scanning the codes, since it checks that it is redirecting you to our domain) or by scanning the code presented with any QR scanner. MIT Certificates must be installed on your mobile device and your mobile browser must support them. In order to test checking in, you can also inspect the QR code image on the page and go to the URL in your browser. This allows you to test only on the computer and does not require a mobile device.
- The Android application apk is located in the QuartirsAndroid folder and can be installed directly to an Android device. Code extends the QR code library implemented at http://sourceforge.net/p/zbar/news/.

Where the code is stored:
- Android App: QuartirsAndroid folder
- Django Web server: quartirs folder
