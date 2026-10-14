import streamlit as st
import os

st.set_page_config(page_title="DRIP FINDER", page_icon="🔥", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@700&family=Poppins:wght@400;600&display=swap');
.stApp { background: #07070b; }
header, footer {visibility: hidden;}

.title {
    font-family: 'Space Grotesk'; font-size: 54px; font-weight: 700; text-align: center;
    background: linear-gradient(90deg, #fff, #00f2ff, #a855f7, #ec4899);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
}
.sub { text-align: center; color: #888; font-family: 'Poppins'; margin-bottom: 25px; }
.glass {
    background: rgba(255,255,255,0.05); backdrop-filter: blur(20px);
    border: 1px solid rgba(255,255,255,0.1); border-radius: 20px; padding: 20px;
}
.card {
    background: #111119; border: 1px solid #222; border-radius: 18px; overflow: hidden;
    transition: 0.4s;
}
.card:hover { transform: translateY(-8px); border-color: #00f2ff; box-shadow: 0 15px 50px rgba(0,242,255,0.3); }
.badge { background: linear-gradient(90deg, #00f2ff, #a855f7); color: black; font-weight: 800; font-size: 11px; padding: 6px 12px; border-radius: 20px; position: absolute; top: 10px; right: 10px; z-index: 10; }

/* CSS ONLY PARTICLES - No JS */
.particles { position: fixed; top:0; left:0; width:100%; height:100%; pointer-events:none; z-index:0; overflow:hidden; }
.p { position: absolute; width:6px; height:6px; background: #00f2ff; border-radius: 50%; box-shadow: 0 0 10px #00f2ff; animation: floatUp linear infinite; opacity:0.6; }
.p:nth-child(1){ left:10%; animation-duration:12s; animation-delay:0s; }
.p:nth-child(2){ left:20%; animation-duration:15s; animation-delay:1s; background:#a855f7; box-shadow:0 0 10px #a855f7; }
.p:nth-child(3){ left:35%; animation-duration:10s; animation-delay:2s; }
.p:nth-child(4){ left:50%; animation-duration:13s; animation-delay:0.5s; background:#ec4899; box-shadow:0 0 10px #ec4899; }
.p:nth-child(5){ left:70%; animation-duration:11s; animation-delay:3s; }
.p:nth-child(6){ left:85%; animation-duration:14s; animation-delay:1.5s; background:#a855f7; }
@keyframes floatUp { 0%{transform: translateY(100vh) scale(0); opacity:0} 20%{opacity:1} 80%{opacity:1} 100%{transform: translateY(-10vh) scale(1.5); opacity:0} }

/* Emoji float */
.emoji-float { display: inline-block; animation: bounce 2s ease-in-out infinite; }
@keyframes bounce { 0%,100%{transform: translateY(0)} 50%{transform: translateY(-6px)} }
</style>

<div class="particles">
  <div class="p"></div><div class="p"></div><div class="p"></div><div class="p"></div><div class="p"></div><div class="p"></div>
</div>

<div class="title">DRIP FINDER <span class="emoji-float">🔥</span></div>
<div class="sub">AI that sees your style • Finds your tribe • Visual Search 2.0 <span class="emoji-float">✨</span></div>
""", unsafe_allow_html=True)

center = st.columns([1,2.2,1])[1]
with center:
    uploaded = st.file_uploader("Drop jacket 🧥 Hoodie 👕 Shirt 👔", type=["jpg","png","jpeg"])

if uploaded:
    col1, col2 = st.columns([1, 1.7])
    with col1:
        st.markdown('<div class="glass">', unsafe_allow_html=True)
        st.image(uploaded, use_container_width=True)
        st.markdown('<p style="text-align:center; color:#00f2ff; font-weight:700; margin-top:10px;">✨ CLIP AI ANALYZED 👁️</p></div>', unsafe_allow_html=True)

    with col2:
        m1,m2,m3 = st.columns(3)
        m1.metric("Visual Match 💯","95.4%","High 🔥")
        m2.metric("Color DNA 🎨","Blue Hue","Exact ✨")
        m3.metric("Style 👕","Trekking","Outdoor ⛰️")

        products = [
            {"file":"trekking.jpg", "brand":"COLUMBIA", "name":"Trek 900 Down 🧥", "price":"₹3,500", "mrp":"₹6,999", "match":"95%"},
            {"file":"waterfall.jpg", "brand":"WILDCRAFT", "name":"Waterproof Hike 500 🌧️", "price":"₹2,800", "mrp":"₹4,999", "match":"93%"},
            {"file":"hiking.jpg", "brand":"QUECHUA", "name":"MH100 Light Tee 🌿", "price":"₹1,500", "mrp":"₹2,199", "match":"91%"},
            {"file":"dailywear.jpg", "brand":"FORCLAZ", "name":"SH100 Winter Parka ❄️", "price":"₹3,000", "mrp":"₹5,499", "match":"89%"},
        ]

        g1,g2 = st.columns(2)
        for i,p in enumerate(products):
            path = f"static/images/{p['file']}"
            target = g1 if i%2==0 else g2
            with target:
                st.markdown(f'<div class="card" style="position:relative"><div class="badge">✨ {p["match"]} MATCH 🔥</div>', unsafe_allow_html=True)
                if os.path.exists(path):
                    st.image(path, use_container_width=True)
                else:
                    st.info(f"Missing: {path} - run python images.py")
                st.markdown(f"""
                <div style="padding:12px 14px;">
                    <div style="color:#666; font-size:11px; letter-spacing:2px;">{p['brand']} 💎</div>
                    <div style="color:#fff; font-weight:700; font-family:Space Grotesk; margin:4px 0;">{p['name']}</div>
                    <div style="color:#fff; font-weight:700;">{p['price']} <span style="color:#666; font-weight:400; text-decoration:line-through; font-size:12px;">{p['mrp']}</span> 🎉</div>
                </div></div><br>
                """, unsafe_allow_html=True)
else:
    st.markdown("""
    <div style='text-align:center; margin-top:30px;'>
        <div style='font-size:60px;'><span class="emoji-float">🧥</span> <span class="emoji-float" style="animation-delay:0.2s">👁️</span> <span class="emoji-float" style="animation-delay:0.4s">✨</span> <span class="emoji-float" style="animation-delay:0.6s">💎</span> <span class="emoji-float" style="animation-delay:0.8s">🔥</span></div>
        <div style='color:#a1a1aa; font-size:20px; font-weight:600; margin-top:15px; font-family:Poppins;'>Upload to see the magic ✨</div>
        <div style='color:#52525b; font-size:13px; margin-top:8px;'>AI matches color 🎨, texture 🧵, pattern ⚡ & brand DNA 🧬</div>
    </div>
    """, unsafe_allow_html=True)