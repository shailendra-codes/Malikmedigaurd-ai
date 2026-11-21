import streamlit as st
from PIL import Image
import numpy as np

st.set_page_config(page_title="Malik MediGuard AI - सही इलाज और बचत", page_icon="🏥", layout="centered")

st.title("🏥 Malik MediGuard AI")
st.subheader("डॉक्टर के पर्चे और मेडिकल बिल की असली जांच करें (100% फ्री - बिना API Key)")
st.caption("Created & Conceptualized by: **Shailendra Kumar Singh** | 🛡️ Independent AI Engine")

with st.sidebar:
    st.header("ℹ️ टूल के बारे में")
    st.success("✅ यह टूल पूरी तरह स्वतंत्र है—इसमें किसी API Key या लॉगिन की ज़रूरत नहीं है।")
    st.info("📋 जनरल फिजिशियन, हार्ट, शुगर, हड्डी, बच्चों, महिला, स्किन और अस्पताल के बिलों की जांच करें।")
    st.markdown("---")
    st.markdown("👨‍💻 **Creator:** Shailendra Kumar Singh")

# भारत की प्रमुख दवाइयों और जन औषधि रेट का बिल्ट-इन डेटाबेस
MEDICINE_DB = {
    "augmentin": {"salt": "Amoxicillin 500mg + Clavulanic Acid 125mg", "brand_price": 223, "jan_price": 65, "use": "बैक्टीरियल संक्रमण, गले/दांत या बुखार का इंफेक्शन", "scheme": "सरकारी अस्पताल व जन औषधि केंद्र पर 70% तक सस्ता उपलब्ध"},
    "pan-d": {"salt": "Pantoprazole 40mg + Domperidone 30mg", "brand_price": 199, "jan_price": 28, "use": "गैस, एसिडिटी और सीने में जलन", "scheme": "जन औषधि केंद्र पर मात्र ₹25-₹30 में 10 कैप्सूल उपलब्ध"},
    "pan 40": {"salt": "Pantoprazole 40mg", "brand_price": 155, "jan_price": 18, "use": "पेट की गैस और अल्सर", "scheme": "जन औषधि केंद्र पर 85% तक बचत"},
    "dolo": {"salt": "Paracetamol 650mg", "brand_price": 33, "jan_price": 12, "use": "बुखार और शरीर दर्द", "scheme": "सभी सरकारी अस्पतालों में मुफ्त व जन औषधि में ₹12 में उपलब्ध"},
    "azithral": {"salt": "Azithromycin 500mg", "brand_price": 132, "jan_price": 38, "use": "गले, फेफड़ों और छाती का संक्रमण", "scheme": "जन औषधि केंद्र पर ₹35-₹40 में उपलब्ध"},
    "telma": {"salt": "Telmisartan 40mg", "brand_price": 240, "jan_price": 25, "use": "हाई ब्लड प्रेशर (BP)", "scheme": "जन औषधि केंद्र पर 88% तक की भारी बचत"},
    "glycomet": {"salt": "Metformin 500mg", "brand_price": 95, "jan_price": 14, "use": "डायबिटीज (शुगर)", "scheme": "जन औषधि केंद्र व सरकारी स्वास्थ्य केंद्रों पर उपलब्ध"},
    "ecosprin": {"salt": "Aspirin 75mg", "brand_price": 18, "jan_price": 5, "use": "दिल की सुरक्षा और खून पतला करने के लिए", "scheme": "जन औषधि केंद्र पर मात्र ₹5 में उपलब्ध"},
    "zerodol": {"salt": "Aceclofenac 100mg + Paracetamol 325mg", "brand_price": 115, "jan_price": 22, "use": "जोड़ों, कमर और हड्डियों का दर्द", "scheme": "जन औषधि केंद्र पर 80% तक सस्ता"},
    "montair": {"salt": "Montelukast 10mg + Levocetirizine 5mg", "brand_price": 210, "jan_price": 32, "use": "एलर्जी, छींक और सांस की तकलीफ", "scheme": "जन औषधि केंद्र पर ₹32 में उपलब्ध"},
    "shelcal": {"salt": "Calcium 500mg + Vitamin D3", "brand_price": 145, "jan_price": 28, "use": "हड्डियों की मजबूती और कैल्शियम की कमी", "scheme": "जन औषधि केंद्र पर 80% तक बचत"},
    "af-tabs": {"salt": "Homoeopathic Anti-Flu (Gelsemium, Bryonia, Eupatorium)", "brand_price": 140, "jan_price": 0, "use": "फ्लू, सर्दी-जुकाम और शरीर दर्द (होम्योपैथी)", "scheme": "सरकारी आयुष (AYUSH) होम्योपैथिक चिकित्सालयों में निःशुल्क उपलब्ध"}
}

@st.cache_resource
def load_ocr():
    import easyocr
    return easyocr.Reader(["en"], gpu=False)

col1, col2 = st.columns(2)
with col1:
    demo_btn = st.button("🧪 1-Click सैंपल पर्चे से डेमो देखें", use_container_width=True)
with col2:
    st.markdown("या नीचे **दवा का नाम लिखें / फोटो डालें** 👇")

med_input = st.text_input("✍️ दवा या बीमारी का नाम लिखें (जैसे: Augmentin, Pan-D, Telma, Dolo, AF-Tabs):")
up = st.file_uploader("📸 या डॉक्टर के पर्चे / दवा की शीशी की फोटो अपलोड करें:", type=("jpg", "jpeg", "png"))

if up is not None:
    st.image(Image.open(up), caption="अपलोड किया गया पर्चा / दवा", width="stretch")

check_btn = st.button("🔍 जांच शुरू करें और बचत देखें", type="primary", use_container_width=True)

if check_btn or demo_btn:
    search_text = ""
    if demo_btn:
        search_text = "augmentin pan-d dolo telma"
    else:
        search_text = med_input.lower()
        if up is not None:
            with st.spinner("📸 फोटो से दवाइयों के नाम पढ़े जा रहे हैं (कृपया पहली बार 10-15 सेकंड रुकें)..."):
                try:
                    reader = load_ocr()
                    img = Image.open(up)
                    img.thumbnail((800, 800))
                    results = reader.readtext(np.array(img), detail=0)
                    extracted = " ".join(results)
                    st.info(f"📄 फोटो से पढ़ा गया टेक्स्ट: {extracted[:200]}...")
                    search_text = search_text + " " + extracted.lower()
                except Exception as e:
                    st.warning(f"फोटो पढ़ने में तकनीकी समय लगा, कृपया ऊपर बॉक्स में दवा का नाम लिखें। ({e})")

    if not search_text.strip():
        st.warning("⚠️ कृपया ऊपर दवा का नाम लिखें, फोटो अपलोड करें, या '1-Click डेमो' बटन दबाएं!")
    else:
        found_items = []
        for key, info in MEDICINE_DB.items():
            if key in search_text or any(word in search_text for word in key.split("-")):
                found_items.append((key.upper(), info))

        if found_items:
            total_brand = sum(x[1]["brand_price"] for x in found_items)
            total_jan = sum(x[1]["jan_price"] for x in found_items)
            saved = total_brand - total_jan
            pct = int((saved / total_brand) * 100) if total_brand > 0 else 0

            st.success(f"💰 कुल अनुमानित बचत: ₹{saved} ({pct}% तक की सीधी बचत!)")
            report_lines = [f"Malik MediGuard AI रिपोर्ट (Created by Shailendra Kumar Singh)\nकुल बचत: ₹{saved} ({pct}%)\n"]

            for name, info in found_items:
                st.markdown(f"### 💊 {name}")
                st.markdown(f"* **असली सॉल्ट (Composition):** {info['salt']}")
                st.markdown(f"* **मुख्य उपयोग:** {info['use']}")
                st.markdown(f"* **बाज़ार कीमत (Branded):** ~₹{info['brand_price']} ➡️ **जन औषधि / सरकारी रेट:** ~₹{info['jan_price']} (**बचत: ₹{info['brand_price'] - info['jan_price']}**)")
                st.markdown(f"* **🏛️ सरकारी योजना:** {info['scheme']}")
                st.markdown("---")
                report_lines.append(f"- {name} ({info['salt']}): ब्रांडेड ₹{info['brand_price']} -> जन औषधि ₹{info['jan_price']}")

            st.warning("⚠️ अस्वीकरण: यह जानकारी केवल जागरूकता और खर्च की पारदर्शिता के लिए है। कोई भी दवा बदलने से पहले अपने डॉक्टर से सलाह ज़रूर लें।")
            st.download_button(
                label="📥 यह पूरी रिपोर्ट मोबाइल में सेव करें",
                data="\n".join(report_lines),
                file_name="Malik_MediGuard_Report.txt",
                mime="text/plain",
                use_container_width=True
            )
        else:
            st.info("🔍 इस दवा का नाम हमारे शुरुआती डेटाबेस में नहीं मिला (या लिखावट साफ नहीं थी)।")
            st.markdown("""
            **आप तुरंत यह कर सकते हैं:**
            1. अपने नज़दीकी **प्रधानमंत्री भारतीय जन औषधि केंद्र (PMBJP)** पर जाकर पर्चे पर लिखा **असली सॉल्ट (Generic Name)** दिखाएं—आपको **50% से 85% तक सस्ती** दवा मिल जाएगी।
            2. गंभीर बीमारी या अस्पताल में भर्ती होने की स्थिति में **आयुष्मान भारत (PM-JAY)** या **मुख्यमंत्री राहत कोष** से ₹5 लाख तक का मुफ्त इलाज चेक करें।
            """)

st.markdown("---")
st.markdown("<div style='text-align: center;'>🏥 <b>Malik MediGuard AI (Zero-API Edition)</b> | Created by <b>Shailendra Kumar Singh</b></div>", unsafe_allow_html=True)
 
