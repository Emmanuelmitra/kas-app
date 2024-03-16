import base64
import streamlit as st
import os
from dotenv import load_dotenv
import io
import google.generativeai as genai
import langid
from PyPDF2 import PdfReader

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
        return text_content, response
    except Exception as e:
        st.error(f"Error in generating response: {str(e)}")
        return None, None

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

# Toggle for language filtering
filter_language = st.checkbox("Filter English Questions", value=True)

# Individual question input
individual_question = st.text_area("Paste or type individual questions here", height=150, max_chars=1000)

# Button for generating answers for individual questions
submit_individual_question = st.button("Generate Answer for Individual Question")

# Question paper upload
uploaded_file = st.file_uploader("Upload Question Paper (Text file or PDF):", type=["txt", "pdf"])

# Button for generating answers for question paper
submit_question_answer = st.button("Generate Answers for Question Paper")

# Custom buttons with prompts
submit_prompt1 = st.button("Generate Effective Prompt 1")
submit_prompt2 = st.button("Generate Effective Prompt 2")

# Button for explanation of generated answer
submit_explanation = st.button("Explain Generated Answer")

# Display confidence scores
show_confidence_scores = st.checkbox("Display Confidence Scores", value=False)

# Handle button click for generating answer for individual question
if submit_individual_question:
    if individual_question:
        st.subheader("Generated Answer for Individual Question:")
        answer, response = get_generative_ai_answer(individual_question)
        if answer is not None:
            st.write(answer)
    else:
        st.warning("Please paste or type an individual question.")

# Handle button click for generating answer for question paper
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
                pdf_reader = PdfReader(io.BytesIO(question_paper_content))
                question_paper_content = ''
                for page_num in range(len(pdf_reader.pages)):
                    question_paper_content += pdf_reader.pages[page_num].extract_text()
            except Exception as e:
                st.error(f"Error extracting text from PDF: {str(e)}")
                st.stop()

        # Filter out non-English questions if enabled
        if filter_language:
            question_paper_content = filter_english_questions(question_paper_content)

        st.subheader("Generated Answers for Question Paper:")
        answer, _ = get_generative_ai_answer(question_paper_content)
        if answer is not None:
            st.write(answer)
            
        # Download button for generated answers
        if st.button("Download Answers"):
            output_filename = "generated_answers.txt"
            with open(output_filename, "w", encoding="utf-8") as f:
                f.write(answer)
            st.download_button(label="Click to download", data=output_filename, file_name=output_filename)

    else:
        st.warning("Please upload a question paper.")

# Handle button clicks for effective prompts
if submit_prompt1:
    effective_prompt1 = "Generate a detailed explanation of the concept of <concept_name>."
    st.subheader("Effective Prompt 1:")
    st.write(effective_prompt1)

if submit_prompt2:
    effective_prompt2 = "Create a comprehensive analysis of the <topic> and its implications on <industry/field>."
    st.subheader("Effective Prompt 2:")
    st.write(effective_prompt2)

# Handle button click for explanation of generated answer
if submit_explanation:
    explanation = "The generated answer is based on the input provided and the model's understanding of the context. For detailed insights, consider consulting a subject matter expert."
    st.subheader("Explanation of Generated Answer:")
    st.write(explanation)


