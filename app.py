import base64
import streamlit as st
import os
from dotenv import load_dotenv
import io
import google.generativeai as genai
import langid
import PyPDF2

# Load environment variables
load_dotenv()

# Configure Generative AI
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

@st.cache_data(show_spinner=True)
@st.cache_resource()
def get_generative_ai_answer(input_text):
    try:
        model = genai.GenerativeModel('gemini-pro')  # Use the appropriate model for your task
        response = model.generate_content([input_text])
        text_content = response.parts[0].text if response.parts else "No text found in the response"
        return text_content
    except Exception as e:
        st.error(f"Error in generating response: {str(e)}")
        return None

# Function to filter out non-English questions
def filter_english_questions(question_paper_content):
    filtered_questions = []
    for line in question_paper_content.split('\n'):
        lang, _ = langid.classify(line)
        if lang == 'en':
            filtered_questions.append(line)
    return '\n'.join(filtered_questions)

# Custom color values
custom_background_color = "#f0f0f0"
custom_primary_color = "#ff5733"  # Orange
custom_secondary_color = "#333333"  # Dark Gray

# Apply styling with custom colors
st.markdown(
    f"""
    <style>
        body {{
            background-color: {custom_background_color};
            font-family: 'Arial', sans-serif;
        }}
        h1, .stApp {{
            color: {custom_primary_color};
            text-align: center;
        }}
        h2, h3, .stMarkdown {{
            color: {custom_secondary_color};
        }}
        .stTextInput, .stFileUploader, .stButton, .stTextArea {{
            border-color: {custom_primary_color};
        }}
        .stTextInput, .stFileUploader, .stButton:hover {{
            background-color: {custom_primary_color};
            color: white;
        }}
    </style>
    """
    , unsafe_allow_html=True
)

# Streamlit App
st.title("Question Answering Application")
st.header("Generative AI-based Question Answering")

# Single question input
single_question = st.text_input("Type your single question here")

# Button for generating answer for single question
submit_single_question = st.button("Get Answer for Single Question")

# Question paper upload
uploaded_file = st.file_uploader("Upload Question Paper (Text file or PDF):", type=["txt", "pdf"])

# Button for generating answers for uploaded question paper
submit_question_answer = st.button("Generate Answers")

# Custom buttons with prompts
submit_prompt1 = st.button("Custom Prompt 1")
submit_prompt2 = st.button("Custom Prompt 2")

# Handle button click for single question answering
if submit_single_question and single_question:
    st.subheader("Answer for Single Question:")
    single_answer = get_generative_ai_answer(single_question)
    st.write(single_answer)

# Handle button click for question answering for uploaded question paper
if submit_question_answer:
    if uploaded_file is not None:
        content_type = uploaded_file.type
        question_paper_content = uploaded_file.read()

        if content_type == 'text/plain':
            # Text file, decode as UTF-8
            question_paper_content = question_paper_content.decode("utf-8")
        elif content_type == 'application/pdf':
            # PDF file, extract text using PyPDF2
            try:
                pdf_reader = PyPDF2.PdfReader(io.BytesIO(question_paper_content))
                question_paper_content = ''
                for page in pdf_reader.pages:
                    question_paper_content += page.extract_text()
            except Exception as e:
                st.error(f"Error extracting text from PDF: {str(e)}")
                st.stop()

        # Filter out non-English questions
        english_question_paper_content = filter_english_questions(question_paper_content)

        st.subheader("Generated Answers for Uploaded Question Paper:")
        answer = get_generative_ai_answer(english_question_paper_content)
        st.write(answer)
    else:
        st.warning("Please upload a question paper.")

# Handle button clicks for custom prompts
if submit_prompt1:
    custom_prompt = "generate one similar question paper which is in systematic way to download"
    answer = get_generative_ai_answer(custom_prompt)
    st.subheader("Generated Answers (Custom Prompt 1):")
    st.write(answer)

if submit_prompt2:
    custom_prompt = "generate question papers of similar"
    answer = get_generative_ai_answer(custom_prompt)
    st.subheader("Generated Answers (Custom Prompt 2):")
    st.write(answer)
