from PaddleOCR import PaddleOCR, draw_ocr
from PIL import Image


def vis_save(img_path, result, save_path='result.jpg', font='simfang'):
    # Visualization
    image = Image.open(img_path).convert('RGB')
    boxes = [line[0] for line in result]
    txts = [line[1][0] for line in result]
    scores = [line[1][1] for line in result]
    im_show = draw_ocr(image, boxes, txts, scores, font_path=f'fonts/{font}.ttf')
    im_show = Image.fromarray(im_show)
    im_show.save(save_path)


def ocr(img_path, lang='ch', save_path='result.jpg', font='simfang'):
    # lang = {ch, en, french, ...}
    # Switch the language by modifying the lang parameter
    ocr = PaddleOCR(lang=lang)  # The model file will be downloaded automatically when executed for the first time
    result = ocr.ocr(img_path, det=True)

    # Recognition and detection can be performed separately through parameter control
    # result = ocr.ocr(img_path, det=False)  Only perform recognition
    # result = ocr.ocr(img_path, rec=False)  Only perform detection
    # Print detection frame and recognition result
    for line in result:
        print(line)

    vis_save(img_path, result, save_path=save_path, font=font)


if __name__ == '__main__':
    ocr(img_path='imgs/ocr_airport_multilang.jpeg', lang='ch',
        save_path='imgs/res_ocr_airport_multilang.jpg', font='simfang')

    ocr(img_path='imgs/ocr_paris_signs.jpeg', lang='french',
        save_path='imgs/res_ocr_paris_signs.jpg', font='french')
