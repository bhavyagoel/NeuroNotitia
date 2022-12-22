from cv2 import blur
from privyfilter.privyfilter import Privyfilter as pf
import streamlit as st
import cv2
import numpy as np
from PIL import Image
from moviepy.editor import *
import tempfile



def vd_face_blur():
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
        blurred = cv2.VideoWriter('temp/blurred.webm',fourcc, 1, (width, height)) 
        
        for frame in frames:
            im = Image.fromarray(frame)
            im.save("temp/blur_.jpeg")
            faces2, img1 = pf.faceScrub("temp/blur_.jpeg")
            
            img1 = Image.fromarray(img1)
            img1.save("temp/blur_temp.jpeg")
            blurred.write(cv2.imread("temp/blur_temp.jpeg"))
        
        cv2.destroyAllWindows()
        blurred.release()
        st.video("temp/blurred.webm")
