from PIL import Image
import numpy as np
from numpy.random import default_rng

# new white image
w, h = 512, 512
data = np.zeros((h, w, 3), dtype=np.uint8)
data[0:w, 0:h] = [255, 255, 255]

comps_x = np.tile(np.arange(w), h)
comps_y = np.arange(h).repeat(w)

# draw random circles
rng = default_rng(321)
circle_count = 660
radius_range = (5, 40)
circles_radius_sq = rng.triangular(left=radius_range[0], mode=radius_range[0], right=radius_range[1], size=circle_count) ** 2
circles_position = rng.uniform(size=(2, circle_count)) * [[w], [h]]

dist_circles_sq = ((np.broadcast_to(comps_x[None, :], (circle_count,) + comps_x.shape) - circles_position[0, :, None]) ** 2 + 
                   (np.broadcast_to(comps_y[None, :], (circle_count,) + comps_y.shape) - circles_position[1, :, None]) ** 2)
circle_pix = dist_circles_sq < circles_radius_sq[:, None]

for in_circle in circle_pix:
    data[(comps_x[in_circle], comps_y[in_circle])] = [0, 0, 0]


img = Image.fromarray(data, 'RGB')
img.show()