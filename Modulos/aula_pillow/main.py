# tamanho original: 768.27kb
# Photoshop do python :)

from pathlib import Path
from PIL import Image

ROOT = Path(__file__).parent
ORIGINAL = ROOT / 'img' / 'original.png'
NEW_IMG = ROOT / 'img' / 'new.png'

img_pil = Image.open(ORIGINAL)
width, height = img_pil.size

new_width = 640
new_height = round(height * new_width / width)  # 276

imgResized = img_pil.resize((new_width, new_height))
imgResized.save(
    NEW_IMG,
    optimize=True,
    quality=70
)
