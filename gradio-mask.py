import gradio as gr
import base64
import json
import cv2
import requests
import numpy as np


title = "AI Demo - Mask Detection"


def convert_and_save(b64_string):
    b64_string += '=' * (-len(b64_string) % 4)  # restore stripped '='s
    string = b64_string.encode()
    with open("flagged/result.png", "wb") as f:
        f.write(base64.decodebytes(string))


def mask(img):
    url = "https://aimask.apps.fr01.paas.diod.orange.com/image"
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    _, image_buffer = cv2.imencode('.jpg', img)
    image_b64 = base64.b64encode(image_buffer).decode('utf-8')
    payload = "{\"img\":\"" + image_b64 + "\"}"
    headers = {
        'Content-Type': 'application/json',
    }
    response = requests.request("POST", url, headers=headers, data=payload, verify=False)
    response = json.loads(response.text)
    convert_and_save(response['image'])
    img = cv2.imread('flagged/result.png')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return img


inputs = [
    gr.inputs.Image(label="image for mask detection")
]

outputs = [gr.outputs.Image(label="Mask Detection")]

examples = [['imgs/mask_faces.jpg'],
            ['imgs/mask_qiushuzhen.jpg'],
            ['imgs/mask_zhuyin.jpg']]

fns = [mask]

iface = gr.Interface(
    fn=fns,
    inputs=inputs,
    outputs=outputs,
    title=title,
    examples=examples
)


if __name__ == '__main__':
    iface.launch(share=True)
