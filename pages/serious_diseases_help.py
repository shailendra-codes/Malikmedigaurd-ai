import urllib.parse
import streamlit as st

st.set_page_config(page_title="गंभीर बीमारी सरकारी मदद - Malik MediGuard AI", page_icon="🏛️")
st.title("🏛️ गंभीर बीमारियों के लिए सरकारी मुफ्त इलाज और बचत गाइड")
st.caption("Created by: **Shailendra Kumar Singh** | Malik MediGuard Critical Care Support")

st.info("कैंसर, किडनी, हार्ट सर्जरी, टीबी (TB) और गंभीर बीमारियों में लाखों रुपये बचाने के लिए भारत और उत्तर प्रदेश सरकार की अधिकृत योजनाओं की जानकारी:")

SERIOUS_DB = {
    "कैंसर (Cancer / Chemotherapy)": {
        "medicine_help": "💊 **AMRIT Pharmacy (अमृत फार्मेसी):** केंद्र सरकार के अमृत स्टोर पर कैंसर (Chemotherapy) और महंगे इम्प्लांट्स की दवाइयां बाजार से **60% से 90% तक सस्ती** मिलती हैं।",
        "govt_scheme": "🏥 **आयुष्मान भारत (PM-JAY) + प्रधानमंत्री/मुख्यमंत्री राहत कोष:** आयुष्मान कार्ड पर ₹5 लाख तक का कैशलेस इलाज, और कार्ड न होने पर **PMNRF** या **UP मुख्यमंत्री विवेकाधीन कोष** से सीधा अस्पताल के खाते में लाखों रुपये की आर्थिक सहायता मिलती है।",
        "nearby_center": "📍 **नज़दीकी प्रमुख केंद्र (UP / पूर्वांचल):** होमी भाभा कैंसर अस्पताल एवं महामना पंडित मदन मोहन मालवीय कैंसर सेंटर (Tata Memorial), वाराणसी (BHU परिसर) — यहाँ बेहद कम खर्च या मुफ्त में विश्वस्तरीय इलाज होता है।"
    },
    "किडनी और डायलिसिस (Kidney / Dialysis)": {
        "medicine_help": "💊 **जन औषधि केंद्र:** किडनी, BP और इम्यूनोसप्रेसेंट दवाइयां जन औषधि केंद्र पर 80% तक सस्ती मिलती हैं।",
        "govt_scheme": "🏥 **प्रधानमंत्री राष्ट्रीय डायलिसिस कार्यक्रम (PMNDP):** देश के सभी जिला सरकारी अस्पतालों (जैसे जिला अस्पताल जौनपुर) में बीपीएल/आयुष्मान मरीज़ों के लिए **डायलिसिस पूरी तरह निःशुल्क** है।",
        "nearby_center": "📍 **नज़दीकी केंद्र:** जिला चिकित्सालय (जौनपुर), IMS-BHU (वाराणसी), और SGPGI (लखनऊ)।"
    },
    "हार्ट सर्जरी / स्टेंट / बाईपास (Heart Surgery & Stent)": {
        "medicine_help": "💊 **NPPA सरकारी रेट कैपिंग & जन औषधि:** सरकार ने हार्ट स्टेंट (Stent) की कीमतें फिक्स कर दी हैं, और खून पतला करने व कोलेस्ट्रॉल की दवाइयां जन औषधि पर ₹10-₹25 में मिलती हैं।",
        "govt_scheme": "🏥 **आयुष्मान भारत (PM-JAY):** एंजियोप्लास्टी, स्टेंट और बाईपास सर्जरी आयुष्मान भारत के पैनल अस्पतालों में **100% मुफ्त (कैशलेस)** होती है।",
        "nearby_center": "📍 **नज़दीकी केंद्र:** BHU हृदय रोग विभाग (वाराणसी), LPS इंस्टीट्यूट ऑफ कार्डियोलॉजी (कानपुर), और आयुष्मान सूचीबद्ध निजी अस्पताल।"
    },
    "टीबी / क्षय रोग (Tuberculosis - TB)": {
        "medicine_help": "💊 **DOTS / नि-क्षय केंद्र:** टीबी की पूरी दवा सरकारी स्वास्थ्य केंद्रों पर **100% मुफ्त** दी जाती है।",
        "govt_scheme": "💰 **नि-क्षय पोषण योजना (Nikshay Poshan Yojana):** इलाज चलने तक सरकार हर महीने मरीज़ के बैंक खाते में **₹1,000 पोषण (खाने-पीने) के लिए** सीधे भेजती है।",
        "nearby_center": "📍 **नज़दीकी केंद्र:** नज़दीकी सामुदायिक स्वास्थ्य केंद्र (CHC), प्राथमिक स्वास्थ्य केंद्र (PHC) या जिला क्षय रोग केंद्र (जौनपुर)।"
    },
    "न्यूरो / ब्रेन / रीढ़ की सर्जरी (Neuro & Spine)": {
        "medicine_help": "💊 **जन औषधि एवं अमृत फार्मेसी:** नसों और दिमाग की महंगी दवाइयां जन औषधि केंद्र पर 75-85% सस्ती उपलब्ध हैं।",
        "govt_scheme": "🏥 **आयुष्मान भारत एवं राज्य बीमारी सहायता निधि:** गंभीर न्यूरो सर्जरी के लिए आयुष्मान कार्ड और मुख्यमंत्री राहत कोष से पूरी मदद मिलती है।",
        "nearby_center": "📍 **नज़दीकी केंद्र:** IMS-BHU ट्रॉमा सेंटर (वाराणसी) और KGMU / SGPGI (लखनऊ)।"
    }
}

disease = st.selectbox("अपनी या परिवार की गंभीर बीमारी चुनें:", list(SERIOUS_DB.keys()))

if disease:
    data = SERIOUS_DB[disease]
    st.success(f"### 🩺 {disease} — संपूर्ण सहायता रिपोर्ट")
    st.markdown(data["medicine_help"])
    st.markdown(data["govt_scheme"])
    st.info(data["nearby_center"])

st.markdown("---")
st.subheader("📍 अपने शहर में अमृत फार्मेसी और आयुष्मान अस्पताल खोजें")
city = st.text_input("🏙️ शहर या जिले का नाम लिखें:", value="Jaunpur")

if city.strip():
    q_amrit = urllib.parse.quote(f"AMRIT Pharmacy near {city} Varanasi")
    q_ayushman = urllib.parse.quote(f"Ayushman Bharat empaneled hospitals in {city}")
    st.link_button(f"💊 नज़दीकी 'AMRIT Pharmacy' (सस्ती कैंसर/गंभीर दवा) मैप पर देखें", f"https://google.com{q_amrit}", use_container_width=True)
    st.link_button(f"🏨 {city} के 'आयुष्मान भारत (PM-JAY)' अस्पताल देखें", f"https://google.com{q_ayushman}", use_container_width=True)

st.markdown("---")
st.markdown("**🔗 सरकारी सहायता के सीधे लिंक:**")
st.markdown("* [आयुष्मान भारत (PM-JAY) पात्रता व कार्ड डाउनलोड](https://nha.gov.in)")
st.markdown("* [अमृत फार्मेसी (AMRIT Stores) आधिकारिक वेबसाइट](https://amritpharmacy.gov.in)")
st.warning("⚠️ अस्वीकरण: यह जानकारी जन-जागरूकता के लिए है। इलाज और योजना की पात्रता के लिए संबंधित अस्पताल के आयुष्मान मित्र या डॉक्टर से संपर्क करें।")
st.markdown("<div style='text-align: center;'>🏥 <b>Malik MediGuard AI</b> | Created by <b>Shailendra Kumar Singh</b></div>", unsafe_allow_html=True)
