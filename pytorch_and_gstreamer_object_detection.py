import os, sys
import gi
gi.require_version('Gst', '1.0')
from gi.repository import Gst
import numpy as np
import torch
import cv2
print("until torch loaded")
from ultralytics import YOLO
print("after utlralytics loaded")
detector = YOLO('yolov9t.pt')
print(detector.device)
# detector.device = 'mps'
# print(detector.device)
frame_format, pixel_bytes = 'RGB', 3
device = torch.device('mps' if torch.backends.mps.is_available() else 'cpu')
# detector = torch.hub.load('NVIDIA/DeepLearningExamples:torchhub', 'nvidia_ssd', model_math='fp32').eval().to(device)
# preprocess = torchvision.transforms.ToTensor()
count = 0 
Gst.init()
pipeline = Gst.parse_launch(f'''
    rtspsrc location=rtsp://admin:mohan897@192.168.0.29:554/Streaming/Channels/101  ! decodebin ! videoconvert !
    video/x-raw,format={frame_format} !
    fakesink name=s
''')

def on_frame_probe(pad, info):
    global count 
    buf = info.get_buffer()
    print(f'[{buf.pts / Gst.SECOND:6.2f}]')

    image_tensor = buffer_to_image_tensor(buf, pad.get_current_caps())
    # image_batch = image_tensor.unsqueeze(0).to(device)
    image_batch = image_tensor
    with torch.no_grad():
        detections = detector(image_batch,device='mps')
        print(detections)
        cv2.imwrite('Detection_Results_{}.png'.format(count), cv2.cvtColor(detections[0].plot(), cv2.COLOR_RGB2BGR))
        # cv2.waitKey(0)
        count+=1
        # cv2.destroyAllWindows()

    return Gst.PadProbeReturn.OK

def buffer_to_image_tensor(buf, caps):
    caps_structure = caps.get_structure(0)
    height, width = caps_structure.get_value('height'), caps_structure.get_value('width')

    is_mapped, map_info = buf.map(Gst.MapFlags.READ)
    if is_mapped:
        try:
            image_array = np.ndarray(
                (height, width, pixel_bytes),
                dtype=np.uint8,
                buffer=map_info.data
            ).copy() # extend array lifetime beyond subsequent unmap
            # return preprocess(image_array[:,:,:3]) # RGBA -> RGB
            return image_array
        finally:
            buf.unmap(map_info)

pipeline.get_by_name('s').get_static_pad('sink').add_probe(
    Gst.PadProbeType.BUFFER,
    on_frame_probe
)

pipeline.set_state(Gst.State.PLAYING)

try:
    while True:
        msg = pipeline.get_bus().timed_pop_filtered(
            Gst.SECOND,
            Gst.MessageType.EOS | Gst.MessageType.ERROR
        )
        if msg:
            text = msg.get_structure().to_string() if msg.get_structure() else ''
            msg_type = Gst.message_type_get_name(msg.type)
            print(f'{msg.src.name}: [{msg_type}] {text}')
            break
finally:
    # open(f'logs/{os.path.splitext(sys.argv[0])[0]}.pipeline.dot', 'w').write(
    #     Gst.debug_bin_to_dot_data(pipeline, Gst.DebugGraphDetails.ALL)
    # )
    pipeline.set_state(Gst.State.NULL)