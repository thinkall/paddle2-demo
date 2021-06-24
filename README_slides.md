---
marp: true
theme: mytheme
backgroundColor: orange
headingDivider: 2
paginate: true
footer: 'Designed by JIANG Li @ June 2021'
_class: lead gaia
---

<style scoped>
section h1 {text-align: center;font-size: 80px;color:black;}
</style>

# A Quick Guide on How to Launch AI with Paddle tools
#### JIANG Li
#### Orange Labs China

<!-- [toc] -->

## PaddlePaddle Ecosystem

## PaddlePaddle Use Cases

---

## Demo Time!


## Demos on Paddle tools

Demo codes for implementing AI models with [PaddlePaddle](https://github.com/PaddlePaddle/) tools such as PaddleHub, PaddleOCR and PaddleX.

### Paddle Installation

[Installation Guide](https://www.paddlepaddle.org.cn/install/quick?docurl=/documentation/docs/en/install/pip/linux-pip_en.html)

```
python -m pip install paddlepaddle -i https://mirror.baidu.com/pypi/simple
```

#### Verify installation
```
>>> import paddle
>>> paddle.utils.run_check()
Running verify PaddlePaddle program ... 
.
PaddlePaddle is installed successfully! Let's start deep learning with PaddlePaddle now.
```

#### Download Demo Code
```
git clone --recurse-submodules https://github.com/thinkall/paddle2-demo
```

## PaddleHub
### Mask Detection
```
python mask-paddlehub.py
```
- Mask Detection with PaddleHub

<div align="center"><img src=imgs/mask_sample.jpeg width="750"/> <img src=imgs/res_mask_sample.jpeg width="750"/></div>

---

### Line Draft



### OCR
```
python ocr-paddlehub.py
```

- PaddleHub OCR VS [i2OCR Free French OCR](https://www.i2ocr.com/free-online-french-ocr)

<div align="center"><img src=imgs/res_ocr_airport_multilang.jpg width="500"/><img src=imgs/res_i2ocr_airport_multilang_ch.png width="400"/></div>

<div align="center"><img src=imgs/res_ocr_paris_signs.jpg width="400"/><img src=imgs/res_i2ocr_paris_signs.png width="500"/></div>


## PaddleOCR
### Download PaddleOCR

```
git clone https://github.com/PaddlePaddle/PaddleOCR.git
```

### Prepare dataset
```
ln -sf $PWD/data/ocr ./PaddleOCR/train_data
```
### download pretrained model
```
cd PaddleOCR/

if [ ! -d "./pretrain_models/rec_mv3_none_bilstm_ctc_v2.0_train" ];then
  # Download MobileNetV3 pretrained model
  wget -P ./pretrain_models/ https://paddleocr.bj.bcebos.com/dygraph_v2.0/ch/ch_ppocr_mobile_v2.0_rec_pre.tar
  # unzip model parameters files
  cd pretrain_models
  tar -xf ch_ppocr_mobile_v2.0_rec_pre.tar && rm -rf ch_ppocr_mobile_v2.0_rec_pre.tar
fi
```

### Train
```
cd PaddleOCR/

# GPU training support single GPU and multi-GPUs, choose card with --gpus
# Train our data, save logs to train.log in "{save_model_dir}"
python3 -m paddle.distributed.launch --gpus '0,1,2,3'  tools/train.py -c ../configs/rec_street_ch_train.yml

# no GPU, set use_gpu to false in the config file
python3 tools/train.py -c ../configs/rec_street_ch_train.yml
```

### Evaluation

```
cd PaddleOCR/

# GPU
python3 -m paddle.distributed.launch --gpus '0' tools/eval.py -c ../configs/rec_street_ch_train.yml -o Global.checkpoints=./output/rec_chinese_lite_v2.0/latest

# no GPU
python3 tools/eval.py -c ../configs/rec_street_ch_train.yml -o Global.checkpoints=./output/rec_chinese_lite_v2.0/latest
```

### Predict

```
python3 tools/infer_rec.py -c ../configs/rec_street_ch_train.yml -o Global.pretrained_model=./output/rec_chinese_lite_v2.0/latest Global.load_static_weights=false Global.infer_img=python3 tools/infer_rec.py -c ../configs/rec_street_ch_train.yml -o Global.pretrained_model=./output/rec_chinese_lite_v2.0/latest \
 Global.load_static_weights=false Global.infer_img=train_data/ocr-sample-images/Train_000000.jpg
```

## PaddleX

