source  /opt/intel/dlstreamer/setupvars.sh
# GST_DEBUG=h264parse:5,vaapi:5
# GST_DEBUG=7
/opt/intel/dlstreamer/gstreamer/bin/gst-launch-1.0 -m udpsrc address=::1  name=client_ipv6_2_49_206_199_97_25001_cam_1 mtu=70000 timeout=10000000000 port=16000   !   queue  !    h264parse update-timecode=true ! vaapih264dec   !   vaapipostproc deinterlace-method=0  deinterlace-mode=2   ! videoconvert ! capsfilter  caps="video/x-raw,format=BGR"  ! videorate drop-only=true  max-rate=1 silent=false  ! video/x-raw,width=312,height=312 ,framerate=1/1 !  queue  ! gvapython module=xeon_gva_python.py class=custom_accumulator function=process_frame arg={\\\"cam_no\\\":\\\"client_ipv6_2_49_206_199_97_25001_cam_1\\\"} ! fakesink async=false     \
udpsrc address=::1  name=client_ipv6_2_49_206_199_97_25001_cam_2 mtu=70000 timeout=10000000000 port=16001    !   queue  !    h264parse update-timecode=true ! vaapih264dec   !   vaapipostproc deinterlace-method=0  deinterlace-mode=2   ! videoconvert ! capsfilter  caps="video/x-raw,format=BGR"  ! videorate drop-only=true  max-rate=1 silent=false  ! video/x-raw,width=312,height=312 ,framerate=1/1 !  queue  ! gvapython module=xeon_gva_python.py class=custom_accumulator function=process_frame arg={\\\"cam_no\\\":\\\"client_ipv6_2_49_206_199_97_25001_cam_2\\\"} ! fakesink async=false     \
udpsrc address=::1  name=client_ipv6_2_49_206_199_97_25001_cam_3 mtu=70000 timeout=10000000000 port=16002   !   queue  !    h264parse update-timecode=true ! vaapih264dec   !   vaapipostproc deinterlace-method=0  deinterlace-mode=2   ! videoconvert ! capsfilter  caps="video/x-raw,format=BGR"  ! videorate drop-only=true  max-rate=1 silent=false  ! video/x-raw,width=312,height=312 ,framerate=1/1 !  queue  ! gvapython module=xeon_gva_python.py class=custom_accumulator function=process_frame arg={\\\"cam_no\\\":\\\"client_ipv6_2_49_206_199_97_25001_cam_3\\\"} ! fakesink async=false    \
udpsrc address=::1  name=client_ipv6_2_49_206_199_97_25001_cam_4 mtu=70000 timeout=10000000000 port=16003   !   queue  !    h264parse update-timecode=true ! vaapih264dec   !   vaapipostproc deinterlace-method=0  deinterlace-mode=2   ! videoconvert ! capsfilter  caps="video/x-raw,format=BGR"  ! videorate drop-only=true  max-rate=1 silent=false  ! video/x-raw,width=312,height=312 ,framerate=1/1 !  queue  ! gvapython module=xeon_gva_python.py class=custom_accumulator function=process_frame arg={\\\"cam_no\\\":\\\"client_ipv6_2_49_206_199_97_25001_cam_4\\\"} ! fakesink async=false     \
udpsrc address=::1  name=client_ipv6_2_49_206_199_97_25001_cam_5 mtu=70000 timeout=10000000000 port=16004   !   queue  !    h264parse update-timecode=true ! vaapih264dec   !   vaapipostproc deinterlace-method=0  deinterlace-mode=2   ! videoconvert ! capsfilter  caps="video/x-raw,format=BGR"  ! videorate drop-only=true  max-rate=1 silent=false  ! video/x-raw,width=312,height=312 ,framerate=1/1 !  queue  ! gvapython module=xeon_gva_python.py class=custom_accumulator function=process_frame arg={\\\"cam_no\\\":\\\"client_ipv6_2_49_206_199_97_25001_cam_5\\\"} ! fakesink async=false    \
udpsrc address=::1  name=client_ipv6_2_49_206_199_97_25001_cam_6 mtu=70000 timeout=10000000000 port=16005   !   queue  !    h264parse update-timecode=true ! vaapih264dec   !   vaapipostproc deinterlace-method=0  deinterlace-mode=2   ! videoconvert ! capsfilter  caps="video/x-raw,format=BGR"  ! videorate drop-only=true  max-rate=1 silent=false  ! video/x-raw,width=312,height=312 ,framerate=1/1 !  queue  ! gvapython module=xeon_gva_python.py class=custom_accumulator function=process_frame arg={\\\"cam_no\\\":\\\"client_ipv6_2_49_206_199_97_25001_cam_6\\\"} ! fakesink async=false    \
udpsrc address=::1  name=client_ipv6_2_49_206_199_97_25001_cam_7 mtu=70000 timeout=10000000000 port=16006   !   queue  !    h264parse update-timecode=true ! vaapih264dec   !   vaapipostproc deinterlace-method=0  deinterlace-mode=2   ! videoconvert ! capsfilter  caps="video/x-raw,format=BGR"  ! videorate drop-only=true  max-rate=1 silent=false  ! video/x-raw,width=312,height=312 ,framerate=1/1 !  queue  ! gvapython module=xeon_gva_python.py class=custom_accumulator function=process_frame arg={\\\"cam_no\\\":\\\"client_ipv6_2_49_206_199_97_25001_cam_7\\\"} ! fakesink async=false    \
udpsrc address=::1  name=client_ipv6_2_49_206_199_97_25001_cam_8 mtu=70000 timeout=10000000000 port=16007   !   queue  !    h264parse update-timecode=true ! vaapih264dec   !   vaapipostproc deinterlace-method=0  deinterlace-mode=2   ! videoconvert ! capsfilter  caps="video/x-raw,format=BGR"  ! videorate drop-only=true  max-rate=1 silent=false  ! video/x-raw,width=312,height=312 ,framerate=1/1 !  queue  ! gvapython module=xeon_gva_python.py class=custom_accumulator function=process_frame arg={\\\"cam_no\\\":\\\"client_ipv6_2_49_206_199_97_25001_cam_8\\\"} ! fakesink async=false    \
udpsrc address=::1  name=client_ipv6_2_49_206_199_97_25001_cam_9 mtu=70000 timeout=10000000000 port=16008   !   queue  !    h264parse update-timecode=true ! vaapih264dec   !   vaapipostproc deinterlace-method=0  deinterlace-mode=2   ! videoconvert ! capsfilter  caps="video/x-raw,format=BGR"  ! videorate drop-only=true  max-rate=1 silent=false  ! video/x-raw,width=312,height=312 ,framerate=1/1 !  queue  ! gvapython module=xeon_gva_python.py class=custom_accumulator function=process_frame arg={\\\"cam_no\\\":\\\"client_ipv6_2_49_206_199_97_25001_cam_9\\\"} ! fakesink async=false    \
udpsrc address=::1  name=client_ipv6_2_49_206_199_97_25001_cam_10 mtu=70000 timeout=10000000000 port=16009   !   queue  !    h264parse update-timecode=true ! vaapih264dec   !   vaapipostproc deinterlace-method=0  deinterlace-mode=2   ! videoconvert ! capsfilter  caps="video/x-raw,format=BGR"  ! videorate drop-only=true  max-rate=1 silent=false  ! video/x-raw,width=312,height=312 ,framerate=1/1 !  queue  ! gvapython module=xeon_gva_python.py class=custom_accumulator function=process_frame arg={\\\"cam_no\\\":\\\"client_ipv6_2_49_206_199_97_25001_cam_10\\\"} ! fakesink async=false       \
udpsrc address=::1  name=client_ipv6_2_49_206_199_97_25001_cam_11 mtu=70000 timeout=10000000000 port=16010   !   queue  !    h264parse update-timecode=true ! vaapih264dec   !   vaapipostproc deinterlace-method=0  deinterlace-mode=2   ! videoconvert ! capsfilter  caps="video/x-raw,format=BGR"  ! videorate drop-only=true  max-rate=1 silent=false  ! video/x-raw,width=312,height=312 ,framerate=1/1 !  queue  ! gvapython module=xeon_gva_python.py class=custom_accumulator function=process_frame arg={\\\"cam_no\\\":\\\"client_ipv6_2_49_206_199_97_25001_cam_11\\\"} ! fakesink async=false    \
udpsrc address=::1  name=client_ipv6_2_49_206_199_97_25001_cam_12 mtu=70000 timeout=10000000000 port=16011   !   queue  !    h264parse update-timecode=true ! vaapih264dec   !   vaapipostproc deinterlace-method=0  deinterlace-mode=2   ! videoconvert ! capsfilter  caps="video/x-raw,format=BGR"  ! videorate drop-only=true  max-rate=1 silent=false  ! video/x-raw,width=312,height=312 ,framerate=1/1 !  queue  ! gvapython module=xeon_gva_python.py class=custom_accumulator function=process_frame arg={\\\"cam_no\\\":\\\"client_ipv6_2_49_206_199_97_25001_cam_12\\\"} ! fakesink async=false    \
udpsrc address=::1  name=client_ipv6_2_49_206_199_97_25001_cam_13 mtu=70000 timeout=10000000000 port=16012   !   queue  !    h264parse update-timecode=true ! vaapih264dec   !   vaapipostproc deinterlace-method=0  deinterlace-mode=2   ! videoconvert ! capsfilter  caps="video/x-raw,format=BGR"  ! videorate drop-only=true  max-rate=1 silent=false  ! video/x-raw,width=312,height=312 ,framerate=1/1 !  queue  ! gvapython module=xeon_gva_python.py class=custom_accumulator function=process_frame arg={\\\"cam_no\\\":\\\"client_ipv6_2_49_206_199_97_25001_cam_13\\\"} ! fakesink async=false    \
udpsrc address=::1  name=client_ipv6_2_49_206_199_97_25001_cam_14 mtu=70000 timeout=10000000000 port=16013   !   queue  !    h264parse update-timecode=true ! vaapih264dec   !   vaapipostproc deinterlace-method=0  deinterlace-mode=2   ! videoconvert ! capsfilter  caps="video/x-raw,format=BGR"  ! videorate drop-only=true  max-rate=1 silent=false  ! video/x-raw,width=312,height=312 ,framerate=1/1 !  queue  ! gvapython module=xeon_gva_python.py class=custom_accumulator function=process_frame arg={\\\"cam_no\\\":\\\"client_ipv6_2_49_206_199_97_25001_cam_14\\\"} ! fakesink async=false    \
udpsrc address=::1  name=client_ipv6_2_49_206_199_97_25001_cam_15 mtu=70000 timeout=10000000000 port=16014   !   queue  !    h264parse update-timecode=true ! vaapih264dec   !   vaapipostproc deinterlace-method=0  deinterlace-mode=2   ! videoconvert ! capsfilter  caps="video/x-raw,format=BGR"  ! videorate drop-only=true  max-rate=1 silent=false  ! video/x-raw,width=312,height=312 ,framerate=1/1 !  queue  ! gvapython module=xeon_gva_python.py class=custom_accumulator function=process_frame arg={\\\"cam_no\\\":\\\"client_ipv6_2_49_206_199_97_25001_cam_15\\\"} ! fakesink async=false    \
udpsrc address=::1  name=client_ipv6_2_49_206_199_97_25001_cam_16 mtu=70000 timeout=10000000000 port=16015   !   queue  !    h264parse update-timecode=true ! vaapih264dec   !   vaapipostproc deinterlace-method=0  deinterlace-mode=2   ! videoconvert ! capsfilter  caps="video/x-raw,format=BGR"  ! videorate drop-only=true  max-rate=1 silent=false  ! video/x-raw,width=312,height=312 ,framerate=1/1 !  queue  ! gvapython module=xeon_gva_python.py class=custom_accumulator function=process_frame arg={\\\"cam_no\\\":\\\"client_ipv6_2_49_206_199_97_25001_cam_16\\\"} ! fakesink async=false   

