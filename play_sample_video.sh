gst-launch-1.0 -e \
    v4l2src device=/dev/video44 ! video/x-raw,format=NV12,width=960,height=640,framerate=30/1 ! queue  ! videomixer name=mix sink_0::xpos=0 sink_0::ypos=0 sink_1::xpos=960 sink_1::ypos=0 sink_2::xpos=0 sink_2::ypos=640 sink_3::xpos=960 sink_3::ypos=640 ! xvimagesink  sync=false \
    v4l2src device=/dev/video62  ! video/x-raw,format=NV12,width=960,height=640,framerate=30/1 ! queue ! videoflip method=rotate-180 ! mix. \
    v4l2src device=/dev/video53  ! video/x-raw,format=NV12,width=960,height=640,framerate=30/1 ! queue ! videoflip method=rotate-180 ! mix. \
    v4l2src device=/dev/video71  ! video/x-raw,format=NV12,width=960,height=640,framerate=30/1 ! queue ! mix. 