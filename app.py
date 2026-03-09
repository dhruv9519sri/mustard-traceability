import streamlit as st
import folium
from streamlit_folium import st_folium
from data import product_data

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Himalayan Mustard Traceability" ,
    page_icon="🍀",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

.stApp {
background-color: #eef7ee;
}

.main {
background-color:#eef6ec;
}

.block-container{
padding-top:2rem;
padding-bottom:2rem;
}
h1,h2,h3{
color:black !important;
font-weight:700;
}
p, span, div {
color:black !important;
}
.card{
background:black;
color:white !important;
padding:20px;
border-radius:12px;
box-shadow:0px 4px 10px rgba(0,0,0,0.06);
margin-bottom:20px; 
}
.hero{
background:linear-gradient(90deg,#2f5d3a,#7bbf6a);
padding:60px;
border-radius:15px;
color:white;
text-align:center;
margin-bottom:40px;
}
.hero h1{
color:white;
font-size:48px;
}
.hero p{
font-size:20px;
}
.timeline{
border-left:3px solid #6aa84f;
padding-left:20px;
margin-left:10px;
}
.timeline-item{
margin-bottom:20px;
}
.gallery img{
border-radius:10px;
}
</style>
"""
, unsafe_allow_html=True)
# ---------------- HERO SECTION ----------------
st.markdown(f"""
<div class="hero">
<h1>{product_data["product_name"]}</h1>
<p>{product_data["tagline"]}</p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

st.header("CLF Profile")

st.markdown("""
    <div class="card">
    Vikash Mahila CLF based in Kalsi block of Dehradun, operates a community owned oil
    extraction unit focused on producing pure, preservatives free mustard oil while supporting
    sustainable rural livelihoods. Responding to the rising demand for chemical free edible
    oils, the enterprise has established itself as a reliable producer of both cold-pressed and
    hot-pressed variants. With a strong emphasis on quality, traceable sourcing, and
    community driven operations, it is emerging as a key player in the regional value chain. Its
    USP includes unadulterated, locally sourced production, naturally high pungency, FSSAI
    certified quality, and rural community ownership. The enterprise records an annual
    turnover of INR 8,13,850.These CLF member are supported by REAP.
    <div>
    """, unsafe_allow_html=True)

st.markdown("""
<div style="display:flex;gap:15px;margin-bottom:25px;flex-wrap:wrap">
<div style="background:#dff2e1;color:#1b5e20;padding:10px 18px;border-radius:20px;font-weight:600">
✅ FSSAI Certified
</div>
<div style="background:#dff2e1;color:#1b5e20;padding:10px 18px;border-radius:20px;font-weight:600">
🌾 Traditional Farming
</div>
<div style="background:#dff2e1;color:#1b5e20;padding:10px 18px;border-radius:20px;font-weight:600">
🏔️ Himalayan Origin
</div>
<div style="background:#dff2e1;color:#1b5e20;padding:10px 18px;border-radius:20px;font-weight:600">
🔍 Traceable Supply Chain
</div>
</div>
"""
, unsafe_allow_html=True)

# ---------------- FARMERS ----------------
st.header("🧑‍🌾🏔️ Our Farmers and Their Village")
col1, col2 = st.columns([1,2])
with col1:
    st.image("farm2.jpeg" , use_container_width=True)
with col2:
    st.markdown("""
    <div class="card">
    <b>Bika Devi (39) and Suba Devi (40)</b><br><br>
    📍 Village: Byas Mari Village, Kalsi Block, Dehradun<br>
    🏔️ Altitude: 780 meters<br><br>
    Bika Devi and Suba Devi, residents of Byas Mari village, are custodians of traditional
    Himalayan mustard seed and practitioners of high altitude farming systems. They cultivate
    crops on steep terraces entirely through family labor, relying on inherited knowledge. To
    enhance the sustainable farm practices, they cultivate using organic method thereby
    sustaining both ecological balance and agricultural productivity. These farmers are
    members of SHG supported by REAP.
    <br><br>
    <b>Village Landscape </b><br><br>
    The geomorphology of Byas Mari village significantly influences local livelihoods and
    agricultural practices. The region is characterized by rugged terrain, steep slopes, and
    dissected valleys shaped by tributaries of the Yamuna River. Agriculture is mainly practiced
    on riverine plains and terraced fields, where fertile alluvial soils support cultivation but
    remain vulnerable to erosion during heavy monsoon rains. Natural springs and
    groundwater sources further support irrigation, enabling small-scale farming despite the
    challenging terrain.
    </div>
    """, unsafe_allow_html=True)
# ---------------- FARMING CALENDAR ----------------
st.header(" Farming Calendar 📆")
c1,c2, = st.columns(2)
c1.metric("🌱 Sowing" , "Oct – Nov")
c2.metric("🌾 Harvest" , "Mar – Apr")
st.markdown("---")
#---------------- Farming Practices ---------
st.header("🚜 Farming Practices")
col1, col2 = st.columns([1,2])
with col1:
    st.markdown("""
    <div class="card">
    <b>Nutrients Management</b><br><br>
    Bio-Fertilizers
    <br><br>
    Vermicompost
    <br><br>
    Jeevamrut
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown("""
    <div class="card">
    <b>Irrigation</b><br><br>
    The produce is irrigated by diverting water from nearby springs using <b>Traditional
    Guhls</b>
    </div>
    """, unsafe_allow_html=True)
# ---------------- PROCESSING ----------------
st.header("⚙ Processing and Quality")
for step in product_data["processing_steps"]:
    st.markdown(f"""
    <div class="card">✔ {step}</div>
    """, unsafe_allow_html=True)
st.markdown("---")
st.header("🚛 Supply Chain Timeline")
st.markdown("""
<div style="
display:flex;
align-items:center;
justify-content:space-between;
background:white;
padding:25px;
border-radius:12px;
box-shadow:0px 3px 8px rgba(0,0,0,0.05);
">
<div style="text-align:center">
🌾 <br>Farm
</div>
<div>➡</div>
<div style="text-align:center">
☀️ <br>Sun Drying
</div>
<div>➡</div>
<div style="text-align:center">
🧹 <br>Sorting
</div>
<div>➡</div>
<div style="text-align:center">
🚚 <br>Vikas Mahila CLF
</div>
<div>➡</div>
<div style="text-align:center">
🛢️ <br>Oil Extraction
</div>
<div>➡</div>
<div style="text-align:center">
📦 <br>Packaging
</div>
<div>➡</div>
<div style="text-align:center">
🏪 <br>Market
</div>
</div>
"""
, unsafe_allow_html=True)
st.markdown("---")
# ---------------- SUPPLY CHAIN ----------------
st.header("🚚 Supply Chain Journey")
st.markdown('<div class="timeline">' , unsafe_allow_html=True)
for step in product_data["supply_chain"]:
    st.markdown(f"""
    <div class="timeline-item">
    ➤ {step}
    </div>
    """, unsafe_allow_html=True)
st.markdown('</div>' , unsafe_allow_html=True)
st.markdown("---")
# ---------------- MAP ----------------
st.header("📍 Farm Location")
lat = 30.515315
lon = 77.843203
farm_map = folium.Map(
    location=[lat,lon],
    zoom_start=14,
    tiles="Esri.WorldImagery"
)
#Marker
folium.Marker(
    [lat,lon],
    tooltip="Mustard Farm" ,
    popup="Byas Mari village"
).add_to(farm_map)
st_folium(farm_map, width=700)
st.markdown("---")
st.header(" Supply Chain Journey Map")
farm_lat = 30.515315
farm_lon = 77.843203
dehradun_lat = 30.3165
dehradun_lon = 78.0322
journey_map = folium.Map(
    location=[30.45,77.95],
    zoom_start=10,
    tiles="Esri.WorldImagery"
)
# Farm Marker
folium.Marker(
    [farm_lat, farm_lon],
    tooltip="Mustard Farm" ,
    popup="Byas Mari Village" ,
    icon=folium.Icon(color="green" , icon="leaf")
).add_to(journey_map)
# Dehradun Hub Marker
folium.Marker(
    [dehradun_lat, dehradun_lon],
    tooltip="Logistics Hub" ,
    popup="Dehradun Pickup Hub" ,
    icon=folium.Icon(color="blue" , icon="truck")
).add_to(journey_map)
# Supply Chain Line
folium.PolyLine(
    [[farm_lat, farm_lon], [dehradun_lat, dehradun_lon]],
    color="yellow" ,
    weight=4
).add_to(journey_map)
st_folium(journey_map, width=900)
st.markdown("---")
# ---------------- Certification ----------
st.header("📜 Certification")
st.markdown("""
<div Class="card">
**✅ FSSAI Licensed Product**
This product is processed and marketed under a valid **FSSAI License**, ensuring
compliance with India's food safety and hygeine standards.
The certification guarantess that the product meets required standards for:
<br><br>
Food safety
<br><br>
Hygiene Practices
<br><br>
Quality assurance
<br><br>
Regulatory compliance
</div>
"""
, unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    st.image("Certificate (1).jpeg" , width=350)
with col2:
    st.image("Certificate (2).jpeg" , width=350)
# ---------------- GALLERY ----------------
st.header("📸 Photo Gallery")
cols = st.columns(3)
for i,img in enumerate(product_data["images"]):
    cols[i % 3].image(img, width=350)
st.markdown("---")
# ---------------- VIDEO ----------------
st.header("📹 Field Video")
video_cols = st.columns(3)
for i, vid in enumerate(product_data["videos"]):
    with video_cols[i % 3]:
        st.video(vid)
