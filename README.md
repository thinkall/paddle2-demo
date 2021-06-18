# paddle2-demo
[toc]

Demo codes for AI models implemented with [PaddlePaddle](https://github.com/PaddlePaddle/)

## Paddle Installation

[Installation Guide](https://www.paddlepaddle.org.cn/install/quick?docurl=/documentation/docs/en/install/pip/linux-pip_en.html)

### Choose CPU/GPU

If your computer doesn’t have NVIDIA® GPU, please install the CPU Version of PaddlePaddle

If your computer has NVIDIA® GPU, please make sure that the following conditions are met and install the GPU Version of PaddlePaddle


```
CUDA toolkit 10.1/10.2 with cuDNN v7.6.5+

CUDA toolkit 11.2 with cuDNN v8.1.1

Hardware devices with GPU computing power over 3.0
```

You can refer to NVIDIA official documents for installation process and configuration method of CUDA and cudnn. Please refer to CUDA，cuDNN

### Installation Step

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

## PaddleHub
- Mask Detection
- Line Draft

## PaddleOCR


## PaddleX

