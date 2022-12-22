# Create a basic webrtc application using streamlit
import streamlit as st
from PIL import Image
from video.face_anonymise import vd_face_anonymise
from image.face_anonymise import im_face_anonymise
from image.face_blur import im_face_blur
from video.face_blur import vd_face_blur
from image. num_plate_blur import im_num_plate
from video.num_plate_blur import vd_num_plate

def main():
    image = Image.open("static/priv.jpg")
    logo = Image.open("static/icon.png")
    st.set_page_config(page_title="Anonymising Images", page_icon=logo)

    st.image(image)
    st.title("Anonymising Images")

    st.sidebar.title("Methods for Anonymisation")


    im_conv = st.sidebar.selectbox(
        "Image Conversion", options=["Home", "Face Anonymise", "Face Blur", "Number Plate Blur"]
    )
    if im_conv == "Face Anonymise":
        im_face_anonymise()
    elif im_conv == "Face Blur":
        im_face_blur()
    elif im_conv == "Number Plate Blur":
        im_num_plate()

    # st.sidebar.markdown("On-Demand Conversion")
    vd_conv = st.sidebar.selectbox(
        "Video Conversion", options=["Home", "Face Anonymise", "Face Blur", "Number Plate Blur"]
    )
    
    if vd_conv == "Face Anonymise":
        vd_face_anonymise()
    elif vd_conv == "Face Blur":
        vd_face_blur()
    elif vd_conv == "Number Plate Blur":
            vd_num_plate()

if __name__ == "__main__":
    main()
