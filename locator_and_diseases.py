import urllib.parse
import streamlit as st

st.set_page_config(page_title="Malik MediGuard - बीमारी व अस्पताल लोकेटर", page_icon="📍")
st.title("📍 जन औषधि व आयुष्मान अस्पताल लोकेटर")
st.caption("Created by: **Shailendra Kumar Singh** | Malik MediGuard AI Extension")

DISEASE_GUIDE = {
    "बुखार / बदन दर्द (Fever)": ("Paracetamol 650mg (Dolo)", "₹33", "₹12", "सरकारी अस्पतालों में निःशुल्क व जन औषधि में ₹12 में"),
    "गैस / एसिडिटी (Gas & Acidity)": ("Pantoprazole 40mg + Domperidone 30mg (Pan-D)", "₹199", "₹28", "जन औषधि केंद्र पर मात्र ₹28 में 10 कैप्सूल"),
    "हाई ब्लड प्रेशर (High BP)": ("Telmisartan 40mg (Telma 40)", "₹240", "₹25", "जन औषधि केंद्र पर 88% तक की सीधी बचत"),
    "शुगर / मधुमेह (Diabetes)": ("Metformin 500mg (Glycomet)", "₹95", "₹14", "जन औषधि केंद्र व सरकारी स्वास्थ्य केंद्रों पर उपलब्ध"),
    "जोड़ों व कमर दर्द (Joint/Body Pain)": ("Aceclofenac 100mg + Paracetamol 325mg (Zerodol-P)", "₹115", "₹22", "जन औषधि केंद्र पर ₹22 में उपलब्ध"),
    "सर्दी-जुकाम / एलर्जी (Cold & Allergy)": ("Montelukast 10mg + Levocetirizine 5mg (Montair-LC)", "₹210", "₹32", "जन औषधि केंद्र पर ₹32 में उपलब्ध"),
    "गले का इन्फेक्शन (Throat Infection)": ("Azithromycin 500mg (Azithral 500)", "₹132", "₹38", "जन औषधि केंद्र पर ₹38 में उपलब्ध"),
    "कैल्शियम व कमजोरी (Calcium & Vitamin)": ("Calcium 500mg + Vitamin D3 (Shelcal 500)", "₹145", "₹28", "जन औषधि केंद्र पर 80% तक की बचत")
}

st.subheader("1️⃣ बीमारी चुनकर सस्ती जन औषधि दवा देखें")
selected_disease = st.selectbox("अपनी समस्या या बीमारी चुनें:", list(DISEASE_GUIDE.keys()))

if selected_disease:
    salt, brand_p, jan_p, scheme = DISEASE_GUIDE[selected_disease]
    st.success(f"💊 **असली सॉल्ट:** {salt}")
    st.info(f"💰 **बाज़ार कीमत:** {brand_p} ➡️ **जन औषधि रेट:** {jan_p} | **🏛️ योजना:** {scheme}")

st.markdown("---")
st.subheader("2️⃣ अपने शहर में जन औषधि केंद्र और आयुष्मान अस्पताल खोजें")
city = st.text_input("🏙️ अपने शहर या जिले का नाम लिखें:", value="Jaunpur")

if city.strip():
    q_jan = urllib.parse.quote(f"Jan Aushadhi Kendra near {city}")
    q_ayushman = urllib.parse.quote(f"Ayushman Bharat empaneled hospitals in {city}")
    q_govt = urllib.parse.quote(f"District Government Hospital {city}")

    st.link_button(f"💊 {city} के नज़दीकी 'जन औषधि केंद्र' मैप पर देखें", f"https://google.com{q_jan}", use_container_width=True)
    st.link_button(f"🏨 {city} के 'आयुष्मान भारत (PM-JAY)' अस्पताल देखें", f"https://google.com{q_ayushman}", use_container_width=True)
    st.link_button(f"🏛️ {city} का सरकारी जिला अस्पताल खोजें", f"https://google.com{q_govt}", use_container_width=True)

st.markdown("---")
st.warning("⚠️ अस्वीकरण: यह जानकारी केवल जागरूकता के लिए है। कोई भी दवा लेने से पहले डॉक्टर से सलाह ज़रूर लें।")
st.markdown("<div style='text-align: center;'>🏥 <b>Malik MediGuard AI</b> | Created by <b>Shailendra Kumar Singh</b></div>", unsafe_allow_html=True)
 
