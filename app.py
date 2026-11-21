import time
import streamlit as st
from google import genai
from PIL import Image

# 1. वेबसाइट का पेज सेटअप और ब्रांडिंग
st.set_page_config(page_title="Malik MediGuard AI - सही इलाज और बचत", page_icon="🏥")
st.title("🏥 Malik MediGuard AI")
st.subheader("डॉक्टर के पर्चे और मेडिकल बिल की असली जांच करें")
st.caption("Created & Conceptualized by: **Shailendra Kumar Singh** | 🛡️ Self-Healing AI System")

# 2. किन-किन डॉक्टरों के पर्चे पढ़ सकता है
with st.expander("📋 यह टूल किन-किन डॉक्टरों के पर्चे और बिल पढ़ सकता है? (यहाँ क्लिक करें)", expanded=True):
    st.markdown("""
    **Malik MediGuard AI** भारत के लगभग हर विशेषज्ञ (Specialist) और सामान्य डॉक्टर के हाथ से लिखे या प्रिंटेड पर्चे को पढ़ सकता है:
    * 🩺 **जनरल फिजिशियन (General Physician):** बुखार, सर्दी-जुकाम, संक्रमण और सामान्य बीमारियां।
    * ❤️ **हृदय रोग विशेषज्ञ (Cardiologist):** BP, कोलेस्ट्रॉल, ECG और दिल की बीमारियों के पर्चे।
    * 🦴 **हड्डी रोग विशेषज्ञ (Orthopedic):** जोड़ों का दर्द, फ्रैक्चर, कमर दर्द और कैल्शियम/विटामिन की दवाइयां।
    * 👶 **बाल रोग विशेषज्ञ (Pediatrician):** बच्चों के सिरप, ड्रॉप्स और टीकाकरण के पर्चे।
    * 👩‍⚕️ **स्त्री रोग विशेषज्ञ (Gynecologist):** महिलाओं के स्वास्थ्य और प्रेग्नेंसी से जुड़े पर्चे।
    * 🧠 **न्यूरोलॉजिस्ट और मानसिक रोग (Neurologist / Psychiatrist):** सिरदर्द, माइग्रेन और नसों की दवाइयां।
    * 🦷 **डेंटिस्ट (Dentist), स्किन (Dermatologist) और आँख-कान-गला (ENT)** के पर्चे।
    * 🌿 **आयुर्वेदिक (Ayurveda) और होम्योपैथिक (Homeopathy)** डॉक्टरों के पर्चे।
    * 🧾 **पैथोलॉजी लैब रिपोर्ट और अस्पताल के डिस्चार्ज बिल।**
    """)

# 3. साइडबार में API Key डालने की जगह
with st.sidebar:
    st.header("⚙️ सेटिंग्स")
    api_key = st.text_input("अपनी Gemini API Key डालें:", type="password")
    st.info("यह टूल दवाइयों के सस्ते जेनेरिक विकल्प और सरकारी योजनाओं की जानकारी देता है।")
    st.markdown("---")
    st.markdown("👨‍💻 **Creator:** Shailendra Kumar Singh")
# 4. Self-Healing AI इंजन (अपने आप बैकअप और सुधार करने वाला सिस्टम)
def analyze_with_self_healing(api_key, image, prompt):
    client = genai.Client(api_key=api_key)
    # भविष्य के लिए मल्टीपल बैकअप मॉडल्स की लिस्ट
    backup_models = ["gemini-2.5-flash", "gemini-2.5-pro", "gemini-2.0-flash"]
   
    last_error = ""
    for model_name in backup_models:
        for attempt in range(2):  # हर मॉडल पर 2 बार ऑटो-रीट्राई करेगा
            try:
                response = client.models.generate_content(
                    model=model_name,
                    contents=
                )
                if response and response.text:
                    return response.text, model_name
            except Exception as e:
                last_error = str(e)
                # अगर API Key ही गलत है, तो तुरंत रुककर बता दे
                if "API_KEY_INVALID" in last_error or "403" in last_error:
                    raise Exception("आपकी Gemini API Key गलत है या एक्सपायर हो गई है। कृपया नई Key डालें।")
                time.sleep(1.5)  # 1.5 सेकंड रुककर अपने आप दोबारा कोशिश करेगा
               
    raise Exception(f"सभी बैकअप सिस्टम व्यस्त हैं। कृपया थोड़ी देर बाद प्रयास करें। (तकनीकी कारण: {last_error})")

# 5. फोटो अपलोड और विश्लेषण
uploaded_file = st.file_uploader("यहाँ डॉक्टर के पर्चे या अस्पताल के बिल की फोटो अपलोड करें", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    try:
        image = Image.open(uploaded_file)
        st.image(image, caption="अपलोड किया गया पर्चा / बिल", use_container_width=True)
    except Exception:
        st.error("⚠️ यह फोटो खराब (Corrupted) है। कृपया कोई दूसरी साफ फोटो अपलोड करें।")
        st.stop()

    if st.button("🔍 जांच शुरू करें और बचत देखें"):
        if not api_key:
            st.error("कृपया पहले बाईं तरफ (Sidebar) अपनी Gemini API Key डालें!")
        else:
            with st.spinner("Malik MediGuard AI (Self-Healing Engine) आपके पर्चे की जांच कर रहा है..."):
                try:
                    prompt = """
                    आप एक अनुभवी भारतीय मेडिकल बिल और जेनेरिक दवा विशेषज्ञ हैं।
                    इस इमेज (डॉक्टर का पर्चा या अस्पताल का बिल) को ध्यान से पढ़ें और सरल हिंदी में नीचे दिए गए 4 बिंदुओं में रिपोर्ट दें:
1. **पर्चे/बिल का सार:** यह किस विशेषज्ञ डॉक्टर का पर्चा लग रहा है और इसमें कौन-कौन सी मुख्य दवाइयां या टेस्ट लिखे हैं?
                    2. **सस्ते जेनेरिक विकल्प (बचत गाइड):** हर महंगी दवा का असली सॉल्ट (Composition) बताएं और 'जन औषधि केंद्र' या बाज़ार में मिलने वाले सस्ते विकल्प व अनुमानित बचत बताएं।
                    3. **बिल/चार्ज की जांच:** यदि यह अस्पताल या लैब का बिल है, तो बताएं कि क्या कोई चार्ज सामान्य से बहुत ज़्यादा (Overpriced) लग रहा है।
                    4. **सरकारी योजना सहायता:** क्या इस बीमारी या इलाज के लिए 'आयुष्मान भारत (PM-JAY)' या कोई अन्य सरकारी मदद मिल सकती है?

                    अंत में एक स्पष्ट चेतावनी लिखें कि यह जानकारी केवल जागरूकता के लिए है, कोई भी दवा बदलने से पहले अपने डॉक्टर से ज़रूर पूछें।
                    """
                    result_text, used_model = analyze_with_self_healing(api_key, image, prompt)
                    st.success(f"✅ विश्लेषण पूरा हुआ! (सुरक्षित इंजन: {used_model})")
                    st.markdown(result_text)
                except Exception as e:
                    st.error(f"🛠️ ऑटो-रिकवरी सूचना: {e}")

# 6. सबसे नीचे क्रिएटर का नाम
st.markdown("---")
st.markdown("<div style='text-align: center;'>🏥 <b>Malik MediGuard AI</b> | Created by <b>Shailendra Kumar Singh</b></div>", unsafe_allow_html=True)
 
