source  /opt/intel/dlstreamer/setupvars.sh
# GST_DEBUG=h264parse:5,vaapi:5
# GST_DEBUG=7
/opt/intel/dlstreamer/gstreamer/bin/gst-launch-1.0 -m udpsrc  name=client_appsrc_49_206_199_97_25001_cam_1 mtu=70000 timeout=10000000000 port=12001   !   queue  !    h264parse update-timecode=true ! vaapih264dec   !   vaapipostproc deinterlace-method=0  deinterlace-mode=2   ! videoconvert ! capsfilter  caps="video/x-raw,format=BGR"  ! videorate drop-only=true  max-rate=1 silent=false  ! video/x-raw,width=312,height=312 ,framerate=1/1 !  queue  ! gvapython module=xeon_gva_python.py class=custom_accumulator function=process_frame arg={\\\"cam_no\\\":\\\"client_appsrc_49_206_199_97_25001_cam_1\\\"} ! fakesink async=false  
