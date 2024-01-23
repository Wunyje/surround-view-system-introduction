import os
import cv2


camera_names = ["front", "back", "left", "right"]

# --------------------------------------------------------------------
# (shift_width, shift_height): how far away the birdview looks outside
# of the calibration pattern in horizontal and vertical directions
shift_w = 100
shift_h = 150

# size of the gap between the calibration pattern and the car
# in horizontal and vertical directions
inn_shift_w = 0
inn_shift_h = 0

# total width/height of the stitched image
total_w = 210 + 2 * shift_w
total_h = 300 + 2 * shift_h

# four corners of the rectangular region occupied by the car
# top-left (x_left, y_top), bottom-right (x_right, y_bottom)
xl = shift_w + 50 + inn_shift_w
xr = total_w - xl
yt = shift_h + 100 + inn_shift_h
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
    "front": [(shift_w + 40, shift_h +  74),
              (shift_w + 100, shift_h +  74),
              (shift_w + 40, shift_h + 111),
              (shift_w + 100, shift_h + 111)],

    "back":  [(shift_w + 40, shift_h +  74),
              (shift_w + 100, shift_h +  74),
              (shift_w + 40, shift_h + 111),
              (shift_w + 100, shift_h + 111)],

    "left":  [(shift_h + 164, shift_w),
              (shift_h + 124, shift_w),
              (shift_h + 164, shift_w + 37),
              (shift_h + 124, shift_w + 37)],

    "right": [(shift_h + 124, shift_w),
              (shift_h + 164, shift_w),
              (shift_h + 124, shift_w + 37),
              (shift_h + 164, shift_w + 37)]
}

current_file_directory = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
car_image = cv2.imread(os.path.join(current_file_directory, "images", "car.png"))
car_image = cv2.resize(car_image, (xr - xl, yb - yt))
