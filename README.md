# AI-Translator-App
A user-friendly, lightweight AI-powered language translation assistant that instantly converts English text into several supported languages using state-of-the-art NLP models.

## What the Agent Does
This AI agent serves as a language translation assistant. It accepts English input and translates it into one of the following languages:
- French
- German
- Romanian
- Spanish
- (or back to English)

The agent uses a Transformer-based T5 model for translation and returns results in real-time through a streamlined web interface built with Streamlit.

## How It Interacts with the User
1. Streamlit Web Interface
- The user is welcomed by a clean and simple UI.
- They select a target language from a dropdown list.
- They type their text to be translated into a text area.
- Clicking the "Translate" button triggers the translation logic.
2. Translation Output
- The translated text is displayed immediately on the page.
- A balloon animation celebrates a successful translation.
- A warning message is shown if the "Translate" button is clicked with no input text.

## Key Technical Features
 Transformer Model (T5)
- Leverages the t5-base model from Hugging Face via the text2text-generation pipeline.
- T5 is a multi-task language model capable of performing translation and other NLP tasks.

LangChain Integration
- The Hugging Face pipeline is wrapped using LangChain's HuggingFacePipeline class.
- LLMChain handles prompt-to-model interactions with modular, reusable logic chains.

Streamlit Frontend
- Built using Streamlit for rapid UI prototyping.
- Uses widgets like selectbox, text_area, and button.
- Includes styled headers, input validation, and celebratory animations (st.balloons()).

