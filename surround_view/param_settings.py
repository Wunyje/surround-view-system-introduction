import os
import cv2


camera_names = ["front", "back", "left", "right"]

# --------------------------------------------------------------------
# (shift_width, shift_height): how far away the birdview looks outside
# of the calibration pattern in horizontal and vertical directions
shift_w = 270
shift_h = 270

# size of the gap between the calibration pattern and the car
# in horizontal and vertical directions
inn_shift_w = 0
inn_shift_h = 0

# total width/height of the stitched image
total_w = 540 + 2 * shift_w
total_h = 540 + 2 * shift_h

# four corners of the rectangular region occupied by the car
# top-left (x_left, y_top), bottom-right (x_right, y_bottom)
xl = shift_w + 108 + inn_shift_w
xr = total_w - xl
yt = shift_h + 108 + inn_shift_h
yb = total_h - yt
# --------------------------------------------------------------------

project_shapes = {
    "front": (total_w, yt),
    "back":  (total_w, yt),
    "left":  (total_h, xl),
    "right": (total_h, xl)
}

# pixel locations of the four points to be chosen.
# you must click these pixels in the same order when running
# the get_projection_map.py script
project_keypoints = {
    "front": [(shift_w + 144, shift_h +  0),
              (shift_w + 396, shift_h +  0),
              (shift_w + 144, shift_h + 108),
              (shift_w + 396, shift_h + 108)],

    "back":  [(shift_w + 144, shift_h +  0),
              (shift_w + 396, shift_h +  0),
              (shift_w + 144, shift_h + 108),
              (shift_w + 396, shift_h + 108)],

    "left":  [(shift_h + 144, shift_w),
              (shift_h + 396, shift_w),
              (shift_h + 144, shift_w + 108),
              (shift_h + 396, shift_w + 108)],

    "right": [(shift_h + 144, shift_w),
              (shift_h + 396, shift_w),
              (shift_h + 144, shift_w + 108),
              (shift_h + 396, shift_w + 108)]
}

current_file_directory = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
car_image = cv2.imread(os.path.join(current_file_directory, "images", "car.png"))
car_image = cv2.resize(car_image, (xr - xl, yb - yt))
