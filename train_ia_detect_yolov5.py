# -*- coding: utf-8 -*-
"""Train IA detect  YOLOv5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1aHL-VubnTh0oI8VYus2BA7X0Ij2KvVW9

# INICIO

Realizar en https://www.makesense.ai el posicionamiento de las clases

Adjuntamos el directorio data.zip

Configuracion.yaml pegar en "/content/yolov5/data"

# ENTORNO
"""

import shutil

# Borra el directorio /content/data/
shutil.rmtree("/content/datasets/")

# Commented out IPython magic to ensure Python compatibility.
!git clone https://github.com/ultralytics/yolov5
# %cd yolov5
# %pip install -qr requirements.txt comet_ml

import torch
import utils
display = utils.notebook_init()

!unzip -q /content/data.zip -d /content/

"""# ENTRENAMIENTO"""

# Entrenamiento configuracion.yaml 150 epocas
!python train.py --img 640 --batch 4 --epochs 150 --data /content/yolov5/data/configuracion.yaml --weights yolov5x.pt --cache

# Commented out IPython magic to ensure Python compatibility.
#evaluamos el entrenamiento

# Buscar metrics/precision

# %load_ext tensorboard
# %tensorboard --logdir runs

# Exportar modelo con los pesos

from google.colab import files
files.download('/content/yolov5/runs/train/exp/weights/best.pt')