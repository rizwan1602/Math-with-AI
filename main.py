import cvzone
import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np
import google.generativeai as genai
import os
from PIL import Image
import streamlit as st

st.set_page_config(page_title="AI Whiteboard", page_icon="🎨", layout="wide")

col1 , col2 = st.columns([2,1])

with col1:
    run = st.checkbox("Run", value=True)
    FRAME_WINDOW = st.image([])


with col2:
    st.title("Answer")
    output_text_area = st.subheader("")



genai.configure(api_key=os.environ.get("AI_KEY"))
model = genai.GenerativeModel('gemini-1.5-flash')




cap = cv2.VideoCapture(0)
# cap.set(propId=3, value=1240)
# cap.set(propId=4, value=720)
detector = HandDetector(staticMode=False, maxHands=1, modelComplexity=1, detectionCon=0.7, minTrackCon=0.5)

def gethandinfo(img):
    hands, img = detector.findHands(img, draw=False, flipType=True)
    if hands:
        hand1 = hands[0]  
        lmList = hand1["lmList"] 
        bbox1 = hand1["bbox"]  
        center1 = hand1['center']  
        handType1 = hand1["type"] 
        fingers = detector.fingersUp(hand1)
        return fingers , lmList

def draw(info, prev_pos, canvas):
    fingers, lmList = info
    current_pos = None
    if fingers== [0,1,0,0,0]:
        current_pos = lmList[8][0:2]
        if prev_pos is None: prev_pos = current_pos
        cv2.line(canvas, current_pos, prev_pos, (255,0,255), thickness=10)
    elif fingers == [0,1,1,1,1]:
        canvas.fill(0)

    return current_pos  

def sendtoAI(model, canvas,fingers):
    if fingers == [1,1,1,1,1]:
        pil_image = Image.fromarray(canvas)
        response = model.generate_content(["solve this problem", pil_image])
        return response.text



prev_pos = None
canvas = None
image_combined = None
output_text = ""
while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    if canvas is None:
        canvas = np.zeros_like(img)
        image_combined = img.copy()

    info = gethandinfo(img)
    if info:
        fingers, lmList = info
        prev_pos= draw(info, prev_pos, canvas)
        output_text = sendtoAI(model, canvas, fingers)


    image_combined = cv2.addWeighted(img, 0.7, canvas, 0.3, 0)
    FRAME_WINDOW.image(image_combined, channels="BGR")
    if output_text:
        output_text_area.text(output_text)

    cv2.waitKey(1)



        

    