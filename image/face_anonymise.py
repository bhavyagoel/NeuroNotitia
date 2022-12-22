import streamlit as st
import cv2
import numpy as np
from deep_privacy.build import build_anonymizer


anonymizer, cfg = build_anonymizer(return_cfg=True)

def im_face_anonymise():
    img = st.camera_input("Take a Picture")

    if img is not None:
        bytes_data = img.getvalue()
        img = cv2.imdecode(np.frombuffer(
            bytes_data, np.uint8), cv2.IMREAD_COLOR)
        width = 1280
        height = 720
        img = cv2.resize(img, (width, height))
        img = img[:, :, ::-1]
        img = anonymizer.detect_and_anonymize_images([img])[0]
        st.write("Anonymised Image")
        st.image(img)
