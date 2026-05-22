import glob
import re
import os

files = glob.glob('c:/Users/mthar/OneDrive/Desktop/Pibs Front/*.html')
for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    new_content = re.sub(r'\s*<a href="/delivery-info\.html".*?</a>', '', content)
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(new_content)

# Delete delivery-info.html
delivery_path = 'c:/Users/mthar/OneDrive/Desktop/Pibs Front/delivery-info.html'
if os.path.exists(delivery_path):
    os.remove(delivery_path)
