import streamlit as st
import os
from PIL import Image
import google.generativeai as genai

# ---------------- CONFIG ----------------
st.set_page_config(page_title="Gemini Vision Chat", page_icon="🧠", layout="wide")

# Secure API key (use secrets.toml)

os.environ["GEMINI_API_KEY"] = "gemini_api_key"

genai.configure(api_key=os.environ["GEMINI_API_KEY"])
# ---------------- SESSION STATE ----------------
if "history" not in st.session_state:
    st.session_state.history = []

# ---------------- MODEL FUNCTION ----------------
def get_gemini_response(prompt, images):
    model = genai.GenerativeModel("models/gemini-3-flash-preview")

    if prompt:
        response = model.generate_content([prompt] + images)
    else:
        response = model.generate_content(images)

    return response.text

# ---------------- SIDEBAR ----------------
with st.sidebar:
    st.title("⚙️ Settings")
    st.info("Upload images and chat with Gemini Vision AI.")

    if st.button("🗑️ Clear History"):
        st.session_state.history = []

# ---------------- MAIN UI ----------------
st.title("🧠 Gemini Vision Chat App")
st.markdown("Chat with images like ChatGPT 🚀")

# ---------------- QUICK PROMPTS ----------------
st.markdown("### ⚡ Quick Prompts")
colA, colB, colC = st.columns(3)

if colA.button("🧾 Describe Image"):
    st.session_state.prompt = "Describe this image in detail"

if colB.button("🔍 Detect Objects"):
    st.session_state.prompt = "What objects are present in this image?"

if colC.button("📊 Extract Text"):
    st.session_state.prompt = "Extract all visible text from this image"

# ---------------- INPUT AREA ----------------
prompt = st.text_input("💬 Ask something about the image", value=st.session_state.get("prompt", ""))

uploaded_files = st.file_uploader(
    "📤 Upload one or more images",
    type=["jpg", "jpeg", "png"],
    accept_multiple_files=True
)

images = []

if uploaded_files:
    cols = st.columns(len(uploaded_files))

    for i, file in enumerate(uploaded_files):
        img = Image.open(file)
        images.append(img)
        cols[i].image(img, use_container_width=True)

# ---------------- CHAT DISPLAY ----------------
st.markdown("---")
st.markdown("### 💬 Conversation")

for chat in st.session_state.history:
    with st.chat_message("user"):
        st.write(chat["user"])

    with st.chat_message("assistant"):
        st.write(chat["assistant"])

# ---------------- SUBMIT ----------------
if st.button("🚀 Generate Response"):
    if not images:
        st.warning("Please upload at least one image")
    else:
        with st.spinner("🤖 Gemini analyzing..."):
            response = get_gemini_response(prompt, images)

        st.session_state.history.append({
            "user": prompt if prompt else "Analyze image",
            "assistant": response
        })

        st.rerun()

# ---------------- FOOTER ----------------
st.markdown("---")
st.markdown("🚀 Built with Gemini AI + Streamlit | Advanced UI Version")

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
.stButton>button {
    background-color: #4CAF50;
    color: white;
    border-radius: 10px;
    height: 3em;
    width: 100%;
}
.stTextInput>div>div>input {
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)