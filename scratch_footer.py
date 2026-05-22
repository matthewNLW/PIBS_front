import glob
import re

new_footer = '''    <!-- FOOTER -->
    <footer class="w-full bg-[#0F172A] pt-24 pb-12 px-6 lg:px-12 border-t border-white/10 mt-auto">
        <div class="max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-16 mb-16">
            <!-- Brand -->
            <div class="space-y-6">
                <a href="/" class="block">
                    <img src="/logo.png" alt="Pawleys Island Beach Service" class="h-14 w-auto">
                </a>
                <p class="font-sans text-slate-400 text-sm font-light leading-relaxed max-w-xs">
                    Serving Pawleys Island, Litchfield, DeBordieu, and Huntington Beach State Park with premium rentals.
                </p>
            </div>

            <!-- Navigation -->
            <div>
                <h4 class="font-sans text-xs font-bold uppercase tracking-widest text-white mb-6">Explore</h4>
                <ul class="space-y-4 font-sans text-sm font-light text-slate-400">
                    <li><a href="/bikes.html" class="hover:text-brand-blue transition-colors">Bikes & Cruisers</a></li>
                    <li><a href="/beach-gear.html" class="hover:text-brand-blue transition-colors">Beach Rentals</a></li>
                    <li><a href="/water-sports.html" class="hover:text-brand-blue transition-colors">Water Sports</a></li>
                    <li><a href="/about.html" class="hover:text-brand-blue transition-colors">About Us</a></li>
                    <li><a href="/faqs.html" class="hover:text-brand-blue transition-colors">FAQs</a></li>
                </ul>
            </div>

            <!-- Contact -->
            <div>
                <h4 class="font-sans text-xs font-bold uppercase tracking-widest text-white mb-6">Contact</h4>
                <ul class="space-y-4 font-sans text-sm font-light text-slate-400">
                    <li><a href="tel:8432374666" class="hover:text-brand-yellow transition-colors">(843) 237-4666</a></li>
                    <li><a href="mailto:info@pibeachservice.com" class="hover:text-brand-yellow transition-colors">info@pibeachservice.com</a></li>
                    <li><a href="/contact.html" class="hover:text-brand-yellow transition-colors">Send a Message</a></li>
                </ul>
            </div>

            <!-- Location & Hours -->
            <div>
                <h4 class="font-sans text-xs font-bold uppercase tracking-widest text-white mb-6">Visit Us</h4>
                <ul class="space-y-4 font-sans text-sm font-light text-slate-400">
                    <li>10570 Ocean Hwy<br>Pawleys Island, SC 29585</li>
                    <li class="pt-2 text-white font-medium">Open Daily<br><span class="text-slate-400 font-light">9:00 AM - 5:00 PM</span></li>
                </ul>
            </div>
        </div>

        <div class="max-w-7xl mx-auto pt-8 border-t border-slate-800 flex flex-col md:flex-row justify-between items-center gap-4">
            <div class="text-xs text-slate-500 font-sans uppercase tracking-widest">
                &copy; 2026 Pawleys Island Beach Service
            </div>
            <div class="text-xs text-slate-600 font-sans">
                Powered by Booqable
            </div>
        </div>
    </footer>
'''

files = glob.glob('c:/Users/mthar/OneDrive/Desktop/Pibs Front/*.html')
for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # If the file already has the new footer block, we replace it.
    if '<!-- FOOTER -->' in content:
        content = re.sub(r'<!-- FOOTER -->.*?</footer>\n*', new_footer, content, flags=re.DOTALL)
    elif '<!-- 6. FOOTER -->' in content:
        content = re.sub(r'<!-- 6\. FOOTER -->.*?</footer>\n*', new_footer, content, flags=re.DOTALL)
    else:
        # Insert before booqable script hook
        if '<!-- BOOQABLE SCRIPT HOOK -->' in content:
            content = content.replace('<!-- BOOQABLE SCRIPT HOOK -->', new_footer + '\n    <!-- BOOQABLE SCRIPT HOOK -->')
        else:
            content = content.replace('</body>', new_footer + '\n</body>')
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
