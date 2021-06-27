import gradio as gr
import base64
import json
import cv2
import requests
import numpy as np

from PaddleOCR import PaddleOCR, draw_ocr
from PIL import Image


title = "AI Demo - OCR"


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
    else:
        for line in result:
            print(f'\nOCR Result: {line}\n')


def ocr_gradio(img, lang):
    img_path = 'flagged/ocr_tmp.jpg'
    out_path = 'flagged/ocr_res.jpg'
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    cv2.imwrite(img_path, img)
    font = 'french' if lang == 'french' else 'simfang'
    ocr(img_path, lang=lang, save_path=out_path, font=font)
    img = cv2.imread(out_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return img


inputs = [
    gr.inputs.Image(label="image for ocr"),
    gr.inputs.Radio(['ch', 'en', 'french'], default='ch', label="language for ocr")
]

outputs = [gr.outputs.Image(label="OCR")]

examples = [['imgs/ocr_airport_multilang.jpeg'],
            ['imgs/ocr_paris_signs.jpeg'],
            ['imgs/ocr_menu.png']]

fns = [ocr_gradio]
iface = gr.Interface(
    fn=fns,
    inputs=inputs,
    outputs=outputs,
    title=title,
    examples=examples,
    allow_screenshot=True,
    allow_flagging=True
)


if __name__ == '__main__':
    iface.launch(debug=True, share=True)
