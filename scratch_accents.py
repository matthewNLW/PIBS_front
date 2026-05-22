import glob
import re

files = glob.glob('c:/Users/mthar/OneDrive/Desktop/Pibs Front/*.html')
for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # 1. Header Navigation Hovers
    # In <nav> or header: hover:text-[#0F172A] -> hover:text-brand-blue
    content = re.sub(r'hover:text-slate-500', 'hover:text-brand-blue', content)
    content = re.sub(r'hover:text-\[\#0F172A\]', 'hover:text-brand-blue', content)
    
    # 2. Footer Links Hovers
    # The footer has text-slate-400 and hover:text-white. Let's make it hover:text-brand-yellow
    # Specifically inside footer:
    footer_match = re.search(r'<!-- FOOTER -->.*?</footer>', content, flags=re.DOTALL)
    if footer_match:
        footer_html = footer_match.group(0)
        new_footer = footer_html.replace('hover:text-white', 'hover:text-brand-yellow')
        content = content.replace(footer_html, new_footer)
    
    # 3. Homepage Category Links
    # <a ... border-b border-[#0F172A] ... text-[#0F172A] hover:text-brand-blue
    content = content.replace('border-[#0F172A]', 'border-brand-blue')
    
    # 4. Buttons (like Contact Form)
    content = content.replace('bg-[#0F172A] text-white font-sans text-xs font-bold uppercase tracking-widest py-5 rounded-xl hover:bg-slate-700', 'bg-brand-blue text-white font-sans text-xs font-bold uppercase tracking-widest py-5 rounded-xl hover:bg-[#0F172A]')
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
