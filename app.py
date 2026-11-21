import streamlit as st
from google import genai
from PIL import Image

st.set_page_config(page_title="Malik MediGuard AI", page_icon="🏥")
st.title("🏥 Malik MediGuard AI")
st.subheader("डॉक्टर के पर्चे और मेडिकल बिल की असली जांच करें")
st.caption("Created by: Shailendra Kumar Singh | 🛡️ Smart Backup AI")

default_key = st.secrets.get("GEMINI_API_KEY", "")
api_key = st.sidebar.text_input("अपनी Gemini API Key डालें:", value=default_key, type="password")

med_text = st.text_input("✍️ यहाँ दवा या बीमारी का नाम लिखें (जैसे: Augmentin 625, AF-Tabs):")
up = st.file_uploader("या यहाँ डॉक्टर के पर्चे / दवा की फोटो अपलोड करें:", type=("jpg", "jpeg", "png"))

if st.button("🔍 जांच शुरू करें और बचत देखें"):
    if not api_key:
        st.error("कृपया पहले बाईं तरफ (>>) अपनी Gemini API Key डालें!")
    elif not med_text and up is None:
        st.warning("कृपया ऊपर दवा का नाम लिखें या नीचे फोटो अपलोड करें!")
    else:
        with st.spinner("Malik MediGuard AI जांच कर रहा है..."):
            client = genai.Client(api_key=api_key)
            prompt = f"आप एक भारतीय मेडिकल बिल और जेनेरिक दवा विशेषज्ञ हैं। इस जानकारी/फोटो ({med_text}) को पढ़कर सरल हिंदी में 4 पॉइंट्स में रिपोर्ट दें: 1. दवा या पर्चे का सार, 2. सस्ते जेनेरिक (जन औषधि) विकल्प और बचत, 3. रेट/बिल की जांच, 4. आयुष्मान भारत या सरकारी योजना की मदद। अंत में डॉक्टर से सलाह लेने की चेतावनी लिखें।"
            items = list((prompt,))
            if up is not None:
                img = Image.open(up)
                img.thumbnail((800, 800))
                items.append(img)
            done = False
            for m in ("gemini-3.8-flash-lite", "gemini-3.8-flash", "gemini-3.8-pro"):
                try:
                    res = client.models.generate_content(model=m, contents=items)
                    st.success(f"✅ विश्लेषण पूरा हुआ! (इंजन: {m})")
                    st.markdown(res.text)
                    done = True
                    break
                except Exception as e:
                    last_err = str(e)
            if not done:
                st.error(f"सभी सर्वर अभी व्यस्त हैं, कृपया 10 सेकंड बाद प्रयास करें: {last_err}")

st.markdown("---")
st.write("🏥 Malik MediGuard AI | Created by Shailendra Kumar Singh")
 
