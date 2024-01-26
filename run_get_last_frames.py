import cv2
import os
'''
gst-launch-1.0 -e \
    v4l2src device=/dev/video44 ! video/x-raw,format=NV12,width=960,height=640,framerate=30/1 ! queue  ! videomixer name=mix sink_0::xpos=0 sink_0::ypos=0 sink_1::xpos=960 sink_1::ypos=0 sink_2::xpos=0 sink_2::ypos=640 sink_3::xpos=960 sink_3::yp                                                                                                                                                                                                          os=640 ! xvimagesink  sync=false \
    v4l2src device=/dev/video62  ! video/x-raw,format=NV12,width=960,height=640,framerate=30/1 ! queue ! videoflip method=rotate-180 ! mix. \
    v4l2src device=/dev/video53  ! video/x-raw,format=NV12,width=960,height=640,framerate=30/1 ! queue ! videoflip method=rotate-180 ! mix. \
    v4l2src device=/dev/video71  ! video/x-raw,format=NV12,width=960,height=640,framerate=30/1 ! queue ! mix. 
    
gst-launch-1.0 -e \
    v4l2src device=/dev/video44 ! video/x-raw,format=NV12,width=960,height=640,framerate=30/1 ! tee name=video44_t \
    video44_t. ! queue  ! videomixer name=mix sink_0::xpos=0 sink_0::ypos=0 sink_1::xpos=960 sink_1::ypos=0 sink_2::xpos=0 sink_2::ypos=640 sink_3::xpos=960 sink_3::ypos=640 ! xvimagesink  sync=false \
    video44_t. !  mpph264enc ! h264parse ! mp4mux ! filesink location=./videos/video44.mp4 \
    v4l2src device=/dev/video62 ! video/x-raw,format=NV12,width=960,height=640,framerate=30/1 ! videoflip method=rotate-180 ! tee name=video62_t \
    video62_t. ! queue ! mix. \
    video62_t. !  mpph264enc ! h264parse ! mp4mux ! filesink location=./videos/video62.mp4 \
    v4l2src device=/dev/video53 ! video/x-raw,format=NV12,width=960,height=640,framerate=30/1 ! videoflip method=rotate-180 ! tee name=video53_t \
    video53_t. ! queue ! mix. \
    video53_t. !  mpph264enc ! h264parse ! mp4mux ! filesink location=./videos/video53.mp4 \
    v4l2src device=/dev/video71 ! video/x-raw,format=NV12,width=960,height=640,framerate=30/1 ! tee name=video71_t \
    video71_t. ! queue ! mix. \
    video71_t. !  mpph264enc ! h264parse ! mp4mux ! filesink location=./videos/video71.mp4
'''
current_file_directory = os.path.dirname(os.path.realpath(__file__))

# List of video files and corresponding output image names
videos = ['video44.mp4', 'video53.mp4', 'video62.mp4', 'video71.mp4']
output_images = ['front.png', 'left.png', 'back.png', 'right.png']

for video, output_image in zip(videos, output_images):
    video_path = os.path.join(current_file_directory, 'videos', video)
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print(f"Error opening video file {video_path}")
        continue

    # Get total number of frames in the video
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    # Set the current frame position to the last frame
    cap.set(cv2.CAP_PROP_POS_FRAMES, total_frames - 1)

    # Read the last frame
    ret, frame = cap.read()

    img_path = os.path.join(current_file_directory, 'images', output_image)
    if ret:
        # Save the last frame to a file
        cv2.imwrite(img_path, frame)
    else:
        print(f"Error reading last frame of {video_path}")

    # Release the video capture object
    cap.release()

cv2.destroyAllWindows()
