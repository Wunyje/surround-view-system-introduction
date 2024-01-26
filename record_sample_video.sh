gst-launch-1.0 -e \
    v4l2src device=/dev/video44 num-buffers=100 ! video/x-raw,format=NV12,width=960,height=640,framerate=30/1 ! tee name=video44_t \
    video44_t. ! queue  ! videomixer name=mix sink_0::xpos=0 sink_0::ypos=0 sink_1::xpos=960 sink_1::ypos=0 sink_2::xpos=0 sink_2::ypos=640 sink_3::xpos=960 sink_3::ypos=640 ! xvimagesink  sync=false \
    video44_t. !  mpph264enc ! h264parse ! mp4mux ! filesink location=./videos/video44.mp4 \
    v4l2src device=/dev/video62 num-buffers=100 ! video/x-raw,format=NV12,width=960,height=640,framerate=30/1 ! tee name=video62_t \
    video62_t. ! queue ! mix. \
    video62_t. !  mpph264enc ! h264parse ! mp4mux ! filesink location=./videos/video62.mp4 \
    v4l2src device=/dev/video53 num-buffers=100 ! video/x-raw,format=NV12,width=960,height=640,framerate=30/1 ! tee name=video53_t \
    video53_t. ! queue ! mix. \
    video53_t. !  mpph264enc ! h264parse ! mp4mux ! filesink location=./videos/video53.mp4 \
    v4l2src device=/dev/video71 num-buffers=100 ! video/x-raw,format=NV12,width=960,height=640,framerate=30/1 ! tee name=video71_t \
    video71_t. ! queue ! mix. \
    video71_t. !  mpph264enc ! h264parse ! mp4mux ! filesink location=./videos/video71.mp4
