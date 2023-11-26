import os 
import shutil
c= 0
for l in os.listdir("inputs"):
    to_keep =False
    for k in os.listdir("multimodal_llm_pilot_test_outputs"):
        if l in k:
            to_keep=True
    if to_keep:
        pass
    else:
        c+=1
        os.remove("./inputs/{}".format(l))
        print("removed",l,c)
