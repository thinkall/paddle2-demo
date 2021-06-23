from paddleocr import PaddleOCR
import os
import json
import tqdm

ocr = PaddleOCR(lang="ch")

root = '/Users/jiangli/Work/projects/github-projects/datasets/OCR/A榜测试数据集/'

unk = []

with open(os.path.join(root, 'LabelTestA.txt'), 'w') as f:
    for i in tqdm.trange(10000):
        file_name = f'TestA_{i:06d}.jpg'
        file_path = os.path.join(root, 'TestAImages', file_name)
        results = ocr.ocr(file_path, det=False)
        results = [res[0] for res in results]

        if len(results) > 0:
            text = ' '.join(results)
            text = file_name + '\t' + text + '\n'
            f.write(text)
        else:
            unk.append(file_name)

        # if i > 10:
        #     break

with open(os.path.join(root, 'unk.txt'), 'w') as f:
    f.write(str(len(unk)) + '\n')
    f.write(json.dumps(unk))
