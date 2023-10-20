source  /opt/intel/dlstreamer/setupvars.sh
GST_DEBUG=h264parse:5,vaapi:5
# GST_DEBUG=7
/opt/intel/dlstreamer/gstreamer/bin/gst-launch-1.0 -vvvm udpsrc mtu=70000 timeout=40000000000 port=10000   !   queue !  h264parse update-timecode=true ! vaapih264dec  ! vaapisink sync=false