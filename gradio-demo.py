import gradio as gr
import base64
import json
import cv2
import requests
import numpy as np

from PaddleOCR import PaddleOCR, draw_ocr
from PIL import Image


title = "AI Demo - Mask Detection & OCR"


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


def vis_save(img_path, result, save_path='result.jpg', font='simfang'):
    # Visualization
    image = Image.open(img_path).convert('RGB')
    boxes = [line[0] for line in result]
    txts = [line[1][0] for line in result]
    scores = [line[1][1] for line in result]
    im_show = draw_ocr(image, boxes, txts, scores, font_path=f'fonts/{font}.ttf')
    im_show = Image.fromarray(im_show)
    im_show.save(save_path)


def ocr(img_path, lang='ch', save_path='result.jpg', font='simfang', det=True):
    # lang = {ch, en, french, ...}
    # Switch the language by modifying the lang parameter
    ocr = PaddleOCR(lang=lang)  # The model file will be downloaded automatically when executed for the first time
    result = ocr.ocr(img_path, det=det)

    # Recognition and detection can be performed separately through parameter control
    # result = ocr.ocr(img_path, det=False)  Only perform recognition
    # result = ocr.ocr(img_path, rec=False)  Only perform detection
    # Print detection frame and recognition result

    if det:
        vis_save(img_path, result, save_path=save_path, font=font)
        txt = [line[1][0] for line in result]
    else:
        txt = [line for line in result]
    return '\n'.join(txt)


def ocr_gradio(img, lang):
    img_path = 'flagged/ocr_tmp.jpg'
    out_path = 'flagged/ocr_res.jpg'
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    cv2.imwrite(img_path, img)
    font = 'french' if lang == 'french' else 'simfang'
    txt = ocr(img_path, lang=lang, save_path=out_path, font=font)
    img = cv2.imread(out_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return img, txt


def main(img_mask, img_ocr, lang):
    img, txt = ocr_gradio(img_ocr, lang)
    print(txt)
    return mask(img_mask), img, txt


inputs = [
    gr.inputs.Image(label="image for mask detection"),
    gr.inputs.Image(label="image for ocr"),
    gr.inputs.Radio(['ch', 'en', 'french'], default='ch', label="language for ocr")
]

outputs = [gr.outputs.Image(label="Mask Detection"),
           gr.outputs.Image(label="OCR"),
           gr.outputs.Textbox(label="OCR", type="auto")]

examples = [['imgs/mask_faces.jpg', 'imgs/ocr_airport_multilang.jpeg', 'ch'],
            ['imgs/mask_qiushuzhen.jpg', 'imgs/ocr_paris_signs.jpeg', 'french'],
            ['imgs/mask_zhuyin.jpg', 'imgs/ocr_menu.png', 'french']]

iface = gr.Interface(
    fn=main,
    inputs=inputs,
    outputs=outputs,
    title=title,
    examples=examples,
    allow_flagging=False,
    allow_screenshot=False
)


if __name__ == '__main__':
    iface.launch(share=True)
