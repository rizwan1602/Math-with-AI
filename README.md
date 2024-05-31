Steps to run 
# AI Whiteboard

AI Whiteboard is a Python application that uses computer vision and AI to interpret hand-drawn images on a virtual whiteboard and generate detailed explanations of complex mathematical problems.

## Dependencies

The application uses the following libraries:

- cvzone
- cv2
- HandTrackingModule from cvzone
- numpy
- google.generativeai
- os
- PIL
- streamlit

## Setup

1. Clone the repository to your local machine.
2. Create a virtual environment: `python -m venv env`
3. Activate the virtual environment: `.\env\Scripts\activate` (Windows) or `source env/bin/activate` (Linux/Mac)
4. Install the required dependencies: `pip install -r requirements.txt`
5. Set your Google Generative AI API key as an environment variable: `$env:AI_KEY="your_api_key`"
`
6. Run the application: `streamlit run main.py`

## Usage

The application opens a Streamlit interface with two columns. The left column contains a checkbox to start the application and a window that displays the video feed from your webcam. The right column displays the AI-generated explanation of the mathematical problem.

The application uses hand tracking to allow you to draw on the virtual whiteboard. The drawn image is then sent to the Google Generative AI model, which generates a detailed explanation of the mathematical problem.

## Note

This application is a proof of concept and is not intended for use in a production environment.