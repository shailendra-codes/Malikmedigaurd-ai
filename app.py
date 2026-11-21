import streamlit as st
from google import genai
from PIL import Image

st.set_page_config(page_title="Malik MediGuard AI", page_icon="🏥")
st.title("🏥 Malik MediGuard AI")
st.subheader("डॉक्टर के पर्चे और मेडिकल बिल की असली जांच करें")
st.caption("Created by: Shailendra Kumar Singh | Superfast AI")

st.info("📋 यह टूल जनरल फिजिशियन, हार्ट, हड्डी, बच्चों, महिला, स्किन, डेंटल, आयुर्वेद, होम्योपैथी के पर्चे और लैब/अस्पताल बिल पढ़ सकता है।")

api_key = st.sidebar.text_input("अपनी Gemini API Key डालें:", type="password")
st.sidebar.write("Creator: Shailendra Kumar Singh")

up = st.file_uploader("यहाँ डॉक्टर के पर्चे या दवा की फोटो अपलोड करें", type=("jpg", "jpeg", "png"))

if up is not None:
    img = Image.open(up)
    st.image(img, width="stretch")
    if st.button("🔍 जांच शुरू करें और बचत देखें"):
        if not api_key:
            st.error("कृपया पहले बाईं तरफ (>>) अपनी Gemini API Key डालें!")
        else:
            with st.spinner("Malik MediGuard AI जांच कर रहा है..."):
                try:
                    small_img = img.copy()
                    small_img.thumbnail((1024, 1024))
                    client = genai.Client(api_key=api_key)
                    prompt = "आप एक भारतीय मेडिकल बिल और जेनेरिक दवा विशेषज्ञ हैं। इस फोटो को पढ़कर सरल हिंदी में 4 पॉइंट्स में रिपोर्ट दें: 1. दवा या पर्चे का सार, 2. सस्ते जेनेरिक (जन औषधि) विकल्प और बचत, 3. बिल/रेट की जांच, 4. आयुष्मान भारत या सरकारी योजना की मदद। अंत में डॉक्टर से सलाह लेने की चेतावनी लिखें।"
                    res = client.models.generate_content(model="gemini-2.5-flash", contents=list((small_img, prompt)))
                    st.success("✅ विश्लेषण पूरा हुआ!")
                    st.markdown(res.text)
                except Exception as e:
                    st.error(f"त्रुटि: {e}")

st.markdown("---")
st.write("🏥 Malik MediGuard AI | Created by Shailendra Kumar Singh")
 
