import paddlehub as hub
import cv2
import os


module = hub.Module(name="Extract_Line_Draft")


def line_draft(img_path, output_path, use_gpu=False):

    # execute predict
    module.ExtractLine(img_path, use_gpu=use_gpu)
    output = 'output/output.png'

    input_img = cv2.imread(img_path)
    output_img = cv2.imread(output)
    output_img = cv2.resize(output_img, (input_img.shape[1], input_img.shape[0]))
    cv2.imwrite(output_path, output_img)
    os.remove(output)  # remove temp file
    print('Done with the input image.')


if __name__ == '__main__':
    img_path = 'imgs/cartoon.png'
    output_path = 'imgs/res_cartoon.png'
    line_draft(img_path, output_path)
