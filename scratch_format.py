import re

bikes_data = [
    ('beach-bike-rental', 'Standard Beach Cruiser', 'Comfortable and easy to ride. The classic island experience.', '/pawleysislandbeachservice-photo-download-1of1/Website_Photos/DSC05753.JPG', True),
    ('trail-bike', 'Trail Bike', 'Perfect for longer rides and exploring the island paths.', '/pawleysislandbeachservice-photo-download-1of1/Website_Photos/DSC05748.JPG', True),
    ('tandem-bike', 'Tandem Bike', 'Double the fun! Explore Pawleys with a partner.', '/pawleysislandbeachservice-photo-download-1of1/Website_Photos/DSC05750.JPG', True),
    ('adult-trike', 'Adult Trike', 'Maximum stability and comfort for an easy ride.', '/pawleysislandbeachservice-photo-download-1of1/Website_Photos/DSC05752.JPG', True)
]

beach_data = [
    ('beach-chair', 'Premium Beach Chair', 'High-end aluminum chair with wooden armrests.', '/pawleysislandbeachservice-photo-download-1of1/Website_Photos/DSC05760.JPG', False),
    ('wood-chair', 'Classic Wood Chair', 'Traditional and sturdy for a classic beach day.', '/pawleysislandbeachservice-photo-download-1of1/Website_Photos/DSC05754.JPG', False),
    ('beach-umbrella', 'Canvas Beach Umbrella', 'Provide excellent shade with a classic look.', '/pawleysislandbeachservice-photo-download-1of1/Website_Photos/DSC05761.JPG', False),
    ('augbrella', 'Augbrella', 'Heavy-duty umbrella anchor system.', '/pawleysislandbeachservice-photo-download-1of1/Website_Photos/DSC05755.JPG', False),
    ('shibumi-shade', 'Shibumi Shade', 'Wind-powered shade canopy for the whole family.', '/pawleysislandbeachservice-photo-download-1of1/Website_Photos/DSC05756.JPG', False),
    ('roll-away-bed', 'Roll-Away Bed', 'Comfortable twin folding guest bed.', '/pawleysislandbeachservice-photo-download-1of1/Website_Photos/DSC05757.JPG', False)
]

water_data = [
    ('kayak', 'Single Kayak', 'Explore the salt marshes at your own pace.', '/pawleysislandbeachservice-photo-download-1of1/Website_Photos/DSC05722.JPG', False),
    ('kayak-tandem', 'Tandem Kayak', 'Share the adventure on the water.', '/pawleysislandbeachservice-photo-download-1of1/Website_Photos/DSC05758.JPG', False),
    ('paddleboard', 'Stand Up Paddleboard', 'Glide smoothly across the calm waters.', '/pawleysislandbeachservice-photo-download-1of1/Website_Photos/DSC05762.JPG', False),
    ('surfboard', 'Soft-Top Surfboard', 'Perfect for catching your first waves.', '/pawleysislandbeachservice-photo-download-1of1/Website_Photos/DSC05764.JPG', False),
    ('body-board', 'Body Board', 'Fun in the surf for all ages.', '/pawleysislandbeachservice-photo-download-1of1/Website_Photos/DSC05759.JPG', False)
]

def render_cards(items):
    html = ''
    for i, (slug, title, desc, img, is_bike) in enumerate(items):
        delay = (i % 3) * 100
        
        # Determine ordering for alternating layout
        image_order = 'order-1 lg:order-2' if i % 2 != 0 else 'order-1'
        text_order = 'order-2 lg:order-1' if i % 2 != 0 else 'order-2'
        
        img_html = f'''<img src="{img}" alt="{title}" class="absolute inset-0 w-full h-full object-cover">''' if img else f'''<span class="text-slate-300 font-serif italic text-2xl absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2">Premium Quality</span>'''
        
        addon_html = ""
        if is_bike:
            addon_html = '''
                        <div class="bg-slate-50 border border-slate-100 rounded-2xl p-6 mb-10">
                            <h4 class="font-sans text-xs font-bold text-[#0F172A] uppercase tracking-widest mb-2">Available Add-ons</h4>
                            <p class="font-sans text-slate-500 text-sm leading-relaxed">Customize your rental at checkout with our premium add-ons: Bike Baskets, Child Bike Seats, Child Trailers, and Safety Helmets.</p>
                        </div>
'''

        html += f'''
                <!-- {slug} -->
                <div class="flex flex-col lg:flex-row w-full bg-white rounded-3xl overflow-hidden premium-shadow mb-16 fade-in-up delay-{delay}">
                    <!-- Image Side -->
                    <div class="w-full lg:w-1/2 min-h-[400px] relative {image_order} bg-slate-50">
                        {img_html}
                    </div>
                    <!-- Content Side -->
                    <div class="w-full lg:w-1/2 p-12 lg:p-24 flex flex-col justify-center relative {text_order}">
                        <h3 class="font-serif text-4xl lg:text-5xl text-[#0F172A] leading-tight mb-8">{title}</h3>
                        <p class="font-sans text-slate-500 text-lg font-light leading-relaxed mb-10">{desc}</p>
                        {addon_html}
                        <div class="pt-8 border-t border-slate-100">
                            <div class="booqable-product-button" data-id="{slug}"></div>
                        </div>
                    </div>
                </div>'''
    return html

bikes_html = f'''
            <!-- BIKES & CRUISERS -->
            <div class="flex flex-col md:flex-row justify-between items-end mb-16 fade-in-up">
                <div class="max-w-2xl">
                    <h2 class="font-serif text-5xl text-[#0F172A] leading-tight">Bikes & Cruisers.</h2>
                </div>
            </div>
            <div class="flex flex-col w-full">
{render_cards(bikes_data)}
            </div>
'''

beach_html = f'''
            <!-- BEACH RENTALS -->
            <div class="flex flex-col md:flex-row justify-between items-end mb-16 mt-32 fade-in-up">
                <div class="max-w-2xl">
                    <h2 class="font-serif text-5xl text-[#0F172A] leading-tight">Beach Rentals.</h2>
                </div>
            </div>
            <div class="flex flex-col w-full">
{render_cards(beach_data)}
            </div>
'''

water_html = f'''
            <!-- WATER SPORTS -->
            <div class="flex flex-col md:flex-row justify-between items-end mb-16 mt-32 fade-in-up">
                <div class="max-w-2xl">
                    <h2 class="font-serif text-5xl text-[#0F172A] leading-tight">Water Sports.</h2>
                </div>
            </div>
            <div class="flex flex-col w-full">
{render_cards(water_data)}
            </div>
'''

full_fleet = f'''
    <!-- 4. FLEET SHOWCASE -->
    <section id="fleet" class="w-full py-32 px-6 lg:px-12 bg-[#FAFAFA]">
        <div class="max-w-7xl mx-auto">
            {bikes_html}
            {beach_html}
            {water_html}
        </div>
    </section>
'''

# Read index.html
with open('c:/Users/mthar/OneDrive/Desktop/Pibs Front/index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

# Replace the fleet showcase
new_index = re.sub(r'<!-- 4\. FLEET SHOWCASE -->.*?(?=<!-- 5\. 50/50 SPLIT CONTAINER)', full_fleet, index_content, flags=re.DOTALL)

with open('c:/Users/mthar/OneDrive/Desktop/Pibs Front/index.html', 'w', encoding='utf-8') as f:
    f.write(new_index)

# Now for subpages
def update_subpage(filepath, content):
    with open(filepath, 'r', encoding='utf-8') as f:
        file_content = f.read()
    
    # Check if there is a fleet section already
    if '<!-- BIKES & CRUISERS -->' in file_content or '<!-- BEACH RENTALS -->' in file_content or '<!-- WATER SPORTS -->' in file_content:
        # replace existing section
        replacement = f'''    <section class="w-full py-32 px-6 lg:px-12 bg-[#FAFAFA] min-h-screen">
        <div class="max-w-7xl mx-auto mt-20">
            {content}
        </div>
    </section>'''
        new_content = re.sub(r'<section class="w-full py-32 px-6 lg:px-12 bg-\[#FAFAFA\] min-h-screen">.*?</section>', replacement, file_content, flags=re.DOTALL)
    else:
        # replace the min-h-screen py-32 px-12 text-center
        replacement = f'''    <section class="w-full py-32 px-6 lg:px-12 bg-[#FAFAFA] min-h-screen">
        <div class="max-w-7xl mx-auto mt-20">
            {content}
        </div>
    </section>'''
        new_content = re.sub(r'<div class="min-h-screen py-32 px-12 text-center">.*?</div>', replacement, file_content, flags=re.DOTALL)
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

# We also need to fix the first section spacing for subpages (remove mt-32 if it's the first section)
beach_html_first = beach_html.replace('mt-32', '')
water_html_first = water_html.replace('mt-32', '')

update_subpage('c:/Users/mthar/OneDrive/Desktop/Pibs Front/bikes.html', bikes_html)
update_subpage('c:/Users/mthar/OneDrive/Desktop/Pibs Front/beach-gear.html', beach_html_first)
update_subpage('c:/Users/mthar/OneDrive/Desktop/Pibs Front/water-sports.html', water_html_first)
