import paddlehub as hub
import cv2
import matplotlib.pyplot as plt


module = hub.Module(name="pyramidbox_lite_server_mask")


def detect(image):
    """

    Args:
        image: numpy.ndarray from cv2.read(image_path)

    Returns:
        numpy.ndarray of BGR output image
        result
        alarm
    """
    alarm = 0  # 1 for no mask, 0 for mask

    input_dict = {"data": [image]}

    results = module.face_detection(data=input_dict)

    result = results[0]
    result.pop('path')
    for item in result['data']:
        x1 = item['left']
        y1 = item['top']
        x2 = item['right']
        y2 = item['bottom']
        kz = item['label']
        cf = item['confidence']

        if kz == 'MASK':
            image = cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)  # BGR
            cv2.putText(image, f'{kz}: {cf*100:.2f}%', (x1 - 5, y1 - 10), cv2.FONT_HERSHEY_COMPLEX, 0.4, (0, 255, 0), 1)
        else:
            alarm = 1
            image = cv2.rectangle(image, (x1, y1), (x2, y2), (0, 0, 255), 2)  # BGR
            cv2.putText(image, f'{kz}: {cf*100:.2f}%', (x1 - 5, y1 - 10), cv2.FONT_HERSHEY_COMPLEX, 0.4, (0, 0, 255), 1)

    return image, result, alarm


if __name__ == '__main__':
    image = cv2.imread('imgs/mask_sample.jpeg')
    image, res, alarm = detect(image)

    # plt.figure(figsize=(10, 10))
    # plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    # plt.axis('off')
    # plt.show()

    cv2.imwrite('imgs/res_mask_sample.jpeg', image)

    print(res)
