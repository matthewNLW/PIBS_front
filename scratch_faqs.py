import os
import re

base_path = 'c:/Users/mthar/OneDrive/Desktop/Pibs Front/'

# 1. Read contact.html as a template
with open(os.path.join(base_path, 'contact.html'), 'r', encoding='utf-8') as f:
    contact_content = f.read()

# 2. Extract the FAQ Section HTML
faq_match = re.search(r'<!-- FAQ SECTION -->.*?</section>', contact_content, flags=re.DOTALL)
faq_html = faq_match.group(0)

# 3. Remove FAQ Section from contact.html
new_contact_content = contact_content.replace(faq_html, '')
with open(os.path.join(base_path, 'contact.html'), 'w', encoding='utf-8') as f:
    f.write(new_contact_content)

# 4. Build faqs.html
# Use contact.html as base, replace title, hero, and replace contact form with FAQ
faqs_content = contact_content.replace('Contact Us | Pawleys Island Beach Service', 'FAQs | Pawleys Island Beach Service')

# Replace Hero
new_hero = '''    <!-- HERO SECTION -->
    <section class="relative w-full h-[40vh] min-h-[400px] flex items-center justify-center overflow-hidden">
        <div class="absolute inset-0 bg-black z-10 opacity-50"></div>
        <img src="/pawleysislandbeachservice-photo-download-1of1/Website_Photos/DSC05713.JPG" alt="FAQs" class="absolute inset-0 w-full h-full object-cover z-0" style="object-position: center 40%;">
        <div class="relative z-20 text-center px-6 mt-16">
            <span class="text-white font-sans text-xs font-bold uppercase tracking-[0.3em] mb-4 block">Knowledge Base</span>
            <h1 class="font-serif text-5xl md:text-7xl text-white leading-tight">FAQs.</h1>
        </div>
    </section>'''
faqs_content = re.sub(r'<!-- HERO SECTION -->.*?</section>', new_hero, faqs_content, flags=re.DOTALL)

# Replace Contact Form section with FAQ section
faqs_content = re.sub(r'<!-- CONTACT FORM & INFO -->.*?</section>', faq_html, faqs_content, flags=re.DOTALL)

with open(os.path.join(base_path, 'faqs.html'), 'w', encoding='utf-8') as f:
    f.write(faqs_content)
