import streamlit as st
import cv2
import tempfile
import os


plate_cascade =cv2.CascadeClassifier("/home/bhavyagoel/.zi/plugins/pyenv---pyenv/versions/data_privacy/lib/python3.8/site-packages/cv2/data/haarcascade_indian_plate_number.xml")

def detect_plate(img): 
    plate_img = img.copy()
    roi = img.copy()
    plate_rect = plate_cascade.detectMultiScale(plate_img, 1.2)
    for (x,y,w,h) in plate_rect:
        roi_ = roi[y:y+h, x:x+w, :]
        blurred_roi = cv2.blur(roi_, ksize=(16,16)) 
        plate_img[y:y+h, x:x+w, :] = blurred_roi

        cv2.rectangle(plate_img, (x,y), (x+w, y+h), (51,51,255), 3)
        
    return plate_img


def im_num_plate():
    img = st.file_uploader("Upload a Photo", type=["jpg"])


    if img:
        tfile = tempfile.NamedTemporaryFile(delete=False)
        tfile.write(img.read())
        img = cv2.imread(tfile.name)
        st.image(img)
        img = detect_plate(img)
        st.image(img)
        