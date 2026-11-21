import streamlit as st
from google import genai
from PIL import Image

st.set_page_config(page_title="MediGuard AI - सही इलाज और बचत", page_icon="🏥")
st.title("🏥 MediGuard AI")
st.subheader("डॉक्टर के पर्चे और मेडिकल बिल की असली जांच करें")

with st.sidebar:
    st.header("⚙️ सेटिंग्स")
    api_key = st.text_input("अपनी Gemini API Key डालें:", type="password")
    st.info("यह टूल दवाइयों के सस्ते जेनेरिक विकल्प और सरकारी योजनाओं की जानकारी देता है।")

uploaded_file = st.file_uploader("यहाँ डॉक्टर के पर्चे या अस्पताल के बिल की फोटो अपलोड करें", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="अपलोड किया गया पर्चा / बिल", use_container_width=True)

    if st.button("🔍 जांच शुरू करें और बचत देखें"):
        if not api_key:
            st.error("कृपया पहले बाईं तरफ (Sidebar) अपनी Gemini API Key डालें!")
        else:
            with st.spinner("AI आपके पर्चे और बिल का विश्लेषण कर रहा है..."):
                try:
                    client = genai.Client(api_key=api_key)
                    prompt = """
                    आप एक अनुभवी भारतीय मेडिकल बिल और जेनेरिक दवा विशेषज्ञ हैं।
                    इस इमेज (डॉक्टर का पर्चा या अस्पताल का बिल) को ध्यान से पढ़ें और सरल हिंदी में नीचे दिए गए 4 बिंदुओं में रिपोर्ट दें:

                    1. **पर्चे/बिल का सार:** इसमें कौन-कौन सी मुख्य दवाइयां या टेस्ट लिखे हैं?
                    2. **सस्ते जेनेरिक विकल्प (बचत गाइड):** हर महंगी दवा का असली सॉल्ट (Composition) बताएं और 'जन औषधि केंद्र' या बाज़ार में मिलने वाले सस्ते विकल्प व अनुमानित बचत बताएं।
                    3. **बिल/चार्ज की जांच:** यदि यह अस्पताल या लैब का बिल है, तो बताएं कि क्या कोई चार्ज सामान्य से बहुत ज़्यादा (Overpriced) लग रहा है।
                    4. **सरकारी योजना सहायता:** क्या इस बीमारी या इलाज के लिए 'आयुष्मान भारत (PM-JAY)' या कोई अन्य सरकारी मदद मिल सकती है?

                    अंत में एक स्पष्ट चेतावनी लिखें कि यह जानकारी केवल जागरूकता के लिए है, कोई भी दवा बदलने से पहले अपने डॉक्टर से ज़रूर पूछें।
                    """
                    response = client.models.generate_content(
                        model="gemini-2.5-flash",
                        contents=
                    )
                    st.success("✅ विश्लेषण पूरा हुआ!")
                    st.markdown(response.text)
                except Exception as e:
                    st.error(f"कुछ गड़बड़ हुई है: {e}")
 
