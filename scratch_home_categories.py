import re

with open('c:/Users/mthar/OneDrive/Desktop/Pibs Front/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

categories_html = '''    <!-- 4. CATEGORY SHOWCASE -->
    <section id="categories" class="w-full py-32 px-6 lg:px-12 bg-[#FAFAFA]">
        <div class="max-w-7xl mx-auto space-y-32">
            
            <!-- Category 1 -->
            <div class="flex flex-col lg:flex-row w-full bg-white rounded-3xl overflow-hidden premium-shadow fade-in-up">
                <div class="w-full lg:w-1/2 min-h-[500px] relative order-1 lg:order-2 bg-slate-50">
                    <img src="/pawleysislandbeachservice-photo-download-1of1/Website_Photos/DSC05753.JPG" alt="Bikes and Cruisers" class="absolute inset-0 w-full h-full object-cover" style="object-position: center 30%;">
                </div>
                <div class="w-full lg:w-1/2 p-12 lg:p-24 flex flex-col justify-center relative order-2 lg:order-1">
                    <h3 class="font-serif text-5xl lg:text-6xl text-[#0F172A] leading-tight mb-8">Bikes & Cruisers.</h3>
                    <p class="font-sans text-slate-500 text-xl font-light leading-relaxed mb-12">Explore the picturesque coastline and scenic trails of Pawleys Island on one of our comfortable, perfectly maintained beach cruisers.</p>
                    <a href="/bikes.html" class="inline-flex items-center gap-4 text-[#0F172A] hover:text-slate-500 transition-colors group w-max border-b border-[#0F172A] pb-1">
                        <span class="font-sans text-sm font-bold uppercase tracking-widest">Shop Bikes</span>
                        <svg class="w-5 h-5 transition-transform group-hover:translate-x-2" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"></path></svg>
                    </a>
                </div>
            </div>

            <!-- Category 2 -->
            <div class="flex flex-col lg:flex-row w-full bg-white rounded-3xl overflow-hidden premium-shadow fade-in-up">
                <div class="w-full lg:w-1/2 min-h-[500px] relative order-1 bg-slate-50">
                    <img src="/pawleysislandbeachservice-photo-download-1of1/Website_Photos/DSC05814.JPG" alt="Beach Rentals" class="absolute inset-0 w-full h-full object-cover">
                </div>
                <div class="w-full lg:w-1/2 p-12 lg:p-24 flex flex-col justify-center relative order-2">
                    <h3 class="font-serif text-5xl lg:text-6xl text-[#0F172A] leading-tight mb-8">Beach Rentals.</h3>
                    <p class="font-sans text-slate-500 text-xl font-light leading-relaxed mb-12">Relax under the sun with our high-end aluminum chairs, canvas umbrellas, and family-sized Shibumi shades delivered straight to you.</p>
                    <a href="/beach-gear.html" class="inline-flex items-center gap-4 text-[#0F172A] hover:text-slate-500 transition-colors group w-max border-b border-[#0F172A] pb-1">
                        <span class="font-sans text-sm font-bold uppercase tracking-widest">Shop Beach Gear</span>
                        <svg class="w-5 h-5 transition-transform group-hover:translate-x-2" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"></path></svg>
                    </a>
                </div>
            </div>

            <!-- Category 3 -->
            <div class="flex flex-col lg:flex-row w-full bg-white rounded-3xl overflow-hidden premium-shadow fade-in-up">
                <div class="w-full lg:w-1/2 min-h-[500px] relative order-1 lg:order-2 bg-slate-50">
                    <img src="/pawleysislandbeachservice-photo-download-1of1/Website_Photos/DSC05722.JPG" alt="Water Sports" class="absolute inset-0 w-full h-full object-cover" style="object-position: center 20%;">
                </div>
                <div class="w-full lg:w-1/2 p-12 lg:p-24 flex flex-col justify-center relative order-2 lg:order-1">
                    <h3 class="font-serif text-5xl lg:text-6xl text-[#0F172A] leading-tight mb-8">Water Sports.</h3>
                    <p class="font-sans text-slate-500 text-xl font-light leading-relaxed mb-12">Dive into the surf or explore the salt marshes at your own pace with our premium kayaks, paddleboards, and surfboards.</p>
                    <a href="/water-sports.html" class="inline-flex items-center gap-4 text-[#0F172A] hover:text-slate-500 transition-colors group w-max border-b border-[#0F172A] pb-1">
                        <span class="font-sans text-sm font-bold uppercase tracking-widest">Shop Water Sports</span>
                        <svg class="w-5 h-5 transition-transform group-hover:translate-x-2" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"></path></svg>
                    </a>
                </div>
            </div>

        </div>
    </section>'''

# Replace the fleet showcase block in index.html
new_content = re.sub(r'<!-- 4\. FLEET SHOWCASE -->.*?</section>', categories_html, content, flags=re.DOTALL)

with open('c:/Users/mthar/OneDrive/Desktop/Pibs Front/index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)
