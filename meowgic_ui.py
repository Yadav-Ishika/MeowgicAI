import streamlit as st
import streamlit.components.v1 as components
import requests
from gtts import gTTS
import io
import base64

# --- Page Config ---
st.set_page_config(page_title="MeowgicAI 🐾", layout="centered")

# --- Custom Styling for Dark Theme ---
st.markdown("""
    <style>
        body {
            background-color: #1e1e1e;
            color: white;
        }
        .main > div {
            background-color: #1e1e1e;
        }
        h1, h2, h3, h4 {
            color: #FFD700;
        }
        .audio-controls {
            display: flex;
            justify-content: flex-end;
            margin-top: 10px;
            gap: 15px;
        }
        .icon-button {
            background-color: transparent;
            border: none;
            cursor: pointer;
            filter: brightness(0) invert(1);
            width: 30px;
            height: 30px;
        }
        .icon-button:hover {
            transform: scale(1.1);
        }
        audio {
            display: none;
        }
    </style>
""", unsafe_allow_html=True)


st.title("MeowgicAI 🐱")
st.subheader("Your Cat Companion")

# --- Input box ---
question = st.text_input("Ask MeowgicAI a question about cats...")

# --- Generate and Auto-Play Voice ---

def play_audio_auto(text):
    tts = gTTS(text=text, lang='en')
    audio_fp = io.BytesIO()
    tts.write_to_fp(audio_fp)
    audio_fp.seek(0)
    audio_bytes = audio_fp.read()
    b64 = base64.b64encode(audio_bytes).decode()

    components.html(f"""
        <div style="text-align: right; margin-top: 10px;">
            <audio id="meowAudio" autoplay>
                <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
            </audio>

            <button onclick="document.getElementById('meowAudio').currentTime=0; document.getElementById('meowAudio').play();" 
                style="background-color: #1e1e1e; border: none; color: white; font-size: 22px; cursor: pointer; margin-right: 10px;">
                🔁
            </button>
            <button onclick="document.getElementById('meowAudio').pause();" 
                style="background-color: #1e1e1e; border: none; color: white; font-size: 22px; cursor: pointer;">
                🔇
            </button>
        </div>
    """, height=80)


# --- Process User Input ---
if st.button("Get Answer"):
    if not question.strip():
        st.warning("Please enter a question.")
    else:
        with st.spinner("Thinking like a cat..."):
            response = requests.post("http://127.0.0.1:8000/ask", json={"question": question})
            if response.status_code == 200:
                result = response.json()
                answer = result["answer"]

                st.success("Here's what I found:")
                st.markdown(f"<p style='font-size:20px'><b>🧠 {answer}</b></p>", unsafe_allow_html=True)

                # 🔊 Autoplay answer
                play_audio_auto(answer)

            else:
                st.error("Sorry! Something went wrong.")
