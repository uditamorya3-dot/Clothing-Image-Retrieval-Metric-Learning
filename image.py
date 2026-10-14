from PIL import Image, ImageDraw, ImageFont
import os

os.makedirs("static/images", exist_ok=True)

def make_pro_jacket(filename, color, brand, name):
    # Ek mast jacket jaisi image banayenge
    img = Image.new('RGB', (600, 700), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    
    # Jacket ka body
    draw.rectangle([80, 50, 520, 650], fill=color, outline=(0,0,0), width=3)
    # Hood
    draw.ellipse([180, 10, 420, 180], fill=color, outline=(0,0,0), width=3)
    # Zip
    draw.rectangle([290, 50, 310, 650], fill=(0,0,0))
    # Pockets
    draw.rectangle([120, 400, 200, 500], fill=(240,240,240), outline=(0,0,0), width=2)
    draw.rectangle([400, 400, 480, 500], fill=(240,240,240), outline=(0,0,0), width=2)
    # Brand logo
    draw.text((200, 200), brand, fill="white")
    draw.text((200, 550), name, fill="white")
    draw.text((200, 580), "Outdoor Pro", fill="white")
    
    img.save(f"static/images/{filename}")
    print(f"✅ Ban gaya: {filename}")

# 4 pro jackets
make_pro_jacket("trekking.jpg", (30, 90, 200), "COLUMBIA", "Trekking Jacket")
make_pro_jacket("waterfall.jpg", (200, 30, 30), "WILDCRAFT", "Waterfall Jacket")
make_pro_jacket("hiking.jpg", (40, 130, 40), "DECATHLON", "Hiking Shirt")
make_pro_jacket("dailywear.jpg", (25, 25, 25), "QUECHUA", "Dailywear Jacket")

print("\nAll 4 PRO images ready! Ab streamlit run app.py chala")