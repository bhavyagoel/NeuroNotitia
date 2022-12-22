import streamlit as st
import cv2
from deep_privacy.build import build_anonymizer
import tempfile
from moviepy.editor import *
from PIL import Image


def vd_face_anonymise():
    frame_rate = st.number_input("Enter the Frame Rate", step = 1)
    anonymizer, cfg = build_anonymizer(return_cfg=True)
    vid = st.file_uploader("Upload a Video", type=["mp4"])
    
    
    if vid:
        tfile = tempfile.NamedTemporaryFile(delete=False)
        tfile.write(vid.read())
        vf = VideoFileClip(tfile.name)
        new_clip = vf.set_fps(frame_rate)
        frames =  new_clip.iter_frames()

        i = 0
        for frame in frames:
            im = Image.fromarray(frame)
            im.save("temp/orig_{}.jpeg".format(i))
            frame = frame[:, :, ::-1]
            frame = anonymizer.detect_and_anonymize_images([frame])[0]
            frame = frame[:, :, ::-1]
            im = Image.fromarray(frame)
            im.save("temp/anony_{}.jpeg".format(i))
            i += 1
        
        frame = cv2.imread("temp/orig_0.jpeg")
        height, width, layers = frame.shape
        fourcc = cv2.VideoWriter_fourcc(*'VP90')
        orig = cv2.VideoWriter('temp/orig.webm',fourcc, 1, (width, height)) 
        anony = cv2.VideoWriter('temp/anony.webm',fourcc, 1, (width, height)) 
        
        for j in range(0, i):
            orig.write(cv2.imread("temp/orig_"+str(j)+".jpeg"))
            os.remove("temp/orig_"+str(j)+".jpeg")
            anony.write(cv2.imread("temp/anony_"+str(j)+".jpeg"))
            os.remove("temp/anony_"+str(j)+".jpeg")
        
        cv2.destroyAllWindows()
        orig.release()
        anony.release()
        st.video("temp/orig.webm")     
        st.video("temp/anony.webm")