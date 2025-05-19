import streamlit as st
from transformers import pipeline
from langchain.llms import HuggingFacePipeline
from langchain import LLMChain
from langchain.prompts import PromptTemplate

# ===== Streamlit UI =====

st.set_page_config(page_title="🌐 AI Translator App with Transformers & LangChain", layout="centered")
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🌐 AI Translator App</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 18px;'>Translate English text to any language in seconds!</p>", unsafe_allow_html=True)
st.divider()

language_to_translate = st.selectbox(
    label="Select a language to translate to:",
    options=["English", "French", "German", 'Romanian', "Spanish"]
)

text_to_translate = st.text_area("✏️ Enter the text you want to translate:")
translate_btn = st.button("Translate")

# ===== Set up Hugging Face Transformers pipeline =====

# Initialize a text2text-generation pipeline using T5-base model
translation_pipeline = pipeline(
    "text2text-generation",
    model="t5-base",
    tokenizer="t5-base",
    max_length=200
)

# Wrap the pipeline with LangChain's HuggingFacePipeline LLM wrapper
llm = HuggingFacePipeline(pipeline=translation_pipeline)

# Define the prompt template for translation
prompt_template = PromptTemplate(
    input_variables=["text", "language"],
    template="translate English to {language}: {text}"
)

# Create an LLMChain with the prompt and the llm
translation_chain = LLMChain(llm=llm, prompt=prompt_template)

st.markdown("---")
st.subheader("📝 Translated Text")

if translate_btn and text_to_translate.strip() != "":
    # Generate the translation via LangChain chain
    translation = translation_chain.run(text=text_to_translate, language=language_to_translate)
    st.write(translation)
    st.balloons()

elif translate_btn:
    st.warning("⚠️ Please enter some text before translating.")

st.markdown("---")
st.caption("Made with ❤️ using Streamlit, Transformers, and LangChain")
