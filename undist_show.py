import cv2
import numpy as np
import os
from surround_view import FisheyeCameraModel, PointSelector, display_image


# Define your devices and corresponding yaml files
devices = ["/dev/video44", "/dev/video53", "/dev/video62", "/dev/video71"]
yaml_files = ["./yaml/front.yaml", "./yaml/left.yaml", "./yaml/back.yaml", "./yaml/right.yaml"]
camera_names = ["front", "left", "back", "right"]

# Create a VideoCapture object and a Camera object for each device
caps = [cv2.VideoCapture(device) for device in devices]
cameras = [FisheyeCameraModel(file, name) for file, name in zip(yaml_files, camera_names)]

# Set the video resolution and frame rate for each device
for cap in caps:
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1280)
    cap.set(cv2.CAP_PROP_FPS, 30)

scale = (0.8, 1.0)
shift = (0, 0)
while True:
    # Read a frame from each device
    frames = [cap.read()[1] for cap in caps]


    # Apply the calibration parameters to each frame
    calibrated_frames = []
    for frame, camera in zip(frames, cameras):
        # Use the undistort method to undistort the frame
        camera.set_scale_and_shift(scale, shift)
        calibrated_frame = camera.undistort(frame)
        # Rotate the frames from video53 and video62 by 180 degrees
        calibrated_frame = cv2.rotate(calibrated_frame, cv2.ROTATE_180)
        calibrated_frames.append(calibrated_frame)



    # Display the frames in a 2x2 grid
    top = np.hstack((calibrated_frames[0],calibrated_frames[2]))
    bottom = np.hstack((calibrated_frames[1], calibrated_frames[3]))
    combined = np.vstack((top, bottom))
    cv2.imshow('Calibrated Frames', combined)

    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the VideoCapture objects and close the windows
for cap in caps:
    cap.release()
cv2.destroyAllWindows()
