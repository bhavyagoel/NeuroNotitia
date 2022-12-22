import streamlit as st
import cv2
import tempfile
from PIL import Image
from moviepy.editor import *

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


def vd_num_plate():
    frame_rate = st.number_input("Enter the Frame Rate", step = 1)
    vid = st.file_uploader("Upload a Video", type=["mp4"])

    if vid:
        tfile = tempfile.NamedTemporaryFile(delete=False)
        tfile.write(vid.read())
        vf = VideoFileClip(tfile.name)
        if (frame_rate != 0): 
            vf = vf.set_fps(frame_rate)
        frames =  vf.iter_frames()
        
        i = 0 
        height, width, layers = 0, 0, 0
        for frame in frames:
            height, width, layers = frame.shape
            break
        
        fourcc = cv2.VideoWriter_fourcc(*'VP90')
        blurred = cv2.VideoWriter('temp/num_blurred.webm',fourcc, 1, (width, height)) 
        
        for frame in frames:
            im = Image.fromarray(frame)
            im.save("temp/blur_.jpeg")
            img = detect_plate(cv2.imread("temp/blur_.jpeg"))
            blurred.write(img)
        
        cv2.destroyAllWindows()
        blurred.release()
        st.video("temp/num_blurred.webm")