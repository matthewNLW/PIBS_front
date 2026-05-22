import glob
import re

nav_dropdown = '''            <nav class="hidden lg:flex flex-grow justify-center space-x-8 items-center">
                <div class="relative group">
                    <button class="font-sans text-xs font-semibold uppercase tracking-[0.2em] text-[#0F172A] hover:text-slate-500 transition-colors flex items-center gap-1 py-4">
                        Rentals
                        <svg class="w-3 h-3 transition-transform group-hover:rotate-180" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
                    </button>
                    <div class="absolute left-1/2 -translate-x-1/2 mt-0 w-56 bg-white border border-slate-100 rounded-2xl shadow-xl opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-300 transform origin-top -translate-y-2 group-hover:translate-y-0 z-50">
                        <div class="py-3 flex flex-col">
                            <a href="/bikes.html" class="px-6 py-3 font-sans text-xs font-semibold uppercase tracking-[0.2em] text-[#475569] hover:text-[#0F172A] hover:bg-slate-50 transition-colors">Bikes & Cruisers</a>
                            <a href="/beach-gear.html" class="px-6 py-3 font-sans text-xs font-semibold uppercase tracking-[0.2em] text-[#475569] hover:text-[#0F172A] hover:bg-slate-50 transition-colors">Beach Rentals</a>
                            <a href="/water-sports.html" class="px-6 py-3 font-sans text-xs font-semibold uppercase tracking-[0.2em] text-[#475569] hover:text-[#0F172A] hover:bg-slate-50 transition-colors">Water Sports</a>
                        </div>
                    </div>
                </div>
                <a href="/about.html" class="font-sans text-xs font-semibold uppercase tracking-[0.2em] text-[#475569] hover:text-[#0F172A] transition-colors py-4">About</a>
                <a href="/faqs.html" class="font-sans text-xs font-semibold uppercase tracking-[0.2em] text-[#475569] hover:text-[#0F172A] transition-colors py-4">FAQs</a>
                <a href="/contact.html" class="font-sans text-xs font-semibold uppercase tracking-[0.2em] text-[#475569] hover:text-[#0F172A] transition-colors py-4">Contact</a>
            </nav>'''

files = glob.glob('c:/Users/mthar/OneDrive/Desktop/Pibs Front/*.html')
for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    new_content = re.sub(r'<nav class="hidden lg:flex.*?</nav>', nav_dropdown, content, flags=re.DOTALL)
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(new_content)
