import cv2
import os

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

    if ret:
        # Save the last frame to a file
        cv2.imwrite(output_image, frame)
    else:
        print(f"Error reading last frame of {video_path}")

    # Release the video capture object
    cap.release()

cv2.destroyAllWindows()
