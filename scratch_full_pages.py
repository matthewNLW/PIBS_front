import os
import re

base_path = 'c:/Users/mthar/OneDrive/Desktop/Pibs Front/'

# Template structure for injection
with open(os.path.join(base_path, 'delivery-info.html'), 'r', encoding='utf-8') as file:
    template = file.read()

about_content = '''
    <!-- HERO SECTION -->
    <section class="relative w-full h-[60vh] min-h-[500px] flex items-center justify-center overflow-hidden">
        <div class="absolute inset-0 bg-black z-10 opacity-50"></div>
        <img src="/pawleysislandbeachservice-photo-download-1of1/Website_Photos/DSC05780.JPG" alt="About Pawleys Island Beach Service" class="absolute inset-0 w-full h-full object-cover z-0">
        <div class="relative z-20 text-center px-6 mt-16">
            <span class="text-white font-sans text-xs font-bold uppercase tracking-[0.3em] mb-4 block">Our Story</span>
            <h1 class="font-serif text-5xl md:text-7xl text-white leading-tight">About Us.</h1>
        </div>
    </section>

    <!-- CONTENT SECTION -->
    <section class="w-full py-24 px-6 lg:px-12 bg-white">
        <div class="max-w-7xl mx-auto flex flex-col lg:flex-row gap-16 items-center">
            <div class="w-full lg:w-1/2">
                <img src="/pawleysislandbeachservice-photo-download-1of1/Website_Photos/DSC05814.JPG" alt="Beach Rentals" class="w-full h-auto rounded-[2rem] premium-shadow object-cover aspect-[4/5]">
            </div>
            <div class="w-full lg:w-1/2 space-y-8 font-sans text-slate-500 text-lg font-light leading-relaxed">
                <h2 class="font-serif text-4xl lg:text-5xl text-[#0F172A] leading-tight mb-8">Enhancing your beach experience.</h2>
                <p>At Pawleys Island Beach Service, we offer an exciting range of rental services to enhance your beach experience! Choose from our convenient bike rentals, perfect for exploring the picturesque coastline. Beach rentals, including chairs and umbrellas for relaxation under the sun. For the adventurous spirit, dive into our watersport rentals, featuring kayaks, paddle boards, and canoes.</p>
                <p>We provide convenient delivery and curbside pickup options for all rentals. Just let us know your location, and we’ll handle the rest. Whether you’re looking for adventure or relaxation, we’ve got you covered!</p>
            </div>
        </div>
    </section>

    <!-- FEATURES -->
    <section class="w-full py-24 px-6 lg:px-12 bg-[#FAFAFA]">
        <div class="max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-3 gap-12 text-center">
            <div class="p-10 bg-white rounded-[2rem] border border-slate-100 premium-shadow">
                <div class="w-16 h-16 bg-slate-50 rounded-full mx-auto flex items-center justify-center mb-8">
                    <svg class="w-6 h-6 text-[#0F172A]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M5 3v4M3 5h4M6 17v4m-2-2h4m5-16l2.286 6.857L21 12l-5.714 2.143L13 21l-2.286-6.857L5 12l5.714-2.143L13 3z"></path></svg>
                </div>
                <h3 class="font-serif text-2xl text-[#0F172A] mb-4">Premium Gear</h3>
                <p class="font-sans text-slate-500 font-light leading-relaxed">We source only the highest quality bikes, boards, and beach essentials to ensure your comfort and safety.</p>
            </div>
            <div class="p-10 bg-white rounded-[2rem] border border-slate-100 premium-shadow">
                <div class="w-16 h-16 bg-slate-50 rounded-full mx-auto flex items-center justify-center mb-8">
                    <svg class="w-6 h-6 text-[#0F172A]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M13 10V3L4 14h7v7l9-11h-7z"></path></svg>
                </div>
                <h3 class="font-serif text-2xl text-[#0F172A] mb-4">Island Delivery</h3>
                <p class="font-sans text-slate-500 font-light leading-relaxed">Skip the hassle. We deliver your rentals directly to your beach house or vacation rental, completely free of stress.</p>
            </div>
            <div class="p-10 bg-white rounded-[2rem] border border-slate-100 premium-shadow">
                <div class="w-16 h-16 bg-slate-50 rounded-full mx-auto flex items-center justify-center mb-8">
                    <svg class="w-6 h-6 text-[#0F172A]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M21 12a9 9 0 01-9 9m9-9a9 9 0 00-9-9m9 9H3m9 9a9 9 0 01-9-9m9 9c1.657 0 3-4.03 3-9s-1.343-9-3-9m0 18c-1.657 0-3-4.03-3-9s1.343-9 3-9m-9 9a9 9 0 019-9"></path></svg>
                </div>
                <h3 class="font-serif text-2xl text-[#0F172A] mb-4">Local Experts</h3>
                <p class="font-sans text-slate-500 font-light leading-relaxed">As Pawleys Island locals, we know the best trails, the perfect waves, and the ideal spots to set up for the day.</p>
            </div>
        </div>
    </section>
'''

about_html = re.sub(r'<section class="w-full py-32 px-6 lg:px-12 bg-\[#FAFAFA\] min-h-screen">.*?</section>', about_content, template, flags=re.DOTALL)
about_html = re.sub(r'<title>.*?</title>', '<title>About Us | Pawleys Island Beach Service</title>', about_html)
with open(os.path.join(base_path, 'about.html'), 'w', encoding='utf-8') as file:
    file.write(about_html)


contact_content = '''
    <!-- HERO SECTION -->
    <section class="relative w-full h-[40vh] min-h-[400px] flex items-center justify-center overflow-hidden">
        <div class="absolute inset-0 bg-black z-10 opacity-50"></div>
        <img src="/pawleysislandbeachservice-photo-download-1of1/Website_Photos/DSC05753.JPG" alt="Contact Pawleys Island Beach Service" class="absolute inset-0 w-full h-full object-cover z-0" style="object-position: center 30%;">
        <div class="relative z-20 text-center px-6 mt-16">
            <span class="text-white font-sans text-xs font-bold uppercase tracking-[0.3em] mb-4 block">Get In Touch</span>
            <h1 class="font-serif text-5xl md:text-7xl text-white leading-tight">Contact Us.</h1>
        </div>
    </section>

    <!-- CONTACT FORM & INFO -->
    <section class="w-full py-24 px-6 lg:px-12 bg-[#FAFAFA]">
        <div class="max-w-7xl mx-auto grid grid-cols-1 lg:grid-cols-2 gap-16">
            <!-- Info -->
            <div class="flex flex-col justify-center">
                <h2 class="font-serif text-4xl lg:text-5xl text-[#0F172A] mb-10 leading-tight">We'd love to hear from you.</h2>
                <p class="font-sans text-slate-500 text-lg font-light leading-relaxed mb-12">Whether you have questions about our rentals, need help planning your perfect beach day, or want to inquire about delivery, our team is here to assist.</p>
                
                <ul class="space-y-8 font-sans text-slate-500 font-light text-lg">
                    <li class="flex items-start gap-6">
                        <div class="w-14 h-14 bg-white rounded-full flex items-center justify-center premium-shadow flex-shrink-0 text-[#0F172A]">
                            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"></path></svg>
                        </div>
                        <div class="pt-1">
                            <span class="block font-bold text-xs uppercase tracking-widest text-[#0F172A] mb-1">Phone</span>
                            <span>(843) 237-4666</span>
                        </div>
                    </li>
                    <li class="flex items-start gap-6">
                        <div class="w-14 h-14 bg-white rounded-full flex items-center justify-center premium-shadow flex-shrink-0 text-[#0F172A]">
                            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"></path></svg>
                        </div>
                        <div class="pt-1">
                            <span class="block font-bold text-xs uppercase tracking-widest text-[#0F172A] mb-1">Email</span>
                            <span>info@pibeachservice.com</span>
                        </div>
                    </li>
                    <li class="flex items-start gap-6">
                        <div class="w-14 h-14 bg-white rounded-full flex items-center justify-center premium-shadow flex-shrink-0 text-[#0F172A]">
                            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"></path><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"></path></svg>
                        </div>
                        <div class="pt-1">
                            <span class="block font-bold text-xs uppercase tracking-widest text-[#0F172A] mb-1">Location</span>
                            <span>10570 Ocean Hwy<br>Pawleys Island, SC 29585</span>
                        </div>
                    </li>
                </ul>
            </div>
            
            <!-- Form -->
            <div class="bg-white p-12 rounded-[2rem] border border-slate-100 premium-shadow">
                <form class="space-y-6">
                    <div>
                        <label class="block font-sans text-xs font-bold text-[#0F172A] uppercase tracking-widest mb-2">Name</label>
                        <input type="text" class="w-full border border-slate-200 rounded-xl px-4 py-4 bg-slate-50 focus:outline-none focus:border-[#0F172A] focus:bg-white transition-colors" placeholder="Your Name">
                    </div>
                    <div>
                        <label class="block font-sans text-xs font-bold text-[#0F172A] uppercase tracking-widest mb-2">Email</label>
                        <input type="email" class="w-full border border-slate-200 rounded-xl px-4 py-4 bg-slate-50 focus:outline-none focus:border-[#0F172A] focus:bg-white transition-colors" placeholder="your@email.com">
                    </div>
                    <div>
                        <label class="block font-sans text-xs font-bold text-[#0F172A] uppercase tracking-widest mb-2">Message</label>
                        <textarea rows="5" class="w-full border border-slate-200 rounded-xl px-4 py-4 bg-slate-50 focus:outline-none focus:border-[#0F172A] focus:bg-white transition-colors" placeholder="How can we help you?"></textarea>
                    </div>
                    <button type="button" class="w-full bg-[#0F172A] text-white font-sans text-xs font-bold uppercase tracking-widest py-5 rounded-xl hover:bg-slate-700 transition-colors mt-2 shadow-lg">Send Message</button>
                </form>
            </div>
        </div>
    </section>

    <!-- FAQ SECTION -->
    <section class="w-full py-24 px-6 lg:px-12 bg-white">
        <div class="max-w-4xl mx-auto">
            <div class="text-center mb-16">
                <span class="text-[#0F172A] font-sans text-xs font-bold uppercase tracking-widest mb-4 block">Got Questions?</span>
                <h2 class="font-serif text-5xl text-[#0F172A]">Frequently Asked Questions.</h2>
            </div>
            <div class="space-y-8 bg-[#FAFAFA] p-10 lg:p-14 rounded-[2rem] border border-slate-100 premium-shadow">
                <div class="border-b border-slate-200 pb-8">
                    <h4 class="font-serif text-2xl text-[#0F172A] mb-4">What rentals do you offer?</h4>
                    <p class="font-sans text-slate-500 font-light leading-relaxed">We offer a variety of rentals, including bikes, kayaks, paddle boards, canoes, beach chairs, and umbrellas. Whether you’re looking for adventure or relaxation, we’ve got you covered!</p>
                </div>
                <div class="border-b border-slate-200 pb-8">
                    <h4 class="font-serif text-2xl text-[#0F172A] mb-4">Do you offer delivery and pickup services?</h4>
                    <p class="font-sans text-slate-500 font-light leading-relaxed">Yes! We provide convenient delivery and curbside pickup options for all rentals. Just let us know your location, and we’ll handle the rest.</p>
                </div>
                <div class="border-b border-slate-200 pb-8">
                    <h4 class="font-serif text-2xl text-[#0F172A] mb-4">Can I purchase beach gear and apparel from your store?</h4>
                    <p class="font-sans text-slate-500 font-light leading-relaxed">Absolutely! We have a great selection of Pawleys Island T-shirts, beach supplies, pool toys, and accessories—everything you need for a perfect beach day.</p>
                </div>
                <div class="pt-2">
                    <h4 class="font-serif text-2xl text-[#0F172A] mb-4">How do I book a rental?</h4>
                    <p class="font-sans text-slate-500 font-light leading-relaxed">You can book online or visit our store in person. If you have any questions, feel free to give us a call—we’re happy to assist!</p>
                </div>
            </div>
        </div>
    </section>
'''

contact_html = re.sub(r'<section class="w-full py-32 px-6 lg:px-12 bg-\[#FAFAFA\] min-h-screen">.*?</section>', contact_content, template, flags=re.DOTALL)
contact_html = re.sub(r'<title>.*?</title>', '<title>Contact Us | Pawleys Island Beach Service</title>', contact_html)
with open(os.path.join(base_path, 'contact.html'), 'w', encoding='utf-8') as file:
    file.write(contact_html)

