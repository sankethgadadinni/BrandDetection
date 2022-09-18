""" 
author : Sanketh Gadadinni
Date :   16 Sept 2022
file name : detect.py

The file calls MICROSOFT API which detects brands from images

Requirements:

python == 3.8
azure-cognitiveservices-vision-computervision==0.9.0
streamlit==1.12.2
 
"""


from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

from array import array
from PIL import Image



subscription_key = "bb1921ab006f438f857827d112cb07ce"
endpoint = "https://brandmentions.cognitiveservices.azure.com/"

computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))

'''
Detect Brands - local
This example detects common brands like logos and puts a bounding box around them.
'''

def brand_detect(image_file):
    
    image_file = open(image_file, "rb")
    
    # Select the visual feature(s) you want
    local_image_features = ["brands"]
    # Call API with image and features
    detect_brands_results_local = computervision_client.analyze_image_in_stream(image_file, local_image_features)

    # Print detection results with bounding box and confidence score
    if len(detect_brands_results_local.brands) == 0:
        return "No Brands Detected!!!"
    else:
        return detect_brands_results_local
    


