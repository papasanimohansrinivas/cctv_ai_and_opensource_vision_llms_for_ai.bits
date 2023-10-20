source  /opt/intel/dlstreamer/setupvars.sh
GST_DEBUG=h264parse:5,vaapi:5
/opt/intel/dlstreamer/gstreamer/bin/gst-launch-1.0 -vvvm udpsrc mtu=70000 timeout=40000000000 port=10016   !   h264parse update-timecode=true ! vaapih264dec   !   vaapipostproc deinterlace-method=0  deinterlace-mode=2   ! videoconvert ! capsfilter  caps="video/x-raw,format=BGR"  ! videorate   max-rate=5 silent=false  ! video/x-raw,width=312,height=312 ,framerate=1/1 !  queue  ! gvapython module=xeon_gva_python.py class=custom_accumulator function=process_frame arg={\\\"cam_no\\\":\\\"17\\\"} ! fakesink async=false    \
udpsrc mtu=70000 timeout=40000000000 port=10017    !   h264parse update-timecode=true ! vaapih264dec   !   vaapipostproc deinterlace-method=0  deinterlace-mode=2   ! videoconvert ! capsfilter  caps="video/x-raw,format=BGR"  ! videorate   max-rate=5 silent=false  ! video/x-raw,width=312,height=312 ,framerate=1/1 !  queue  ! gvapython module=xeon_gva_python.py class=custom_accumulator function=process_frame arg={\\\"cam_no\\\":\\\"18\\\"} ! fakesink async=false    \
udpsrc mtu=70000 timeout=40000000000 port=10018   !   h264parse update-timecode=true ! vaapih264dec   !   vaapipostproc deinterlace-method=0  deinterlace-mode=2   ! videoconvert ! capsfilter  caps="video/x-raw,format=BGR"  ! videorate   max-rate=5 silent=false  ! video/x-raw,width=312,height=312 ,framerate=1/1 !  queue  ! gvapython module=xeon_gva_python.py class=custom_accumulator function=process_frame arg={\\\"cam_no\\\":\\\"19\\\"} ! fakesink async=false   \
udpsrc mtu=70000 timeout=40000000000 port=10019   !   h264parse update-timecode=true ! vaapih264dec   !   vaapipostproc deinterlace-method=0  deinterlace-mode=2   ! videoconvert ! capsfilter  caps="video/x-raw,format=BGR"  ! videorate   max-rate=5 silent=false  ! video/x-raw,width=312,height=312 ,framerate=1/1 !  queue  ! gvapython module=xeon_gva_python.py class=custom_accumulator function=process_frame arg={\\\"cam_no\\\":\\\"20\\\"} ! fakesink async=false    \
udpsrc mtu=70000 timeout=40000000000 port=10020   !   h264parse update-timecode=true ! vaapih264dec   !   vaapipostproc deinterlace-method=0  deinterlace-mode=2   ! videoconvert ! capsfilter  caps="video/x-raw,format=BGR"  ! videorate   max-rate=5 silent=false  ! video/x-raw,width=312,height=312 ,framerate=1/1 !  queue  ! gvapython module=xeon_gva_python.py class=custom_accumulator function=process_frame arg={\\\"cam_no\\\":\\\"21\\\"} ! fakesink async=false   \
