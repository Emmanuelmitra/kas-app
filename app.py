import streamlit as st
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

# Function to generate PDF
def generate_pdf(content):
    # Set up the PDF canvas
    pdf_path = "output.pdf"
    c = canvas.Canvas(pdf_path, pagesize=letter)
    y = 750

    # Write content to PDF
    for line in content.split("\n"):
        c.drawString(100, y, line)
        y -= 12

    # Save the PDF
    c.save()
    return pdf_path

# Configure Streamlit app
st.title("Question Answering Application")
st.header("Generative AI-based Question Answering")

# Input field for single question
single_question = st.text_input("Enter a single question:")

# Button to generate answer for single question
submit_single_question = st.button("Generate Answer")

# Display generated answer for single question
if submit_single_question:
    if single_question:
        st.subheader("Generated Answer:")
        single_answer = get_generative_ai_answer(single_question)
        st.write(single_answer)
    else:
        st.warning("Please enter a question.")

# Question paper upload
uploaded_file = st.file_uploader("Upload Question Paper (Text file or PDF):", type=["txt", "pdf"])

# Button for generating answers
submit_question_answer = st.button("Generate Answers")

# Custom buttons with prompts
submit_prompt1 = st.button("Custom Prompt 1")
submit_prompt2 = st.button("Custom Prompt 2")

# Handle button click for question answering
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
                pdf_reader = PdfFileReader(io.BytesIO(question_paper_content))
                question_paper_content = ''
                for page_num in range(len(pdf_reader.pages)):
                    question_paper_content += pdf_reader.pages[page_num].extractText()
            except Exception as e:
                st.error(f"Error extracting text from PDF: {str(e)}")
                st.stop()

        # Filter out non-English questions
        english_question_paper_content = filter_english_questions(question_paper_content)

        st.subheader("Generated Answers:")
        answer = get_generative_ai_answer(english_question_paper_content)
        st.write(answer)

        # Generate and download PDF
        pdf_path = generate_pdf(answer)
        with open(pdf_path, "rb") as f:
            st.download_button(label="Download PDF", data=f, file_name="output.pdf", mime="application/pdf")

        # Delete the PDF file after download
        if os.path.exists("output.pdf"):
            os.remove("output.pdf")

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
