import streamlit as st

st.set_page_config(page_title="भारत की सभी प्रमुख दवाइयां - Malik MediGuard AI", page_icon="💊")
st.title("💊 भारत की संपूर्ण दवा एवं सॉल्ट डायरेक्टरी")
st.caption("Created by: **Shailendra Kumar Singh** | Malik MediGuard Mega Medicine Engine")

st.info("यहाँ भारत में सबसे ज़्यादा इस्तेमाल होने वाली सभी दवाइयों (ब्रांड नाम, जेनेरिक सॉल्ट और बीमारी) की पूरी सूची और जन औषधि बचत उपलब्ध है।")

ALL_INDIA_MEDS = [
    {"keys": ["paracetamol", "dolo", "calpol", "crocin", "pacimol", "febrex", "fever", "बुखार"], "name": "Paracetamol 500mg/650mg (Dolo / Calpol)", "cat": "बुखार व दर्द", "brand": "₹33", "jan": "₹12", "scheme": "सरकारी अस्पताल में मुफ्त व जन औषधि में ₹12"},
    {"keys": ["aceclofenac", "zerodol", "hifenac", "movexx", "pain", "दर्द"], "name": "Aceclofenac 100mg + Paracetamol (Zerodol-P)", "cat": "जोड़ों व बदन दर्द", "brand": "₹115", "jan": "₹22", "scheme": "जन औषधि केंद्र पर 80% तक सस्ता"},
    {"keys": ["diclofenac", "voveran", "dynapar", "reactin"], "name": "Diclofenac 50mg (Voveran / Dynapar)", "cat": "तेज़ दर्द व सूजन", "brand": "₹95", "jan": "₹15", "scheme": "जन औषधि केंद्र पर ₹15 में उपलब्ध"},
    {"keys": ["ibuprofen", "combiflam", "brufen", "ibugesic"], "name": "Ibuprofen 400mg + Paracetamol (Combiflam)", "cat": "सिरदर्द, दांत व बदन दर्द", "brand": "₹45", "jan": "₹14", "scheme": "जन औषधि केंद्र पर ₹14 में उपलब्ध"},
    {"keys": ["nimesulide", "nice", "nise", "sumo"], "name": "Nimesulide 100mg (Nise / Sumo)", "cat": "बुखार व दर्द", "brand": "₹105", "jan": "₹18", "scheme": "जन औषधि केंद्र पर उपलब्ध"},
    {"keys": ["tramadol", "ultracet", "domadol"], "name": "Tramadol + Paracetamol (Ultracet)", "cat": "गंभीर दर्द", "brand": "₹240", "jan": "₹45", "scheme": "जन औषधि केंद्र पर 80% बचत"},
    {"keys": ["etoricoxib", "etoshine", "nucoxia", "arcoxia"], "name": "Etoricoxib 90mg (Nucoxia / Etoshine)", "cat": "गठिया व कमर दर्द", "brand": "₹210", "jan": "₹38", "scheme": "जन औषधि केंद्र पर ₹38 में उपलब्ध"},
    {"keys": ["pantoprazole", "pan-d", "pan 40", "pantocid", "pantodac", "gas", "गैस", "एसिडिटी"], "name": "Pantoprazole 40mg / DSR (Pan-D / Pan 40)", "cat": "गैस व एसिडिटी", "brand": "₹199", "jan": "₹28", "scheme": "जन औषधि केंद्र पर मात्र ₹28 में"},
    {"keys": ["omeprazole", "omez", "omez-d", "ocid"], "name": "Omeprazole 20mg (Omez / Omez-D)", "cat": "पेट की जलन व गैस", "brand": "₹110", "jan": "₹16", "scheme": "जन औषधि केंद्र पर ₹16 में उपलब्ध"},
    {"keys": ["rabeprazole", "razo", "rablet", "rabium", "cyra"], "name": "Rabeprazole 20mg + Domperidone (Razo-D / Cyra-D)", "cat": "एसिडिटी व उल्टी", "brand": "₹220", "jan": "₹30", "scheme": "जन औषधि केंद्र पर 85% बचत"},
    {"keys": ["ranitidine", "aciloc", "zinetac", "rantac"], "name": "Ranitidine 150mg (Aciloc / Rantac)", "cat": "सामान्य गैस", "brand": "₹42", "jan": "₹10", "scheme": "सरकारी अस्पतालों में निःशुल्क"},
    {"keys": ["ondansetron", "emeset", "ondem", "vomikind", "उल्टी", "vomit"], "name": "Ondansetron 4mg (Emeset / Vomikind)", "cat": "उल्टी व जी मिचलाना", "brand": "₹58", "jan": "₹12", "scheme": "जन औषधि केंद्र पर ₹12 में उपलब्ध"},
    {"keys": ["dicyclomine", "meftal", "cyclopam", "पेट दर्द", "stomach pain"], "name": "Dicyclomine + Mefenamic Acid (Meftal-Spas)", "cat": "पेट दर्द व मरोड़", "brand": "₹55", "jan": "₹14", "scheme": "जन औषधि केंद्र पर ₹14 में उपलब्ध"},
    {"keys": ["norfloxacin", "tinidazole", "norflox", "oflox", "ornidazole", "दस्त", "diarrhea", "loose motion"], "name": "Norfloxacin + Tinidazole / Oflox-OZ (दस्त)", "cat": "दस्त व पेट संक्रमण", "brand": "₹125", "jan": "₹26", "scheme": "जन औषधि केंद्र पर 78% बचत"},
    {"keys": ["lactulose", "duphalac", "cremaffin", "कब्ज", "constipation"], "name": "Lactulose Solution (Duphalac / Cremaffin)", "cat": "कब्ज (Constipation)", "brand": "₹260", "jan": "₹85", "scheme": "जन औषधि केंद्र पर ₹85 में उपलब्ध"},
    {"keys": ["amoxicillin", "clavulanic", "augmentin", "clavam", "moxikind", "mox", "infection", "इन्फेक्शन"], "name": "Amoxicillin 500 + Clavulanic 125 (Augmentin / Clavam)", "cat": "एंटीबायोटिक", "brand": "₹223", "jan": "₹65", "scheme": "जन औषधि केंद्र पर 70% तक सस्ता"},
    {"keys": ["azithromycin", "azithral", "azee", "zady", "throat", "गला"], "name": "Azithromycin 500mg (Azithral / Azee)", "cat": "गला व छाती संक्रमण", "brand": "₹132", "jan": "₹38", "scheme": "जन औषधि केंद्र पर ₹38 में उपलब्ध"},
    {"keys": ["cefixime", "taxim-o", "zifi", "mahacef", "cefi"], "name": "Cefixime 200mg (Taxim-O / Zifi 200)", "cat": "टाइफाइड व बैक्टीरियल बुखार", "brand": "₹118", "jan": "₹32", "scheme": "जन औषधि केंद्र पर ₹32 में उपलब्ध"},
    {"keys": ["ciprofloxacin", "ciplox", "cifran"], "name": "Ciprofloxacin 500mg (Ciplox 500)", "cat": "यूरिन व पेट संक्रमण", "brand": "₹48", "jan": "₹15", "scheme": "सरकारी अस्पतालों में निःशुल्क"},
    {"keys": ["levofloxacin", "levomac", "lquin", "glevo"], "name": "Levofloxacin 500mg (Levomac / Glevo)", "cat": "फेफड़ों व साइनस संक्रमण", "brand": "₹98", "jan": "₹24", "scheme": "जन औषधि केंद्र पर ₹24 में उपलब्ध"},
    {"keys": ["doxycycline", "doxt", "biodoxi"], "name": "Doxycycline 100mg (Doxt-SL)", "cat": "संक्रमण व मुंहासे", "brand": "₹95", "jan": "₹18", "scheme": "जन औषधि केंद्र पर ₹18 में उपलब्ध"},
    {"keys": ["albendazole", "zentel", "bandy", "कीड़े", "worms"], "name": "Albendazole 400mg (Zentel / Bandy)", "cat": "पेट के कीड़े", "brand": "₹25", "jan": "₹6", "scheme": "सरकारी स्वास्थ्य केंद्रों पर मुफ्त"},
    {"keys": ["ivermectin", "fluconazole", "forcan", "zocon", "itraconazole", "candiforce", "दाद", "खुजली", "fungal"], "name": "Fluconazole / Itraconazole (Zocon / Candiforce)", "cat": "फंगल इन्फेक्शन व दाद", "brand": "₹180", "jan": "₹35", "scheme": "जन औषधि केंद्र पर 80% बचत"},
    {"keys": ["levocetirizine", "cetirizine", "cetzine", "okacet", "1-al", "allergy", "एलर्जी", "छींक"], "name": "Levocetirizine 5mg / Cetirizine 10mg (Cetzine)", "cat": "एलर्जी व छींक", "brand": "₹85", "jan": "₹10", "scheme": "जन औषधि केंद्र पर मात्र ₹10 में"},
    {"keys": ["montelukast", "montair", "telekast", "montek"], "name": "Montelukast 10mg + Levocetirizine (Montair-LC)", "cat": "सांस की एलर्जी व जुकाम", "brand": "₹210", "jan": "₹32", "scheme": "जन औषधि केंद्र पर ₹32 में उपलब्ध"},
    {"keys": ["fexofenadine", "allegra", "altiva"], "name": "Fexofenadine 120mg / 180mg (Allegra)", "cat": "स्किन व नाक की एलर्जी", "brand": "₹235", "jan": "₹38", "scheme": "जन औषधि केंद्र पर ₹38 में उपलब्ध"},
    {"keys": ["sinarest", "wikoryl", "cheston", "solvin", "cold", "जुकाम", "सर्दी"], "name": "Paracetamol + Phenylephrine + CPM (Sinarest / Cheston Cold)", "cat": "सर्दी-जुकाम व सिरदर्द", "brand": "₹95", "jan": "₹18", "scheme": "जन औषधि केंद्र पर ₹18 में उपलब्ध"},
    {"keys": ["ambroxol", "terbutaline", "ascoril", "grilinctus", "benadryl", "alex", "cough", "खांसी"], "name": "Ambroxol + Terbutaline / Dextromethorphan (Ascoril / Alex)", "cat": "सूखी व बलगम वाली खांसी", "brand": "₹135", "jan": "₹35", "scheme": "जन औषधि केंद्र पर 75% बचत"},
    {"keys": ["salbutamol", "budesonide", "asthalin", "foracort", "seretide", "दमा", "अस्थमा", "asthma"], "name": "Salbutamol / Budesonide Inhaler (Asthalin / Foracort)", "cat": "दमा व सांस फूलना", "brand": "₹380", "jan": "₹110", "scheme": "जन औषधि केंद्र पर ₹110 में उपलब्ध"},
    {"keys": ["telmisartan", "telma", "telmikind", "telsar", "cresar", "bp", "बीपी"], "name": "Telmisartan 40mg (Telma 40 / Cresar)", "cat": "ब्लड प्रेशर (BP)", "brand": "₹240", "jan": "₹25", "scheme": "जन औषधि केंद्र पर 88% तक भारी बचत"},
    {"keys": ["amlodipine", "stamlo", "amlokind", "amlong"], "name": "Amlodipine 5mg (Stamlo / Amlokind)", "cat": "ब्लड प्रेशर (BP)", "brand": "₹120", "jan": "₹12", "scheme": "जन औषधि केंद्र पर ₹12 में उपलब्ध"},
    {"keys": ["losartan", "losar", "repace"], "name": "Losartan 50mg (Losar 50)", "cat": "ब्लड प्रेशर (BP)", "brand": "₹135", "jan": "₹18", "scheme": "जन औषधि केंद्र पर ₹18 में उपलब्ध"},
    {"keys": ["metoprolol", "atenolol", "betaloc", "metolar", "aten"], "name": "Metoprolol 25/50mg (Betaloc / Metolar)", "cat": "दिल की धड़कन व BP", "brand": "₹145", "jan": "₹20", "scheme": "जन औषधि केंद्र पर ₹20 में उपलब्ध"},
    {"keys": ["atorvastatin", "rosuvastatin", "atorva", "lipitor", "rosuvas", "rozavel", "cholesterol", "कोलेस्ट्रॉल"], "name": "Atorvastatin 10mg / Rosuvastatin (Atorva / Rosuvas)", "cat": "कोलेस्ट्रॉल व हार्ट सुरक्षा", "brand": "₹190", "jan": "₹22", "scheme": "जन औषधि केंद्र पर 88% बचत"},
    {"keys": ["aspirin", "clopidogrel", "ecosprin", "clopilet", "deplatt", "heart", "दिल"], "name": "Aspirin 75mg / Clopidogrel (Ecosprin / Clopilet)", "cat": "खून पतला करने व हार्ट अटैक बचाव", "brand": "₹95", "jan": "₹14", "scheme": "जन औषधि केंद्र पर ₹14 में उपलब्ध"},
    {"keys": ["metformin", "glycomet", "gluconorm", "obimet", "sugar", "diabetes", "शुगर"], "name": "Metformin 500mg / 1000mg (Glycomet)", "cat": "डायबिटीज (शुगर)", "brand": "₹95", "jan": "₹14", "scheme": "जन औषधि केंद्र व सरकारी केंद्रों पर उपलब्ध"},
    {"keys": ["glimepiride", "amaryl", "glimy", "zoryl"], "name": "Glimepiride 1mg / 2mg (Amaryl / Zoryl)", "cat": "डायबिटीज (शुगर)", "brand": "₹165", "jan": "₹18", "scheme": "जन औषधि केंद्र पर 88% बचत"},
    {"keys": ["sitagliptin", "vildagliptin", "teneligliptin", "januvia", "galvus", "tenepla"], "name": "Teneligliptin 20mg / Vildagliptin (Galvus / Tenepla)", "cat": "शुगर नियंत्रण", "brand": "₹280", "jan": "₹42", "scheme": "जन औषधि केंद्र पर ₹42 में उपलब्ध"},
    {"keys": ["thyroxine", "levothyroxine", "thyronorm", "eltroxin", "thyroid", "थायराइड"], "name": "Levothyroxine 25/50/100mcg (Thyronorm / Eltroxin)", "cat": "थायराइड", "brand": "₹185", "jan": "₹35", "scheme": "जन औषधि केंद्र पर 80% बचत"},
    {"keys": ["calcium", "shelcal", "cipcal", "gemcal", "calcimax", "कैल्शियम"], "name": "Calcium 500mg + Vitamin D3 (Shelcal / Cipcal)", "cat": "हड्डियों की मजबूती", "brand": "₹145", "jan": "₹28", "scheme": "जन औषधि केंद्र पर ₹28 में उपलब्ध"},
    {"keys": ["vitamin d", "cholecalciferol", "uprise", "calcirol", "arachitol"], "name": "Vitamin D3 60,000 IU (Uprise-D3 / Calcirol)", "cat": "विटामिन D की कमी", "brand": "₹130", "jan": "₹24", "scheme": "जन औषधि केंद्र पर ₹24 में उपलब्ध"},
    {"keys": ["vitamin b", "becosules", "neurobion", "methylcobalamin", "नसों", "कमजोरी"], "name": "Vitamin B-Complex / Methylcobalamin (Becosules / Neurobion)", "cat": "नसों की ताकत व कमजोरी", "brand": "₹55", "jan": "₹15", "scheme": "जन औषधि केंद्र पर ₹15 में उपलब्ध"},
    {"keys": ["vitamin c", "limcee", "celin", "zinc", "zincovit"], "name": "Vitamin C 500mg / Multivitamin (Limcee / Zincovit)", "cat": "इम्युनिटी व कमजोरी", "brand": "₹110", "jan": "₹22", "scheme": "जन औषधि केंद्र पर ₹22 में उपलब्ध"},
    {"keys": ["iron", "folic", "autrin", "dexorange", "fefol", "livogen", "खून की कमी", "anemia"], "name": "Ferrous Ascorbate + Folic Acid (Livogen / Dexorange)", "cat": "खून की कमी (एनीमिया)", "brand": "₹160", "jan": "₹28", "scheme": "सरकारी अस्पतालों में निःशुल्क व जन औषधि में ₹28"},
    {"keys": ["pregabalin", "gabapentin", "pregalin", "gabapin", "नसों का दर्द"], "name": "Pregabalin 75mg + Methylcobalamin (Pregalin-M)", "cat": "नसों का दर्द व झुनझुनी", "brand": "₹245", "jan": "₹42", "scheme": "जन औषधि केंद्र पर 82% बचत"}
]
SUFFIX_RULES = {
    "prazole": ("एसिडिटी और गैस की दवा (PPI)", "जन औषधि केंद्र पर 80-85% सस्ती उपलब्ध"),
    "mycin": ("बैक्टीरियल इन्फेक्शन की एंटीबायोटिक", "जन औषधि केंद्र पर 70% सस्ती उपलब्ध"),
    "floxacin": ("यूरिन, पेट या फेफड़ों के इन्फेक्शन की एंटीबायोटिक", "जन औषधि केंद्र पर 75% सस्ती उपलब्ध"),
    "cillin": ("संक्रमण रोकने वाली पेनिसिलिन एंटीबायोटिक", "जन औषधि केंद्र पर 70% सस्ती उपलब्ध"),
    "sartan": ("हाई ब्लड प्रेशर (BP) नियंत्रित करने की दवा", "जन औषधि केंद्र पर 85-90% सस्ती उपलब्ध"),
    "dipine": ("ब्लड प्रेशर और दिल की सुरक्षा की दवा", "जन औषधि केंद्र पर 85% सस्ती उपलब्ध"),
    "lol": ("दिल की धड़कन और BP नियंत्रित करने की दवा", "जन औषधि केंद्र पर 80% सस्ती उपलब्ध"),
    "statin": ("कोलेस्ट्रॉल कम करने और हार्ट अटैक से बचाव की दवा", "जन औषधि केंद्र पर 85% सस्ती उपलब्ध"),
    "gliptin": ("डायबिटीज (शुगर) नियंत्रित करने की दवा", "जन औषधि केंद्र पर 80% सस्ती उपलब्ध"),
    "formin": ("डायबिटीज (शुगर) की मुख्य दवा", "जन औषधि केंद्र व सरकारी केंद्रों पर उपलब्ध"),
    "fenac": ("जोड़ों, कमर और बदन दर्द की दवा", "जन औषधि केंद्र पर 80% सस्ती उपलब्ध"),
    "tirizine": ("एलर्जी, छींक और जुकाम की दवा", "जन औषधि केंद्र पर मात्र ₹10-₹15 में उपलब्ध"),
    "tidine": ("पेट की गैस और जलन की दवा", "सरकारी अस्पतालों व जन औषधि केंद्र पर उपलब्ध")
}

search = st.text_input("🔍 भारत की किसी भी दवा का नाम, सॉल्ट या बीमारी लिखें (जैसे: Telma, Atorva, Zincovit, Thyronorm, गैस, शुगर, BP):")

if search.strip():
    q = search.lower()
    found = [m for m in ALL_INDIA_MEDS if any(k in q for k in m["keys"])]
    if found:
        for m in found:
            st.success(f"💊 **{m['name']}** ({m['cat']})")
            st.markdown(f"* **बाज़ार रेट (Branded):** ~{m['brand']} ➡️ **जन औषधि रेट:** ~{m['jan']}\n* **🏛️ सरकारी योजना:** {m['scheme']}")
    else:
        matched_suffix = False
        for suf, (work, saving) in SUFFIX_RULES.items():
            if suf in q:
                st.success(f"🧠 **Smart Salt पहचान ({search.upper()}):** यह **{work}** है।")
                st.info(f"💰 **बचत सुझाव:** {saving}। इस सॉल्ट का नाम नज़दीकी जन औषधि केंद्र पर दिखाएं।")
                matched_suffix = True
                break
        if not matched_suffix:
            st.info(f"🔍 **{search}** का असली जेनेरिक सॉल्ट नाम (जो रैपर पर छोटे अक्षरों में लिखा होता है) नज़दीकी **प्रधानमंत्री भारतीय जन औषधि केंद्र** पर दिखाएं—आपको 50% से 85% तक की सीधी बचत मिलेगी।")

st.markdown("---")
st.subheader("📑 श्रेणी के अनुसार भारत की प्रमुख दवाइयां देखें")
categories = sorted(list(set(m["cat"] for m in ALL_INDIA_MEDS)))
sel_cat = st.selectbox("बीमारी की श्रेणी चुनें:", categories)
for m in ALL_INDIA_MEDS:
    if m["cat"] == sel_cat:
        st.markdown(f"* **{m['name']}** — बाज़ार: {m['brand']} | जन औषधि: **{m['jan']}** ({m['scheme']})")

st.markdown("---")
st.warning("⚠️ अस्वीकरण: यह सूची केवल जागरूकता और दवाइयों के खर्च की पारदर्शिता के लिए है। किसी भी दवा को बदलने या लेने से पहले डॉक्टर की सलाह ज़रूर लें।")
st.markdown("<div style='text-align: center;'>🏥 <b>Malik MediGuard AI</b> | Created by <b>Shailendra Kumar Singh</b></div>", unsafe_allow_html=True)
 


    
