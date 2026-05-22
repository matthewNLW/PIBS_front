import glob
import re
import os

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
                <a href="/contact.html" class="font-sans text-xs font-semibold uppercase tracking-[0.2em] text-[#475569] hover:text-[#0F172A] transition-colors py-4">Contact</a>
                <a href="/delivery-info.html" class="font-sans text-xs font-semibold uppercase tracking-[0.2em] text-[#475569] hover:text-[#0F172A] transition-colors py-4">Delivery / FAQ</a>
            </nav>'''

base_path = 'c:/Users/mthar/OneDrive/Desktop/Pibs Front/'

# 1. Update navigation on all existing HTML files
files = glob.glob(os.path.join(base_path, '*.html'))
for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    new_content = re.sub(r'<nav class="hidden lg:flex.*?</nav>', nav_dropdown, content, flags=re.DOTALL)
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(new_content)

# 2. Read a base file to clone its head and header
with open(os.path.join(base_path, 'delivery-info.html'), 'r', encoding='utf-8') as file:
    template = file.read()

# 3. Create About Us Page
about_content = '''    <section class="w-full py-32 px-6 lg:px-12 bg-[#FAFAFA] min-h-screen">
        <div class="max-w-4xl mx-auto mt-20">
            <div class="flex flex-col text-center mb-16 fade-in-up">
                <span class="text-[#0F172A] font-sans text-xs font-bold uppercase tracking-widest mb-4 block">Our Story</span>
                <h2 class="font-serif text-5xl text-[#0F172A] leading-tight mb-8">About Us.</h2>
                <div class="w-full h-px bg-slate-200 mb-12"></div>
                
                <div class="text-left space-y-8 font-sans text-slate-500 text-lg font-light leading-relaxed">
                    <p>Welcome to Pawleys Island Beach Service, your premier destination for high-quality beach gear and bike rentals. For years, we have been dedicated to enhancing your vacation experience by providing top-of-the-line equipment delivered straight to your door.</p>
                    <p>We understand that vacations are about relaxation and making memories. That's why we take the hassle out of your trip. Whether you're looking to explore the scenic trails of Pawleys Island on one of our comfortable beach cruisers, hit the waves on a paddleboard, or simply relax under the shade of a premium Shibumi, we have you covered.</p>
                    <p>Our commitment to excellent customer service, well-maintained equipment, and convenient delivery has made us a trusted partner for families returning to the island year after year. Let us handle the gear, so you can focus on enjoying the beach.</p>
                </div>
            </div>
        </div>
    </section>'''

about_html = re.sub(r'<section class="w-full py-32 px-6 lg:px-12 bg-\[#FAFAFA\] min-h-screen">.*?</section>', about_content, template, flags=re.DOTALL)
about_html = re.sub(r'<title>.*?</title>', '<title>About Us | Pawleys Island Beach Service</title>', about_html)

with open(os.path.join(base_path, 'about.html'), 'w', encoding='utf-8') as file:
    file.write(about_html)


# 4. Create Contact Us Page
contact_content = '''    <section class="w-full py-32 px-6 lg:px-12 bg-[#FAFAFA] min-h-screen">
        <div class="max-w-4xl mx-auto mt-20">
            <div class="flex flex-col text-center mb-16 fade-in-up">
                <span class="text-[#0F172A] font-sans text-xs font-bold uppercase tracking-widest mb-4 block">Get In Touch</span>
                <h2 class="font-serif text-5xl text-[#0F172A] leading-tight mb-8">Contact Us.</h2>
                <div class="w-full h-px bg-slate-200 mb-12"></div>
                
                <div class="grid grid-cols-1 md:grid-cols-2 gap-12 text-left">
                    <div class="bg-white p-10 rounded-3xl border border-slate-100 premium-shadow">
                        <h3 class="font-serif text-2xl text-[#0F172A] mb-6">Contact Information</h3>
                        <ul class="space-y-6 font-sans text-slate-500 font-light">
                            <li class="flex items-start gap-4">
                                <svg class="w-6 h-6 text-[#0F172A] flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"></path></svg>
                                <div>
                                    <span class="block font-bold text-xs uppercase tracking-widest text-[#0F172A] mb-1">Phone</span>
                                    <span>(555) 123-4567</span>
                                </div>
                            </li>
                            <li class="flex items-start gap-4">
                                <svg class="w-6 h-6 text-[#0F172A] flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"></path></svg>
                                <div>
                                    <span class="block font-bold text-xs uppercase tracking-widest text-[#0F172A] mb-1">Email</span>
                                    <span>info@pawleysislandbeachservice.com</span>
                                </div>
                            </li>
                            <li class="flex items-start gap-4">
                                <svg class="w-6 h-6 text-[#0F172A] flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"></path><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"></path></svg>
                                <div>
                                    <span class="block font-bold text-xs uppercase tracking-widest text-[#0F172A] mb-1">Location</span>
                                    <span>Pawleys Island, SC 29585</span>
                                </div>
                            </li>
                        </ul>
                    </div>
                    
                    <div class="bg-white p-10 rounded-3xl border border-slate-100 premium-shadow">
                        <h3 class="font-serif text-2xl text-[#0F172A] mb-6">Send a Message</h3>
                        <form class="space-y-4">
                            <div>
                                <label class="block font-sans text-xs font-bold text-[#0F172A] uppercase tracking-widest mb-2">Name</label>
                                <input type="text" class="w-full border border-slate-200 rounded-xl px-4 py-3 bg-slate-50 focus:outline-none focus:border-[#0F172A] transition-colors" placeholder="Your Name">
                            </div>
                            <div>
                                <label class="block font-sans text-xs font-bold text-[#0F172A] uppercase tracking-widest mb-2">Email</label>
                                <input type="email" class="w-full border border-slate-200 rounded-xl px-4 py-3 bg-slate-50 focus:outline-none focus:border-[#0F172A] transition-colors" placeholder="your@email.com">
                            </div>
                            <div>
                                <label class="block font-sans text-xs font-bold text-[#0F172A] uppercase tracking-widest mb-2">Message</label>
                                <textarea rows="4" class="w-full border border-slate-200 rounded-xl px-4 py-3 bg-slate-50 focus:outline-none focus:border-[#0F172A] transition-colors" placeholder="How can we help you?"></textarea>
                            </div>
                            <button type="button" class="w-full bg-[#0F172A] text-white font-sans text-xs font-bold uppercase tracking-widest py-4 rounded-xl hover:bg-slate-700 transition-colors mt-4">Send Message</button>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </section>'''

contact_html = re.sub(r'<section class="w-full py-32 px-6 lg:px-12 bg-\[#FAFAFA\] min-h-screen">.*?</section>', contact_content, template, flags=re.DOTALL)
contact_html = re.sub(r'<title>.*?</title>', '<title>Contact Us | Pawleys Island Beach Service</title>', contact_html)

with open(os.path.join(base_path, 'contact.html'), 'w', encoding='utf-8') as file:
    file.write(contact_html)

