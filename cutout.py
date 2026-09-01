from rembg import remove, new_session
from PIL import Image, ImageFilter
import numpy as np
import os

os.makedirs("images/cutout", exist_ok=True)
session = new_session("isnet-general-use")  # cleaner edges than u2net for products

files = ["float-croissant", "float-cupcake", "float-sourdough", "float-cinnamon", "float-cookie"]

for name in files:
    src = f"images/{name}.png"
    dst = f"images/cutout/{name}.png"
    print(f"Processing {src} ...", flush=True)
    img = Image.open(src).convert("RGBA")

    # Use alpha matting for hairline/crumb detail, then post-process the mask
    out = remove(
        img,
        session=session,
        alpha_matting=True,
        alpha_matting_foreground_threshold=240,
        alpha_matting_background_threshold=15,
        alpha_matting_erode_size=8,
    )

    arr = np.array(out)
    alpha = arr[:, :, 3]

    # De-fringe: push partially-transparent edge pixels either fully opaque or transparent
    # and shrink the alpha by 1px to kill any remaining butter-colored halo.
    alpha_img = Image.fromarray(alpha)
    # slight blur then threshold to smooth jagged edges
    alpha_img = alpha_img.filter(ImageFilter.GaussianBlur(0.6))
    alpha = np.array(alpha_img)
    # kill low-alpha fringe
    alpha[alpha < 60] = 0
    alpha[alpha > 235] = 255
    arr[:, :, 3] = alpha

    cleaned = Image.fromarray(arr, "RGBA")

    # autocrop to content with padding
    bbox = cleaned.getbbox()
    if bbox:
        pad = 10
        l, t, r, b = bbox
        l = max(0, l - pad); t = max(0, t - pad)
        r = min(cleaned.width, r + pad); b = min(cleaned.height, b + pad)
        cleaned = cleaned.crop((l, t, r, b))

    cleaned.save(dst, "PNG", optimize=True)
    print(f"  saved {dst} {cleaned.size}", flush=True)

print("ALL DONE")
