from privyfilter.privyfilter import Privyfilter as pf
import streamlit as st
import cv2
import numpy as np
from PIL import Image


def im_face_blur():
    img = st.camera_input("Take a Picture")

    if img is not None:
        bytes_data = img.getvalue()
        img = cv2.imdecode(np.frombuffer(
            bytes_data, np.uint8), cv2.IMREAD_COLOR)
        
        im = Image.fromarray(img)
        im.save("temp/blur_.jpeg")
        faces2, img1 = pf.faceScrub("temp/blur_.jpeg")
        img2 = pf.RemoveMetaData("temp/blur_.jpeg")
        
        st.image(img1)
        st.image(img2)