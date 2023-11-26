import time
import traceback
import torch
#from torch.onnx import ONNX_ARCHIVE_MODEL_PROTO_NAME, ExportTypes, OperatorExportTypes, #TrainingMode
from torch.autograd import Variable
import torch.nn.functional as F
# from pytorchvideo.models.x3d import create_x3d
import cv2
import re
import numpy as np
import pika
import pickle
import sys
from threading import Thread
import pandas as pd
from torchvision import transforms
from PIL import Image
#from moviepy.editor import ImageSequenceClip
#import av
import requests
import pymysql
import uuid
import sys 

from huggingface_hub import snapshot_download
from pathlib import Path
import os
from threading import Thread

# from llava.constants import IMAGE_TOKEN_INDEX, DEFAULT_IMAGE_TOKEN, DEFAULT_IM_START_TOKEN, DEFAULT_IM_END_TOKEN
# from llava.conversation import conv_templates, SeparatorStyle
# from llava.model.builder import load_pretrained_model
# from llava.utils import disable_torch_init
# from llava.mm_utils import process_images, tokenizer_image_token, get_model_name_from_path, KeywordsStoppingCriteria

from PIL import Image

import requests
from PIL import Image
from io import BytesIO
# from transformers import TextStreamer



load_a = time.time()

from transformers import AutoModelForCausalLM, AutoTokenizer,BitsAndBytesConfig
from transformers.generation import GenerationConfig
import torch
# from modelscope import (
# snapshot_download, AutoModelForCausalLM, AutoTokenizer, GenerationConfig
# )
torch.manual_seed(1234)
# revision = 'v1.0.0'
# model_id = 'qwen/Qwen-VL-Chat-Int4'
# model_dir = snapshot_download(model_id, revision=revision)
# print(model_dir)
# Note: The default behavior now has injection attack prevention off.
tokenizer = AutoTokenizer.from_pretrained("mohan007/Qwen-VL-Chat-Int4", trust_remote_code=True)
# if not hasattr(tokenizer, 'model_dir'):
#     tokenizer.model_dir = model_dir
# use bf16
# quantization_config = BitsAndBytesConfig(
# load_in_4bit=True,
# bnb_4bit_quant_type='nf4',
# bnb_4bit_compute_dtype=torch.bfloat16
# )
# model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen-VL-Chat", device_map="auto", trust_remote_code=True, bf16=True).eval()
# use fp16
# model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen-VL-Chat", device_map="auto", trust_remote_code=True, fp16=True).eval()
# use cpu only
# model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen-VL-Chat", device_map="cpu", trust_remote_code=True).eval()
# use cuda device
model = AutoModelForCausalLM.from_pretrained("mohan007/Qwen-VL-Chat-Int4",device_map="cuda", trust_remote_code=True,low_cpu_mem_usage=True).eval()

# model = model.to_bettertransformer()
# Specify hyperparameters for generation
model.generation_config = GenerationConfig.from_pretrained("mohan007/Qwen-VL-Chat-Int4", trust_remote_code=True)
# print(model.generation_config)
# 1st dialogue turn
load_b = time.time()
print("model loading took this much time !",load_b-load_a)
model.save_pretrained("pretrained_models",max_shard_size="20000MB")
# print(model_download_path,"model_download_path")
