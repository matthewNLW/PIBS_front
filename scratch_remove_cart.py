import glob
import re

files = glob.glob('c:/Users/mthar/OneDrive/Desktop/Pibs Front/*.html')
for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Remove the cart div block
    # It looks like:
    #             <div class="flex-shrink-0 flex items-center">
    #                 <div class="booqable-cart ...">Cart (0)</div>
    #             </div>
    
    new_content = re.sub(r'<div class="flex-shrink-0 flex items-center">\s*<div class="booqable-cart.*?</nav>', '</nav>', content, flags=re.DOTALL)
    
    # Since the regex above might be slightly off depending on whitespace, I'll just remove the specific block:
    pattern = r'<div class="flex-shrink-0 flex items-center">\s*<div class="booqable-cart.*?</div>\s*</div>'
    new_content = re.sub(pattern, '', content, flags=re.DOTALL)
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(new_content)
