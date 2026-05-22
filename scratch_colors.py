from PIL import Image
from collections import Counter

img = Image.open('c:/Users/mthar/OneDrive/Desktop/Pibs Front/logo.png')
img = img.convert('RGB')
pixels = list(img.getdata())
colors = Counter(pixels)

# Exclude white/black/transparent or near white
filtered_colors = []
for color, count in colors.items():
    r, g, b = color
    # Skip very light or very dark colors
    if r > 240 and g > 240 and b > 240:
        continue
    if r < 15 and g < 15 and b < 15:
        continue
    filtered_colors.append((count, color))

filtered_colors.sort(reverse=True)
for count, color in filtered_colors[:10]:
    hex_color = '#{:02x}{:02x}{:02x}'.format(color[0], color[1], color[2])
    print(f"Color: {hex_color}, Count: {count}")
