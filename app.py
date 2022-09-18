""" 
author : Sanketh Gadadinni
Date :   16 Sept 2022
file name : main.py

The file creates a streamlit app for brand detection from images

Requirements:

python == 3.8
azure-cognitiveservices-vision-computervision==0.9.0
streamlit==1.12.2
 
"""


import streamlit as st
import os
from PIL import Image, ImageOps
from detect import brand_detect


@st.cache
def load_image(image_file):
	img = Image.open(image_file)
	return img 

def main():
    
    st.title("Brand Mentions In Images")
        
    image_file = st.file_uploader("Upload URL of Image", type=['jpg','png','jpeg'])
    
    brands = []
    if image_file is not None:
                        
        image = load_image(image_file)
        st.image(image, caption="Uploaded Image")
        
        with open(image_file.name, 'wb') as f:
            f.write(image_file.getbuffer())
        path = os.path.join(os.getcwd(), image_file.name)
        
        
        if st.button('predict'):
            output = brand_detect(path)
            
            if output == 'No Brands Detected!!!':
                st.write("No Brands Detected")
    
            else:

                for brand in output.brands:
                    print("Brand Detected is :", brand.name)
                    x, x1, y, y1 = brand.rectangle.x, brand.rectangle.x + brand.rectangle.w,brand.rectangle.y, brand.rectangle.y + brand.rectangle.h
                    brands.append(brand.name)
                
                st.write("The Brands Detected are : {}".format(brands))
                
            
 

if __name__ == '__main__':
    main()