import imageio
import numpy as np

# Load HDR
hdr = imageio.imread('Asserts/Sky/sky.hdr', format='HDR-FI')
height = hdr.shape[0]

# Keep only the top ~1/3 or top 40% of the image (adjust as needed)
top_fraction = 0.4
sky_hdr = hdr[:int(height * top_fraction), :, :]

# Save new HDR
imageio.imwrite('sky_only.hdr', sky_hdr, format='HDR-FI')
print("Cropped HDR saved as 'sky_only.hdr'")
