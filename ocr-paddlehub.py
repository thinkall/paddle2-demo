import paddlehub as hub


# https://www.paddlepaddle.org.cn/hubdetail?name=french_ocr_db_crnn_mobile&en_category=TextRecognition
ocr = hub.Module(name="french_ocr_db_crnn_mobile")
result = ocr.recognize_text(paths=['imgs/ocr_paris_signs.jpeg'], visualization=True, output_dir='imgs')

# https://www.paddlepaddle.org.cn/hubdetail?name=chinese_ocr_db_crnn_server&en_category=TextRecognition
ocr = hub.Module(name="chinese_ocr_db_crnn_server")
result = ocr.recognize_text(paths=['imgs/ocr_airport_multilang.jpeg'], visualization=True, output_dir='imgs')
