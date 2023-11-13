from llava.constants import IMAGE_TOKEN_INDEX, DEFAULT_IMAGE_TOKEN, DEFAULT_IM_START_TOKEN, DEFAULT_IM_END_TOKEN
from llava.conversation import conv_templates, SeparatorStyle
from llava.model.builder import load_pretrained_model
from llava.utils import disable_torch_init
from llava.mm_utils import process_images, tokenizer_image_token, get_model_name_from_path, KeywordsStoppingCriteria
import cv2
import torch
model_path ="/root/cctv_ai_and_opensource_vision_llms_for_ai.bits/LLaVA/pretrained-models/models--liuhaotian--llava-v1.5-7b/snapshots/12e054b30e8e061f423c7264bc97d4248232e965"
tokenizer, model, image_processor, context_len = load_pretrained_model(model_path, model_base=None, model_name="llava", load_4bit=True,load_8bit=False)
print(tokenizer.__dict__)
print(image_processor.__dict__)
# class ModelConfig:
#     def __init__(self):
#         image_aspect_ratio = "pad"

# model_cfg = ModelConfig()
# input_numpy = cv2.imread("/root/cctv_ai_and_opensource_vision_llms_for_ai.bits/inputs/fff6e932-7665-4373-897f-b2864214862a.png")
# print(type(input_numpy),input_numpy.shape)
# image_tensor = process_images([input_numpy], image_processor, model_cfg)
# if type(image_tensor) is list:
#     image_tensor = [image.to(model.device, dtype=torch.float16) for image in image_tensor]
# else:
#     image_tensor = image_tensor.to(model.device, dtype=torch.float16)

# import torch 
# class pytorch_to_triton(torch.nn.Module):
    
#     def __init__(self,model_path):
#         super(pytorch_to_triton,self).__init__()
#         self.tokenizer, self.model, self.image_processor, self.context_len = load_pretrained_model(model_path, model_base=None, model_name="llava", load_4bit=True,load_8bit=False)
    
#     def forward(self,image_tensor):
#         conv_mode = "llava_v1"
#         conv = conv_templates[conv_mode].copy()
#         roles = conv.roles
#         inp = "Is there fire 🔥, if so return of coordinates of fire 🔥 in x_min,y_min,x_max,y_max format"
#         inp = DEFAULT_IM_START_TOKEN + DEFAULT_IMAGE_TOKEN + DEFAULT_IM_END_TOKEN + '\n' + inp
#         conv.append_message(conv.roles[0], inp)
#         conv.append_message(conv.roles[1], None)
#         prompt = conv.get_prompt()
#         print(prompt,"current_ prompt")
#         temperature = 0.4
#         max_new_tokens = 512
#         input_ids = tokenizer_image_token(prompt, self.tokenizer, IMAGE_TOKEN_INDEX, return_tensors='pt').unsqueeze(0).cuda()
#         stop_str = conv.sep if conv.sep_style != SeparatorStyle.TWO else conv.sep2
#         keywords = [stop_str]
#         stopping_criteria = KeywordsStoppingCriteria(keywords, self.tokenizer, input_ids)
#         # from transformers import TextStreamer
#         # streamer = TextStreamer(self.tokenizer, skip_prompt=True, skip_special_tokens=True)
#         output_ids = self.model.generate(
#                         input_ids,
#                         images=image_tensor,
#                         do_sample=True,
#                         temperature=0.3,
#                         max_new_tokens=512,
#                         # streamer=streamer,
#                         streamer=None,
#                         use_cache=True,
#                         stopping_criteria=[stopping_criteria])

#         # outputs = self.tokenizer.decode(output_ids[0, input_ids.shape[1]:]).strip()

#         return output_ids

# pytrch_model = pytorch_to_triton(model_path).cuda()
# torch_jit = torch.jit.trace(pytrch_model,(image_tensor,))
# torch_jit.save("experiment.pt")
