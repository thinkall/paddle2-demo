# A Quick Guide on How to Launch AI with Paddle tools

[toc]

## PaddlePaddle Ecosystem

## PaddlePaddle Use Cases

## Demos

Demo codes for AI models implemented with [PaddlePaddle](https://github.com/PaddlePaddle/).

### Paddle Installation

[Installation Guide](https://www.paddlepaddle.org.cn/install/quick?docurl=/documentation/docs/en/install/pip/linux-pip_en.html)

#### Choose CPU/GPU

Install CPU Version of PaddlePaddle if no NVIDIA® GPU.

Install GPU Version with below conditions:

```
CUDA toolkit 10.1/10.2 with cuDNN v7.6.5+

CUDA toolkit 11.2 with cuDNN v8.1.1

Hardware devices with GPU computing power over 3.0
```

#### Installation Step

You can choose the following version of PaddlePaddle to start installation:

#### CPU Versoion of PaddlePaddle
```
python -m pip install paddlepaddle -i https://mirror.baidu.com/pypi/simple
```

#### GPU Version of PaddlePaddle

- PaddlePaddle for CUDA 10.1 
```
python -m pip install paddlepaddle-gpu==2.1.0.post101 -f https://paddlepaddle.org.cn/whl/mkl/stable.html
```

- PaddlePaddle for CUDA 10.2
```
python -m pip install paddlepaddle-gpu -i https://mirror.baidu.com/pypi/simple
```

- PaddlePaddle for CUDA 11.2
```
python -m pip install paddlepaddle-gpu==2.1.0.post112 -f https://paddlepaddle.org.cn/whl/mkl/stable.html
```

#### Verify installation
After the installation is complete, you can use python to enter the Python interpreter and then use `import paddle` and `paddle.utils.run_check()`.
```
>>> import paddle
>>> paddle.utils.run_check()
Running verify PaddlePaddle program ... 
.
.
.
PaddlePaddle is installed successfully! Let's start deep learning with PaddlePaddle now.
```

## Download Demo Code
```
git clone --recurse-submodules https://github.com/thinkall/paddle2-demo
```

## PaddleHub
### Mask Detection
```
python mask-paddlehub.py
```
- Mask Detection with PaddleHub

<div align="center"><img src=imgs/mask_sample.jpeg height="250"/><img src=imgs/res_mask_sample.jpeg height="250"/></div>


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
Need CUDA and cuDNN
