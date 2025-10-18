#!/usr/bin/env python3
"""
Simple script to run the University Knowledge Base Flask application
"""

import os
import sys
import subprocess

def main():
    print("🚀 Starting University Knowledge Base for Parents")
    print("=" * 50)

    # Check if data is ingested
    if not os.path.exists("faiss_index"):
        print("❌ FAISS index not found. Please run ingest_data.py first.")
        print("Run: python ingest_data.py")
        sys.exit(1)

    # Check if .env file exists
    if not os.path.exists(".env"):
        print("⚠️  .env file not found. Creating template...")
        with open(".env", "w") as f:
            f.write("GOOGLE_API_KEY=your_google_api_key_here\n")
        print("Please add your Google API key to .env file")
        sys.exit(1)

    # Start Flask app
    print("🌐 Starting Flask server on http://localhost:5000")
    print("Press Ctrl+C to stop the server")
    print("=" * 50)

    try:
        subprocess.run([sys.executable, "app.py"], check=True)
    except KeyboardInterrupt:
        print("\n👋 Server stopped by user")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error starting server: {e}")

if __name__ == "__main__":
    main()
