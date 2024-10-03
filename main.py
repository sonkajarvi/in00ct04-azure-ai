from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials

import os
import sys

if (len(sys.argv) <= 1):
    print("No URL provided :(")
    exit(1)

KEY = os.environ["VISION_KEY"]
ENDPOINT = os.environ["VISION_ENDPOINT"]

client = ComputerVisionClient(ENDPOINT, CognitiveServicesCredentials(KEY))
try:
    result = client.tag_image(sys.argv[1])
except:
    print("An error occurred")
    exit(1)

print("Tags in image: ")
if (len(result.tags) == 0):
    print("No tags detected")
else:
    for tag in result.tags:
        print("'{}', confidence {:.2f}%".format(tag.name, tag.confidence * 100))
