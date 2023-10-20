import os
import copy
"""export DLSTREAMER_DIR=/opt/intel/dlstreamer

# GStreamer
if [[ -f "${DLSTREAMER_DIR}/gstreamer/setupvars.sh" ]]; then
        DLSTREAMER_DIR=/opt/intel/dlstreamer
        PREFIX=${DLSTREAMER_DIR}/gstreamer
        LIBDIR=${PREFIX}/lib
        LIBEXECDIR=${PREFIX}/bin

        GSTREAMER_EXECUTABLES_DIR=${LIBEXECDIR}:${LIBEXECDIR}/gstreamer-1.0

        if [[ ! ":$GST_PLUGIN_PATH:" == *":${LIBDIR}/gstreamer-1.0:"* ]]; then
                export GST_PLUGIN_PATH=${LIBDIR}/gstreamer-1.0:${GST_PLUGIN_PATH:+${GST_PLUGIN_PATH}}
        fi
        export PATH=${GSTREAMER_EXECUTABLES_DIR}:${PATH}
        export LIBRARY_PATH=${LIBDIR}:${LIBRARY_PATH}
        export LD_LIBRARY_PATH=${LIBDIR}:${LD_LIBRARY_PATH}
        export PKG_CONFIG_PATH=${LIBDIR}/pkgconfig:${PKG_CONFIG_PATH}
        export GI_TYPELIB_PATH=${LIBDIR}/girepository-1.0
        export GST_PLUGIN_SCANNER=${LIBEXECDIR}/gstreamer-1.0/gst-plugin-scanner

        oscode=`. /etc/os-release ; echo "${UBUNTU_CODENAME}"`
        if [[ "$oscode" == "bionic" ]]; then
                export PYTHONPATH=${PREFIX}/lib/python3/dist-packages:${PYTHONPATH}
        fi

        echo "[setupvars.sh] GStreamer 1.18 environment initialized"

    
    #source "${DLSTREAMER_DIR}/gstreamer/setupvars.sh"
fi

# DL Streamer
LIBDIR=${DLSTREAMER_DIR}/lib
if [[ ! ":$GST_PLUGIN_PATH:" == *":${LIBDIR}:"* ]]; then
    export GST_PLUGIN_PATH=${LIBDIR}:${GST_PLUGIN_PATH}
fi
export LD_LIBRARY_PATH=${LIBDIR}:${LD_LIBRARY_PATH}
export LIBRARY_PATH=${LIBDIR}:${LIBRARY_PATH}
export PKG_CONFIG_PATH=${LIBDIR}/pkgconfig:${PKG_CONFIG_PATH}
export MODELS_PATH=${MODELS_PATH:-${HOME}/intel/dl_streamer/models}

# Other variables
export LC_NUMERIC="C"
export LIBVA_DRIVER_NAME=iHD

"""
var = {"SHELL": "/bin/bash", "TMUX": "/tmp//tmux-0/default,1576,6", "PKG_CONFIG_PATH": "/opt/intel/dlstreamer/lib/pkgconfig:/opt/intel/dlstreamer/gstreamer/lib/pkgconfig:", "LIBVA_DRIVER_NAME": "iHD", "PWD": "/root", "LOGNAME": "root", "XDG_SESSION_TYPE": "tty", "MOTD_SHOWN": "pam", "GST_PLUGIN_SCANNER": "/opt/intel/dlstreamer/gstreamer/bin/gstreamer-1.0/gst-plugin-scanner", "GI_TYPELIB_PATH": "/opt/intel/dlstreamer/gstreamer/lib/girepository-1.0", "HOME": "/root", "LANG": "en_US.UTF-8",  "MODELS_PATH": "/root/intel/dl_streamer/models", "SSH_CONNECTION": "124.123.168.29 55603 8.9.4.110 22", "XDG_SESSION_CLASS": "user", "TERM": "screen", "USER": "root", "TMUX_PANE": "%6", "LIBRARY_PATH": "/opt/intel/dlstreamer/lib:/opt/intel/dlstreamer/gstreamer/lib:", "DLSTREAMER_DIR": "/opt/intel/dlstreamer", "SHLVL": "2", "XDG_SESSION_ID": "1", "GST_PLUGIN_PATH": "/opt/intel/dlstreamer/lib:/opt/intel/dlstreamer/gstreamer/lib/gstreamer-1.0:", "LD_LIBRARY_PATH": "/opt/intel/dlstreamer/lib:/opt/intel/dlstreamer/gstreamer/lib:", "XDG_RUNTIME_DIR": "/run/user/0", "SSH_CLIENT": "124.123.175.101 2419 22", "XDG_DATA_DIRS": "/usr/local/share:/usr/share:/var/lib/snapd/desktop", "PATH": "/opt/intel/dlstreamer/gstreamer/bin:/opt/intel/dlstreamer/gstreamer/bin/gstreamer-1.0:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin", "DBUS_SESSION_BUS_ADDRESS": "unix:path=/run/user/0/bus", "SSH_TTY": "/dev/pts/0", "LC_NUMERIC": "C", "_": "/usr/bin/python3"}

os.environ["DLSTREAMER_DIR"]=var["DLSTREAMER_DIR"]
# # os.environ["GSTREAMER_EXECUTABLES_DIR"]=var["GSTREAMER_EXECUTABLES_DIR"]
os.environ["GST_PLUGIN_PATH"]=var["GST_PLUGIN_PATH"]


os.environ["PATH"]=var["PATH"]
os.environ["LIBRARY_PATH"]=var["LIBRARY_PATH"]
os.environ["LD_LIBRARY_PATH"]=var["LD_LIBRARY_PATH"]
os.environ["GI_TYPELIB_PATH"]=var["GI_TYPELIB_PATH"]
# os.environ["PKG_CONFIG_PATH"]=var["PKG_CONFIG_PATH"]

# os.environ["GST_PLUGIN_SCANNER"]=var["GST_PLUGIN_SCANNER"]
os.environ["LIBVA_DRIVER_NAME"]="iHD"
os.environ["LC_NUMERIC"]="C"
# os.system(". /opt/intel/dlstreamer/setupvars.sh")
print(os.environ)
import sys
import traceback
import argparse
print("yo----------")
import gi
print("yo----------2")
gi.require_version("Gst", "1.0")
from gi.repository import Gst, GObject,GLib ,GstApp # noqa:F401,F402
print("yo-----3")
import numpy as np
# Initializes Gstreamer, it"s variables, paths
Gst.init(None)
import cv2

command = """ udpsrc mtu=70000 timeout=40000000000 port=10000   !   h264parse update-timecode=true ! vaapih264dec low-latency=true  !   vaapipostproc deinterlace-method=0  deinterlace-mode=2   ! videoconvert ! capsfilter  caps="video/x-raw,format=BGR"  ! videorate drop-only=true  max-rate=1 silent=false ! video/x-raw,width=312,height=312 ,framerate=1/1 !  identity name=test ! fakesink"""




def on_message(bus: Gst.Bus, message: Gst.Message, loop: GLib.MainLoop):
    mtype = message.type
    """
        Gstreamer Message Types and how to parse
        https://lazka.github.io/pgi-docs/Gst-1.0/flags.html#Gst.MessageType
    """
    # print(message.get_structure(),mtype,message.get_structure().has_name("GstUDPSrcTimeout"),message.get_structure().to_string())

    if message is not None:

        
        if message.get_structure().has_name("GstUDPSrcTimeout"):
            print(message.get_structure().to_string())

            timeout_after = int(message.get_structure().to_string().replace("GstUDPSrcTimeout, timeout=(guint64)","").replace(";",""))

        
        if mtype == Gst.MessageType.INFO:
            print("bus event",message.parse_info())

        if mtype == Gst.MessageType.EOS:
            print("End of stream")
            loop.quit()

        elif mtype == Gst.MessageType.ERROR:
            err, debug = message.parse_error()
            print(err, debug)
            loop.quit()

        elif mtype == Gst.MessageType.WARNING:
            err, debug = message.parse_warning()
            print(err, debug)

        return True



class frame_accumulator():

    def __init__(self,cam_no,no_of_frames):
        self.cam_no = cam_no
        self.no_of_frames = 16
        self.array = []
        self.count = 0
        self.numpy_stack_image = None

    def func1(self,element,buffer):
        # print(type(element),buffer,"herer <------")
        height = 312
        width = 312
        success, map_info = buffer.map(Gst.MapFlags.READ)
        if not success:
            raise RuntimeError("Could not map buffer data!")

        numpy_frame = np.ndarray(
            shape=(height, width, 3),
            dtype=np.uint8,
            buffer=map_info.data)

        # Clean up the buffer mapping
        buffer.unmap(map_info)
        if self.numpy_stack_image is None:
            self.numpy_stack_image = np.expand_dims(copy.deepcopy(numpy_frame), axis= 0)
        else:
            self.numpy_stack_image = np.append(self.numpy_stack_image, np.expand_dims(copy.deepcopy(numpy_frame), axis= 0) , axis= 0)
        if self.numpy_stack_image.shape[0]==16:
            for k in list(self.numpy_stack_image):
                cv2.imwrite("special_image_{}_{}.png".format(self.cam_no,self.count),k)
                self.count +=1
            self.count = 0
            self.numpy_stack_image = None

        # if len(self.array)<self.no_of_frames:
        #     self.array.extend(copy.deepcopy(numpy_frame))
        #     # self.array += [numpy_frame]
        #     self.count+=1
        # elif len(self.array)==16:

        #     for k in self.array:
        #         cv2.imwrite("special_image_{}_{}.png".format(self.cam_no,self.count),k)
        #         self.count +=1
        #     self.array = []
        #     self.count = 0
        # elif len(self.array)>16:
        #     for k in self.array[:16]:
        #         cv2.imwrite("special_image_{}_{}.png".format(self.cam_no,self.count),k)
        #         self.count +=1
        #     self.array = self.array[16:]

        #     self.count = 0
        

        print('yaaayy ',numpy_frame.shape,self.count)
        cv2.imwrite("special_image_2_{}_{}.png".format(self.cam_no,self.count),numpy_frame)
        # self.count+=1

    # def try_new_sample(self, app_sink):

    #     sample = app_sink.pull_sample()
    #     caps = sample.get_caps()

    #     # Extract the width and height info from the sample's caps
    #     height = caps.get_structure(0).get_value("height")
    #     width = caps.get_structure(0).get_value("width")

    #     # Get the actual data
    #     buffer = sample.get_buffer()
    #     # Get read access to the buffer data
    #     success, map_info = buffer.map(Gst.MapFlags.READ)
    #     if not success:
    #         raise RuntimeError("Could not map buffer data!")

    #     numpy_frame = np.ndarray(
    #         shape=(height, width, 3),
    #         dtype=np.uint8,
    #         buffer=map_info.data)
    #     print(numpy_frame.shape,"just shape")
    #     # Clean up the buffer mapping
    #     buffer.unmap(map_info)
    #     if len(self.array)<self.no_of_frames:
    #         self.array.append(numpy_frame)
    #     else:
    #         for k in self.array:
    #             cv2.imwrite("special_image_2_{}_{}.png".format(self.cam_no,self.count),numpy_frame)
    #             self.count +=1

f1= frame_accumulator(1,16)
print("just beore parsed-----------")
# Gst.Pipeline https://lazka.github.io/pgi-docs/Gst-1.0/classes/Pipeline.html
# https://lazka.github.io/pgi-docs/Gst-1.0/functions.html#Gst.parse_launch
pipeline = Gst.parse_launch(command)

identity1 = pipeline.get_by_name('test') 
# appsink = pipeline.get_by_name('num_1')

# appsink.set_property("emit-signals", True)
# appsink.connect("new-sample", f1.try_new_sample)
identity1.connect('handoff', f1.func1)
print("just parsed -------------")
# https://lazka.github.io/pgi-docs/Gst-1.0/classes/Bus.html
bus = pipeline.get_bus()

# allow bus to emit messages to main thread
bus.add_signal_watch()

# Start pipeline
pipeline.set_state(Gst.State.PLAYING)

# Init GObject loop to handle Gstreamer Bus Events
loop = GLib.MainLoop()

# Add handler to specific signal
# https://lazka.github.io/pgi-docs/GObject-2.0/classes/Object.html#GObject.Object.connect
bus.connect("message", on_message, loop)
print("just beforerun ---------------")
try:
    print("run man !!!!!!!!!!")
    loop.run()

except Exception:
    traceback.print_exc()
    loop.quit()

# Stop Pipeline
pipeline.set_state(Gst.State.NULL)
