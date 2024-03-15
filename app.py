# import base64
# import streamlit as st
# import os
# from dotenv import load_dotenv  # Move this import here
# load_dotenv()
# import io
# from PIL import Image
# import pdf2image
# import google.generativeai as genai

# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# def get_gemini_response(input, pdf_content, prompt):
#     model = genai.GenerativeModel('gemini-pro-vision')
#     response = model.generate_content([input, pdf_content[0], prompt])

#     # Accessing the text content using the appropriate accessor
#     text_content = response.parts[0].text if response.parts else "No text found in the response"
#     return text_content


# def input_pdf_setup(uploaded_file):
#     if uploaded_file is not None:
#         ## Convert the PDF to image
#         images = pdf2image.convert_from_bytes(uploaded_file.read())

#         first_page = images[0]

#         # Convert to bytes
#         img_byte_arr = io.BytesIO()
#         first_page.save(img_byte_arr, format='JPEG')
#         img_byte_arr = img_byte_arr.getvalue()

#         pdf_parts = [
#             {
#                 "mime_type": "image/jpeg",
#                 "data": base64.b64encode(img_byte_arr).decode()  # encode to base64
#             }
#         ]
#         return pdf_parts
#     else:
#         raise FileNotFoundError("No file uploaded")

# ## Streamlit App

# st.set_page_config(page_title="ATS Resume EXpert")
# st.header("ATS Tracking System")
# input_text = st.text_area("Job Description: ", key="input")
# uploaded_file = st.file_uploader("Upload your resume(PDF)...", type=["pdf"])

# if uploaded_file is not None:
#     st.write("PDF Uploaded Successfully")

# submit1 = st.button("Tell Me About the Resume")
# submit3 = st.button("Percentage match")

# input_prompt1 = """
#  You are an experienced Technical Human Resource Manager, your task is to review the provided resume against the job description. 
#   Please share your professional evaluation on whether the candidate's profile aligns with the role. 
#  Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.
# """

# input_prompt3 = """
# You are a skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science and ATS functionality, 
# your task is to evaluate the resume against the provided job description. give me the percentage of match if the resume matches
# the job description. First, the output should come as a percentage and then keywords missing and last final thoughts.
# """

# if submit1:
#     if uploaded_file is not None:
#         pdf_content = input_pdf_setup(uploaded_file)
#         response = get_gemini_response(input_prompt1, pdf_content, input_text)
#         st.subheader("The Response is")
#         st.write(response)
#     else:
#         st.write("Please upload the resume")

# elif submit3:
#     if uploaded_file is not None:
#         pdf_content = input_pdf_setup(uploaded_file)
#         response = get_gemini_response(input_prompt3, pdf_content, input_text)
#         st.subheader("The Response is")
#         st.write(response)
#     else:
#         st.write("Please upload the resume")
#################################################################################################################################################
#################################################################################################################################################
#################################################################################################################################################

# import base64
# import streamlit as st
# import os
# from dotenv import load_dotenv
# import io
# from PIL import Image
# import pdf2image
# import docx2txt
# import google.generativeai as genai

# # Load environment variables
# load_dotenv()

# # Configure Generative AI
# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# # Function to get Gemini response
# def get_gemini_response(input, pdf_content, prompt):
#     model = genai.GenerativeModel('gemini-pro-vision')
#     response = model.generate_content([input, pdf_content[0], prompt])

#     # Accessing the text content using the appropriate accessor
#     text_content = response.parts[0].text if response.parts else "No text found in the response"
#     return text_content

# # Function to setup PDF content
# def input_pdf_setup(uploaded_file):
#     if uploaded_file is not None:
#         images = pdf2image.convert_from_bytes(uploaded_file.read())
#         first_page = images[0]

#         # Convert to bytes
#         img_byte_arr = io.BytesIO()
#         first_page.save(img_byte_arr, format='JPEG')
#         img_byte_arr = img_byte_arr.getvalue()

#         pdf_parts = [
#             {
#                 "mime_type": "image/jpeg",
#                 "data": base64.b64encode(img_byte_arr).decode()  # encode to base64
#             }
#         ]
#         return pdf_parts
#     else:
#         raise FileNotFoundError("No file uploaded")

# # Streamlit App

# # Custom color values
# custom_background_color = "#f0f0f0"
# custom_primary_color = "#ff5733"  # Orange
# custom_secondary_color = "#333333"  # Dark Gray

# # Apply styling with custom colors
# st.markdown(
#     f"""
#     <style>
#         body {{
#             background-color: {custom_background_color};
#             font-family: 'Arial', sans-serif;
#         }}
#         h1, .stApp {{
#             color: {custom_primary_color};
#             text-align: center;
#         }}
#         h2, h3, .stMarkdown {{
#             color: {custom_secondary_color};
#         }}
#         .stTextInput, .stFileUploader, .stButton, .stTextArea {{
#             border-color: {custom_primary_color};
#         }}
#         .stTextInput, .stFileUploader, .stButton:hover {{
#             background-color: {custom_primary_color};
#             color: white;
#         }}
#     </style>
#     """
#     , unsafe_allow_html=True
# )


# # Header
# st.markdown("<h1> Deloitte ATS Resume Analyzer</h1>", unsafe_allow_html=True)
# st.header("Applicant Tracking System built by Emmanuel")

# # Job description input
# input_text = st.text_area("Job Description: ", key="input", height=150, help="Enter the job description here...")

# # Resume uploader
# uploaded_file = st.file_uploader("Upload your resume (PDF)...", type=["pdf"], help="Click to upload a resume")

# if uploaded_file is not None:
#     st.success("PDF Uploaded Successfully")

# # Buttons
# submit1 = st.button("Tell Me About the Resume")
# submit2 = st.button("Improve My Skills")
# submit3 = st.button("Percentage Match")
# submit4 = st.button("Strengths and Weaknesses")
# submit5 = st.button("Final Thoughts")
# submit6 = st.button("People Analytics")

# # Prompts
# input_prompt1 = """
# As an experienced Technical Human Resource Manager, your responsibility is to thoroughly assess the provided resume in comparison to the job description for the Data Scientist position. Share a detailed professional evaluation, highlighting the alignment of the candidate's profile with the role requirements. Please identify and emphasize both the strengths and weaknesses of the applicant, specifically focusing on their qualifications, skills, and experiences relevant to the specified job requirements. Your evaluation will play a crucial role in determining the candidate's suitability for the position.

# """

# input_prompt2 = """
# In your role as a career development expert, your task is to offer valuable guidance to the candidate for skill improvement and resume enhancement. Provide specific recommendations on how the candidate can further develop their skills to align better with industry expectations. Highlight areas for improvement and suggest practical steps for enhancing their resume, making it more appealing to potential employers. Your insights will contribute to the candidate's professional growth and career advancement.

# """

# input_prompt3 = """
# As a skilled ATS (Applicant Tracking System) scanner with a profound understanding of data science and ATS functionality, your primary responsibility is to evaluate the provided resume in comparison to the given job description. Begin by providing the percentage match between the resume and job description, indicating the degree of alignment. Following the percentage match, identify and list any keywords that are missing from the resume but are crucial for the specified job requirements. Conclude your evaluation with final thoughts, summarizing key insights and recommendations based on the assessment.

# """

# input_prompt4 = """
# In your role as a senior recruiter, your task is to meticulously analyze the applicant's profile in relation to the specified job requirements. Provide a comprehensive assessment by highlighting the candidate's strengths and weaknesses. Emphasize how the applicant's qualifications, skills, and experiences align with the key requirements of the job. Your insights will play a crucial role in making an informed decision regarding the candidate's suitability for the position.

# """

# input_prompt5 = """
# As the hiring manager, your pivotal role involves making a definitive decision on whether the candidate is well-suited for the role. Share your conclusive thoughts on the applicant's overall suitability based on their qualifications, skills, and alignment with the job requirements. Consider both the strengths and weaknesses identified during the evaluation process. Your final thoughts will contribute significantly to the hiring decision and the candidate's potential success in the role.

# """

# input_prompt6 = """
# In your capacity as a people analytics specialist, your focus is on evaluating the candidate's potential beyond technical skills. Assess the individual's capabilities in terms of teamwork, communication skills, adaptability, and cultural fit. Provide insights into how well the candidate is likely to collaborate with others, communicate effectively, adapt to diverse work environments, and align with the organizational culture. Your evaluation will offer a holistic perspective on the candidate's suitability for the role.

# """

# # Handle button clicks
# if submit1:
#     if uploaded_file is not None:
#         pdf_content = input_pdf_setup(uploaded_file)
#         response = get_gemini_response(input_prompt1, pdf_content, input_text)
#         st.subheader("Professional Evaluation:")
#         st.write(response)
#     else:
#         st.warning("Please upload the resume")

# elif submit2:
#     if uploaded_file is not None:
#         pdf_content = input_pdf_setup(uploaded_file)
#         response = get_gemini_response(input_prompt2, pdf_content, input_text)
#         st.subheader("Skill Improvement Suggestions:")
#         st.write(response)
#     else:
#         st.warning("Please upload the resume")

# elif submit3:
#     if uploaded_file is not None:
#         pdf_content = input_pdf_setup(uploaded_file)
#         response = get_gemini_response(input_prompt3, pdf_content, input_text)
#         st.subheader("Resume Match Analysis:")
#         st.write(response)
#     else:
#         st.warning("Please upload the resume")

# # ...

# elif submit4:
#     if uploaded_file is not None:
#         pdf_content = input_pdf_setup(uploaded_file)
#         response = get_gemini_response(input_prompt4, pdf_content, input_text)
#         st.subheader("Strengths and Weaknesses:")
#         st.write(response)
#     else:
#         st.warning("Please upload the resume")

# elif submit5:
#     if uploaded_file is not None:
#         pdf_content = input_pdf_setup(uploaded_file)
#         response = get_gemini_response(input_prompt5, pdf_content, input_text)
#         st.subheader("Final Thoughts:")
#         st.write(response)
#     else:
#         st.warning("Please upload the resume")

# elif submit6:
#     if uploaded_file is not None:
#         pdf_content = input_pdf_setup(uploaded_file)
#         response = get_gemini_response(input_prompt6, pdf_content, input_text)
#         st.subheader("People Analytics Evaluation:")
#         st.write(response)
#         st.success("People Analytics analysis is complete!")
#     else:
#         st.warning("Please upload the resume")




#################################################################################################################################################
#################################################################################################################################################
#####################################working fine############################################################################################################


# import base64
# import streamlit as st
# import os
# from dotenv import load_dotenv
# import io
# from PIL import Image
# import pdf2image
# import docx2txt
# import google.generativeai as genai

# # Load environment variables
# load_dotenv()

# # Configure Generative AI
# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# # Function to get Gemini response
# def get_gemini_response(input, pdf_content, prompt):
#     model = genai.GenerativeModel('gemini-pro-vision')
#     response = model.generate_content([input, pdf_content[0], prompt])

#     # Accessing the text content using the appropriate accessor
#     text_content = response.parts[0].text if response.parts else "No text found in the response"
#     return text_content

# # Function to setup PDF content
# def input_pdf_setup(uploaded_file):
#     if uploaded_file is not None:
#         images = pdf2image.convert_from_bytes(uploaded_file.read())
#         first_page = images[0]

#         # Convert to bytes
#         img_byte_arr = io.BytesIO()
#         first_page.save(img_byte_arr, format='JPEG')
#         img_byte_arr = img_byte_arr.getvalue()

#         pdf_parts = [
#             {
#                 "mime_type": "image/jpeg",
#                 "data": base64.b64encode(img_byte_arr).decode()  # encode to base64
#             }
#         ]
#         return pdf_parts
#     else:
#         raise FileNotFoundError("No file uploaded")

# # Custom color values
# custom_background_color = "#f0f0f0"
# custom_primary_color = "#ff5733"  # Orange
# custom_secondary_color = "#333333"  # Dark Gray

# # Apply styling with custom colors
# st.markdown(
#     f"""
#     <style>
#         body {{
#             background-color: {custom_background_color};
#             font-family: 'Arial', sans-serif;
#         }}
#         h1, .stApp {{
#             color: {custom_primary_color};
#             text-align: center;
#         }}
#         h2, h3, .stMarkdown {{
#             color: {custom_secondary_color};
#         }}
#         .stTextInput, .stFileUploader, .stButton, .stTextArea {{
#             border-color: {custom_primary_color};
#         }}
#         .stTextInput, .stFileUploader, .stButton:hover {{
#             background-color: {custom_primary_color};
#             color: white;
#         }}
#     </style>
#     """
#     , unsafe_allow_html=True
# )

# # Streamlit App
# st.title("Deloitte ATS Resume Analyzer")
# st.header("Applicant Tracking System for People Analytics Team")

# # Job description input
# input_text = st.text_area("Job Description: ", key="input", height=150, help="Enter the job description here...")

# # Resume uploader
# uploaded_file = st.file_uploader("Upload your resume (PDF)...", type=["pdf"], help="Click to upload a resume")

# if uploaded_file is not None:
#     st.success("PDF Uploaded Successfully")


# # Buttons
# submit1 = st.button("Technical HR Manager Evaluation")
# submit2 = st.button("Career Development Suggestions")
# submit3 = st.button("ATS Scanner Analysis")
# submit4 = st.button("Senior Recruiter Assessment")
# submit5 = st.button("Hiring Manager Decision")
# submit6 = st.button("People Analytics Evaluation")

# # Prompts
# input_prompt1 = """
# As an experienced Technical Human Resource Manager, your responsibility is to thoroughly assess the provided resume in comparison to the job description for the Data Scientist position. Share a detailed professional evaluation, highlighting the alignment of the candidate's profile with the role requirements. Please identify and emphasize both the strengths and weaknesses of the applicant, specifically focusing on their qualifications, skills, and experiences relevant to the specified job requirements. Your evaluation will play a crucial role in determining the candidate's suitability for the position.
# """

# input_prompt2 = """
# In your role as a career development expert, your task is to offer valuable guidance to the candidate for skill improvement and resume enhancement. Provide specific recommendations on how the candidate can further develop their skills to align better with industry expectations. Highlight areas for improvement and suggest practical steps for enhancing their resume, making it more appealing to potential employers. Your insights will contribute to the candidate's professional growth and career advancement.
# """

# input_prompt3 = """
# As a skilled ATS (Applicant Tracking System) scanner with a profound understanding of data science and ATS functionality, your primary responsibility is to evaluate the provided resume in comparison to the given job description. Begin by providing the percentage match between the resume and job description, indicating the degree of alignment. Following the percentage match, identify and list any keywords that are missing from the resume but are crucial for the specified job requirements. Conclude your evaluation with final thoughts, summarizing key insights and recommendations based on the assessment.
# """

# input_prompt4 = """
# In your role as a senior recruiter, your task is to meticulously analyze the applicant's profile in relation to the specified job requirements. Provide a comprehensive assessment by highlighting the candidate's strengths and weaknesses. Emphasize how the applicant's qualifications, skills, and experiences align with the key requirements of the job. Your insights will play a crucial role in making an informed decision regarding the candidate's suitability for the position.
# """

# input_prompt5 = """
# As the hiring manager, your pivotal role involves making a definitive decision on whether the candidate is well-suited for the role. Share your conclusive thoughts on the applicant's overall suitability based on their qualifications, skills, and alignment with the job requirements. Consider both the strengths and weaknesses identified during the evaluation process. Your final thoughts will contribute significantly to the hiring decision and the candidate's potential success in the role.
# """

# input_prompt6 = """
# In your capacity as a people analytics specialist, your focus is on evaluating the candidate's potential beyond technical skills. Assess the individual's capabilities in terms of teamwork, communication skills, adaptability, and cultural fit. Provide insights into how well the candidate is likely to collaborate with others, communicate effectively, adapt to diverse work environments, and align with the organizational culture. Your evaluation will offer a holistic perspective on the candidate's suitability for the role.
# """


# # Handle button clicks
# if submit1:
#     if uploaded_file is not None:
#         pdf_content = input_pdf_setup(uploaded_file)
#         response = get_gemini_response(input_prompt1, pdf_content, input_text)
#         st.subheader("Technical HR Manager Evaluation:")
#         st.write(response)
#     else:
#         st.warning("Please upload the resume")

# elif submit2:
#     if uploaded_file is not None:
#         pdf_content = input_pdf_setup(uploaded_file)
#         response = get_gemini_response(input_prompt2, pdf_content, input_text)
#         st.subheader("Career Development Suggestions:")
#         st.write(response)
#     else:
#         st.warning("Please upload the resume")

# elif submit3:
#     if uploaded_file is not None:
#         pdf_content = input_pdf_setup(uploaded_file)
#         response = get_gemini_response(input_prompt3, pdf_content, input_text)
#         st.subheader("ATS Scanner Analysis:")
#         st.write(response)
#     else:
#         st.warning("Please upload the resume")

# # ...

# elif submit4:
#     if uploaded_file is not None:
#         pdf_content = input_pdf_setup(uploaded_file)
#         response = get_gemini_response(input_prompt4, pdf_content, input_text)
#         st.subheader("Senior Recruiter Assessment:")
#         st.write(response)
#     else:
#         st.warning("Please upload the resume")

# elif submit5:
#     if uploaded_file is not None:
#         pdf_content = input_pdf_setup(uploaded_file)
#         response = get_gemini_response(input_prompt5, pdf_content, input_text)
#         st.subheader("Hiring Manager Decision:")
#         st.write(response)
#     else:
#         st.warning("Please upload the resume")

# elif submit6:
#     if uploaded_file is not None:
#         pdf_content = input_pdf_setup(uploaded_file)
#         response = get_gemini_response(input_prompt6, pdf_content, input_text)
#         st.subheader("People Analytics Evaluation:")
#         st.write(response)
#         st.success("People Analytics analysis is complete!")
#     else:
#         st.warning("Please upload the resume")

#################################################################################################
        ############################################################
        ####################changes shivani#######################################

# import base64
# import streamlit as st
# import os
# from dotenv import load_dotenv
# import io
# from PIL import Image
# import pdf2image
# import docx2txt
# import google.generativeai as genai

# # Load environment variables
# load_dotenv()

# # Configure Generative AI
# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
# import warnings

# @st.cache_data(show_spinner=True)
# @st.cache_resource()
# def get_gemini_response(input, pdf_content, prompt):
#     try:
#         model = genai.GenerativeModel('gemini-pro-vision')
#         response = model.generate_content([input, pdf_content[0], prompt])

#         # Accessing the text content using the appropriate accessor
#         text_content = response.parts[0].text if response.parts else "No text found in the response"
#         return text_content
#     except Exception as e:
#         st.error(f"Error in generating response: {str(e)}")
#         return None

# # Function to setup PDF content
# def input_pdf_setup(uploaded_file):
#     if uploaded_file is not None:
#         images = pdf2image.convert_from_bytes(uploaded_file.read())
#         first_page = images[0]

#         # Convert to bytes
#         img_byte_arr = io.BytesIO()
#         first_page.save(img_byte_arr, format='JPEG')
#         img_byte_arr = img_byte_arr.getvalue()

#         pdf_parts = [
#             {
#                 "mime_type": "image/jpeg",
#                 "data": base64.b64encode(img_byte_arr).decode()  # encode to base64
#             }
#         ]
#         return pdf_parts
#     else:
#         raise FileNotFoundError("No file uploaded")

# # Custom color values
# custom_background_color = "#f0f0f0"
# custom_primary_color = "#ff5733"  # Orange
# custom_secondary_color = "#333333"  # Dark Gray

# # Apply styling with custom colors
# st.markdown(
#     f"""
#     <style>
#         body {{
#             background-color: {custom_background_color};
#             font-family: 'Arial', sans-serif;
#         }}
#         h1, .stApp {{
#             color: {custom_primary_color};
#             text-align: center;
#         }}
#         h2, h3, .stMarkdown {{
#             color: {custom_secondary_color};
#         }}
#         .stTextInput, .stFileUploader, .stButton, .stTextArea {{
#             border-color: {custom_primary_color};
#         }}
#         .stTextInput, .stFileUploader, .stButton:hover {{
#             background-color: {custom_primary_color};
#             color: white;
#         }}
#     </style>
#     """
#     , unsafe_allow_html=True
# )

# # Streamlit App
# st.title("Deloitte ATS Resume Analyzer")
# st.header("Applicant Tracking System")

# # Job description input
# input_text = st.text_area("Job Description: ", key="input", height=150, help="Enter the job description here...")

# # Resume uploader
# uploaded_file = st.file_uploader("Upload your resume (PDF)...", type=["pdf"], help="Click to upload a resume")

# if uploaded_file is not None:
#     st.success("PDF Uploaded Successfully")


# # Buttons
# submit1 = st.button("Technical HR Manager Evaluation")
# submit2 = st.button("Career Development Suggestions")
# submit3 = st.button("ATS Scanner Analysis")
# # submit4 = st.button("Senior Recruiter Assessment")
# submit5 = st.button("Hiring Manager Decision")
# submit6 = st.button("People Analytics Evaluation")
# submit7 = st.button("interview questions based on resume")

# # Updated Prompts

# input_prompt1 = """
# 1.extract and list skills and education baground of the resume as{skills from resume{}:}.
# 2.extract and list skills and education baground from the job description as{skills from jod description{}:}.
# 3.now compare the extracted skills and education baground from the resume and extracted skills and education baground from the job description.
# 2.if the skills and qualifications from resume do not match the skills and qualifications mentioned in the job description then you can conclude candidate is not fit for the position because of the missalignment in the skills and education.
# 3.if the skills of resume and job description matches then you can conclude candidate is good fit for the position based on the skills and education baground.
# """

# input_prompt2 = """
# 1.Advise the candidate on enhancing skills not reflected in the resume compared to the job description.
# 2.Provide clear steps for advancing professionally.
# 3.suggest relevant online courses and projects based on job description.
# 4.Guide the candidate on tailoring their resume for technical and interpersonal strengths.
# 5.Offer advice for a successful career trajectory.
# """
# input_prompt3 = """
# 1. Extract skills from the candidate's resume and skills from the job description separately.
# 2. Calculate the skills match percentage by comparing the skills from the resume to the skills in the job description, and express it as {percentage match of skills}.
# 3. If the calculated skills match percentage is below 40 then reject candidate if above 40 accept the candidate.
# 4. Provide a list of skills that are present in the job description but absent in the resume.

# """

# input_prompt5 = """
# 2.calculate and show the total years of experience from the resume as{total experience mentioned in the resume is:}.
# 3.show the total experience mentioned in the job description{total experience mentioned in the job description is:}.
# 3.compare if the experience mentioned in the resume is matching to the experience mentioned in Jod description.
# 4.if experience is not matching reject the candidate based on experience.
# """

# input_prompt6 = """
# 1.based on resume Assess interpersonal skills, communication, and team collaboration potential.
# 2.based on resume content Recommend leveraging unique strengths for enhanced team dynamics.
# 3.Address potential collaborative challenges and propose solutions.
# 4.Evaluate impact on team synergy and organizational success.
# """
# input_prompt7="""
# 1.based on the skills mentioned in resume and projects mentioned in resume give top10 intervew questions.
# 2.based on projects mentioned in the resume give top5 possible expected questions from the interviewer.
# """



# # Handle button clicks
# if submit1:
#     if uploaded_file is not None:
#         pdf_content = input_pdf_setup(uploaded_file)

#         response = get_gemini_response(input_prompt1, pdf_content, input_text)
#         st.subheader("Technical HR Manager Evaluation:")
#         st.write(f'<p style="color: orange;">{response}</p>', unsafe_allow_html=True)
#         st.warning("Please upload the resume")


# elif submit2:
#     if uploaded_file is not None:
#         pdf_content = input_pdf_setup(uploaded_file)
#         response = get_gemini_response(input_prompt2, pdf_content, input_text)
#         st.subheader("Career Development Suggestions:")
#         st.write(response)
#     else:
#         st.warning("Please upload the resume")


# elif submit3:
#     if uploaded_file is not None:
#         pdf_content = input_pdf_setup(uploaded_file)
#         response = get_gemini_response(input_prompt3, pdf_content, input_text)
#         st.subheader("ATS Scanner Analysis:")
#         st.write(f'<span style="color: orange;">{response}</span>', unsafe_allow_html=True)
#     else:
#         st.warning("Please upload the resume")


# elif submit5:
#     if uploaded_file is not None:
#         pdf_content = input_pdf_setup(uploaded_file)
#         response = get_gemini_response(input_prompt5, pdf_content, input_text)
#         st.subheader("Hiring Manager Decision:")
#         st.write(response)
#     else:
#         st.warning("Please upload the resume")

# elif submit6:
#     if uploaded_file is not None:
#         pdf_content = input_pdf_setup(uploaded_file)
#         response = get_gemini_response(input_prompt6, pdf_content, input_text)
#         st.subheader("People Analytics Evaluation:")
#         st.write(response)
#         st.success("People Analytics analysis is complete!")
#     else:
#         st.warning("Please upload the resume")


# elif submit7:
#     if uploaded_file is not None:
#         pdf_content = input_pdf_setup(uploaded_file)
#         response = get_gemini_response(input_prompt7, pdf_content, input_text)
#         st.subheader("interview questions based on resume:")
#         st.write(response)
#         st.success("these are the best interview questions you can prepare")
#     else:
#         st.warning("Please upload the resume")



###$$$$$$$$$$$$$$$$$$$$##################$$$$$$$$$$$$$$$$$$$$$$$$$$$######################
        ###############################################$$$$$$$$$$$$$$$$$$$$$$$$$$$$










# import base64
# import streamlit as st
# import os
# from dotenv import load_dotenv
# import io
# from PIL import Image
# import pdf2image
# import google.generativeai as genai

# # Load environment variables
# load_dotenv()

# # Configure Generative AI
# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
# import warnings

# @st.cache_data(show_spinner=True)
# @st.cache_resource()
# def get_gemini_response(input, pdf_content, prompt):
#     try:
#         model = genai.GenerativeModel('gemini-pro-vision')
#         response = model.generate_content([input, pdf_content[0], prompt])

#         # Accessing the text content using the appropriate accessor
#         text_content = response.parts[0].text if response.parts else "No text found in the response"
#         return text_content
#     except Exception as e:
#         st.error(f"Error in generating response: {str(e)}")
#         return None

# def input_pdf_setup(uploaded_file):
#     if uploaded_file is not None:
#         images = pdf2image.convert_from_bytes(uploaded_file.read())
#         first_page = images[0]

#         # Convert to bytes
#         img_byte_arr = io.BytesIO()
#         first_page.save(img_byte_arr, format='JPEG')
#         img_byte_arr = img_byte_arr.getvalue()

#         pdf_parts = [
#             {
#                 "mime_type": "image/jpeg",
#                 "data": base64.b64encode(img_byte_arr).decode()  # encode to base64
#             }
#         ]
#         return pdf_parts
#     else:
#         raise FileNotFoundError("No file uploaded")

# def apply_custom_styling():
#     st.markdown(
#         """
#         <style>
#             body { background-color: #f0f0f0; font-family: 'Arial', sans-serif; }
#             h1, .stApp { color: #ff5733; text-align: center; }
#             h2, h3, .stMarkdown { color: #333333; }
#             .stTextInput, .stFileUploader, .stButton, .stTextArea { border-color: #ff5733; }
#             .stTextInput, .stFileUploader, .stButton:hover { background-color: #ff5733; color: white; }
#         </style>
#         """
#         , unsafe_allow_html=True
#     )

# def display_results(title, response):
#     st.subheader(title)
#     st.write(response)

# def handle_button_click(button_name, prompt, uploaded_file, input_text, additional_check=None):
#     if uploaded_file is not None:
#         pdf_content = input_pdf_setup(uploaded_file)
#         response = get_gemini_response(prompt, pdf_content, input_text)
#         display_results(button_name, response)
#         if additional_check:
#             additional_check()
#     else:
#         st.warning("Please upload the resume")

# # Streamlit App setup
# apply_custom_styling()
# st.title("Deloitte ATS Resume Analyzer")
# st.header("Applicant Tracking System")

# # Job description input
# input_text = st.text_area("Job Description: ", key="input", height=150, help="Enter the job description here...")

# # Resume uploader
# uploaded_file = st.file_uploader("Upload your resume (PDF)...", type=["pdf"], help="Click to upload a resume")

# if uploaded_file is not None:
#     st.success("PDF Uploaded Successfully")

# # Buttons
# submit1 = st.button("Technical HR Manager Evaluation")
# submit2 = st.button("Career Development Suggestions")
# submit3 = st.button("ATS Scanner Analysis")
# submit5 = st.button("Hiring Manager Decision")
# submit6 = st.button("People Analytics Evaluation")
# submit7 = st.button("Interview Questions based on Resume")

# # Updated Prompts
# input_prompt1 = """
# 1.extract and list skills and education baground of the resume as{skills from resume{}:}.
# 2.extract and list skills and education baground from the job description as{skills from jod description{}:}.
# 3.now compare the extracted skills and education baground from the resume and extracted skills and education baground from the job description.
# 2.if the skills and qualifications from resume do not match the skills and qualifications mentioned in the job description then you can conclude candidate is not fit for the position because of the missalignment in the skills and education.
# 3.if the skills of resume and job description matches then you can conclude candidate is good fit for the position based on the skills and education baground.
# """

# input_prompt2 = """
# 1.Advise the candidate on enhancing skills not reflected in the resume compared to the job description.
# 2.Provide clear steps for advancing professionally.
# 3.suggest relevant online courses and projects based on job description.
# 4.Guide the candidate on tailoring their resume for technical and interpersonal strengths.
# 5.Offer advice for a successful career trajectory.
# """
# input_prompt3 = """
# 1. Extract skills from the candidate's resume and skills from the job description separately.
# 2. Calculate the skills match percentage by comparing the skills from the resume to the skills in the job description, and express it as {percentage match of skills}.
# 3. If the calculated skills match percentage is below 40 then reject candidate if above 40 accept the candidate.
# 4. Provide a list of skills that are present in the job description but absent in the resume.

# """

# input_prompt5 = """
# 2.calculate and show the total years of experience from the resume as{total experience mentioned in the resume is:}.
# 3.show the total experience mentioned in the job description{total experience mentioned in the job description is:}.
# 3.compare if the experience mentioned in the resume is matching to the experience mentioned in Jod description.
# 4.if experience is not matching reject the candidate based on experience.
# """

# input_prompt6 = """
# 1.based on resume Assess interpersonal skills, communication, and team collaboration potential.
# 2.based on resume content Recommend leveraging unique strengths for enhanced team dynamics.
# 3.Address potential collaborative challenges and propose solutions.
# 4.Evaluate impact on team synergy and organizational success.
# """
# input_prompt7="""
# 1.based on the skills mentioned in resume and projects mentioned in resume give top10 intervew questions.
# 2.based on projects mentioned in the resume give top5 possible expected questions from the interviewer.
# """

# # Handle button clicks
# if submit1:
#     handle_button_click("Technical HR Manager Evaluation", input_prompt1, uploaded_file, input_text)

# elif submit2:
#     handle_button_click("Career Development Suggestions", input_prompt2, uploaded_file, input_text)

# elif submit3:
#     handle_button_click("ATS Scanner Analysis", input_prompt3, uploaded_file, input_text)

# elif submit5:
#     handle_button_click("Hiring Manager Decision", input_prompt5, uploaded_file, input_text)

# elif submit6:
#     handle_button_click("People Analytics Evaluation", input_prompt6, uploaded_file, input_text)

# elif submit7:
#     handle_button_click("Interview Questions based on Resume", input_prompt7, uploaded_file, input_text)



# import base64
# import streamlit as st
# import os
# from dotenv import load_dotenv
# import io
# from PIL import Image
# import pdf2image
# import google.generativeai as genai

# # Load environment variables
# load_dotenv()

# # Configure Generative AI
# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
# import warnings

# @st.cache_data(show_spinner=True)
# @st.cache_resource()
# def get_gemini_response(input, pdf_content, prompt):
#     try:
#         model = genai.GenerativeModel('gemini-pro-vision')
#         response = model.generate_content([input, pdf_content[0], prompt])

#         # Accessing the text content using the appropriate accessor
#         text_content = response.parts[0].text if response.parts else "No text found in the response"
#         return text_content
#     except Exception as e:
#         st.error(f"Error in generating response: {str(e)}")
#         return None

# def input_pdf_setup(uploaded_file):
#     if uploaded_file is not None:
#         images = pdf2image.convert_from_bytes(uploaded_file.read())
#         first_page = images[0]

#         # Convert to bytes
#         img_byte_arr = io.BytesIO()
#         first_page.save(img_byte_arr, format='JPEG')
#         img_byte_arr = img_byte_arr.getvalue()

#         pdf_parts = [
#             {
#                 "mime_type": "image/jpeg",
#                 "data": base64.b64encode(img_byte_arr).decode()  # encode to base64
#             }
#         ]
#         return pdf_parts
#     else:
#         raise FileNotFoundError("No file uploaded")

# def apply_custom_styling():
#     st.markdown(
#         """
#         <style>
#             body { background-color: #f0f0f0; font-family: 'Arial', sans-serif; }
#             h1, .stApp { color: #ff5733; text-align: center; }
#             h2, h3, .stMarkdown { color: #333333; }
#             .stTextInput, .stFileUploader, .stButton, .stTextArea { border-color: #ff5733; }
#             .stTextInput, .stFileUploader, .stButton:hover { background-color: #ff5733; color: white; }
#         </style>
#         """
#         , unsafe_allow_html=True
#     )

# def display_results(title, response):
#     st.subheader(title)
#     st.write(response)

# def handle_button_click(button_name, prompt, uploaded_file, input_text, additional_check=None):
#     if uploaded_file is not None:
#         pdf_content = input_pdf_setup(uploaded_file)
#         response = get_gemini_response(prompt, pdf_content, input_text)
#         display_results(button_name, response)
#         if additional_check:
#             additional_check()
#     else:
#         st.warning("Please upload the resume")

# # Streamlit App setup
# apply_custom_styling()
# st.title("Deloitte ATS Resume Analyzer")
# st.header("Applicant Tracking System")

# # Job description input
# input_text = st.text_area("Job Description: ", key="input", height=150, help="Enter the job description here...")

# # Resume uploader
# uploaded_file = st.file_uploader("Upload your resume (PDF)...", type=["pdf"], help="Click to upload a resume")

# if uploaded_file is not None:
#     st.success("PDF Uploaded Successfully")

# # Buttons
# submit1 = st.button("Technical HR Manager Evaluation")
# submit2 = st.button("Career Development Suggestions")
# submit3 = st.button("ATS Scanner Analysis")
# submit5 = st.button("Hiring Manager Decision")
# submit6 = st.button("People Analytics Evaluation")
# submit7 = st.button("Interview Questions based on Resume")

# # Updated Prompts
# input_prompt1 = """1.extract and list skills and education baground of the resume as{skills from resume{}:}..."""
# input_prompt2 = """1.Advise the candidate on enhancing skills not reflected in the resume compared to the job description..."""
# input_prompt3 = """1. Extract skills from the candidate's resume and skills from the job description separately..."""
# input_prompt5 = """2.calculate and show the total years of experience from the resume as{total experience mentioned in the resume is:}..."""
# input_prompt6 = """1.based on resume Assess interpersonal skills, communication, and team collaboration potential..."""
# input_prompt7 = """1.based on the skills mentioned in resume and projects mentioned in resume give top10 interview questions..."""

# # Handle button clicks
# if submit1:
#     handle_button_click("Technical HR Manager Evaluation", input_prompt1, uploaded_file, input_text)

# elif submit2:
#     handle_button_click("Career Development Suggestions", input_prompt2, uploaded_file, input_text)

# elif submit3:
#     handle_button_click("ATS Scanner Analysis", input_prompt3, uploaded_file, input_text)

# elif submit5:
#     handle_button_click("Hiring Manager Decision", input_prompt5, uploaded_file, input_text)

# elif submit6:
#     handle_button_click("People Analytics Evaluation", input_prompt6, uploaded_file, input_text)

# elif submit7:
#     handle_button_click("Interview Questions based on Resume", input_prompt7, uploaded_file, input_text)



# import base64
# import streamlit as st
# import os
# from dotenv import load_dotenv
# import io
# from PIL import Image
# import pdf2image
# import google.generativeai as genai

# # Load Environment Variables
# load_dotenv()

# # Configure Generative AI
# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# # Error Handling
# def handle_error(error_message):
#     st.error(f"Error: {error_message}")

# # PDF Setup
# def input_pdf_setup(uploaded_file):
#     try:
#         if uploaded_file is not None:
#             images = pdf2image.convert_from_bytes(uploaded_file.read())
#             first_page = images[0]

#             # Convert to bytes
#             img_byte_arr = io.BytesIO()
#             first_page.save(img_byte_arr, format='JPEG')
#             img_byte_arr = img_byte_arr.getvalue()

#             pdf_parts = [
#                 {
#                     "mime_type": "image/jpeg",
#                     "data": base64.b64encode(img_byte_arr).decode()  # encode to base64
#                 }
#             ]
#             return pdf_parts
#         else:
#             raise FileNotFoundError("No file uploaded")
#     except Exception as e:
#         handle_error(f"Error in input_pdf_setup: {str(e)}")
#         return None

# # Generative AI Response
# @st.cache_data(show_spinner=True)
# @st.cache_resource()
# def get_gemini_response(input, pdf_content, prompt):
#     try:
#         model = genai.GenerativeModel('gemini-pro-vision')
#         response = model.generate_content([input, pdf_content[0], prompt])

#         # Accessing the text content using the appropriate accessor
#         text_content = response.parts[0].text if response.parts else "No text found in the response"
#         return text_content
#     except Exception as e:
#         handle_error(f"Error in get_gemini_response: {str(e)}")
#         return None

# # Custom Styling
# def apply_custom_styling():
#     st.markdown(
#         """
#         <style>
#             body { background-color: #f0f0f0; font-family: 'Arial', sans-serif; }
#             h1, .stApp { color: #ff5733; text-align: center; }
#             h2, h3, .stMarkdown { color: #333333; }
#             .stTextInput, .stFileUploader, .stButton, .stTextArea { border-color: #ff5733; }
#             .stTextInput, .stFileUploader, .stButton:hover { background-color: #ff5733; color: white; }
#         </style>
#         """
#         , unsafe_allow_html=True
#     )

# # Display Results
# def display_results(title, response):
#     st.subheader(title)
#     st.write(response)

# # Button Handling
# def handle_button_click(button_name, prompt, uploaded_file, input_text, additional_check=None):
#     if uploaded_file is not None:
#         pdf_content = input_pdf_setup(uploaded_file)
#         if pdf_content:
#             response = get_gemini_response(prompt, pdf_content, input_text)
#             if response:
#                 display_results(button_name, response)
#                 if additional_check:
#                     additional_check()
#         else:
#             st.warning("Error in processing PDF")
#     else:
#         st.warning("Please upload the resume")

# # Streamlit App Setup
# apply_custom_styling()
# st.title("Deloitte ATS Resume Analyzer")
# st.header("Applicant Tracking System")

# # Job Description Input
# input_text = st.text_area("Job Description: ", key="input", height=150, help="Enter the job description here...")

# # Resume Uploader
# uploaded_file = st.file_uploader("Upload your resume (PDF)...", type=["pdf"], help="Click to upload a resume")

# if uploaded_file is not None:
#     st.success("PDF Uploaded Successfully")

# # ... (previous code remains unchanged)

# # Updated Prompts
# input_prompt1 = """1.extract and list skills and education baground of the resume as{skills from resume{}:}..."""

# # Buttons
# buttons = {"Technical HR Manager Evaluation": input_prompt1}

# for button_name, prompt in buttons.items():
#     if st.button(button_name):
#         handle_button_click(button_name, prompt, uploaded_file, input_text)





# import base64
# import streamlit as st
# import os
# from dotenv import load_dotenv
# import io
# import google.generativeai as genai
# import langid
# import PyPDF2

# # Load environment variables
# load_dotenv()

# # Configure Generative AI
# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# @st.cache_data(show_spinner=True)
# @st.cache_resource()
# def get_generative_ai_answer(input_text):
#     try:
#         model = genai.GenerativeModel('gemini-pro')  # Use the appropriate model for your task
#         response = model.generate_content([input_text])
#         text_content = response.parts[0].text if response.parts else "No text found in the response"
#         return text_content
#     except Exception as e:
#         st.error(f"Error in generating response: {str(e)}")
#         return None

# # Function to filter out non-English questions
# def filter_english_questions(question_paper_content):
#     filtered_questions = []
#     for line in question_paper_content.split('\n'):
#         lang, _ = langid.classify(line)
#         if lang == 'en':
#             filtered_questions.append(line)
#     return '\n'.join(filtered_questions)

# # Custom color values
# custom_background_color = "#f0f0f0"
# custom_primary_color = "#ff5733"  # Orange
# custom_secondary_color = "#333333"  # Dark Gray

# # Apply styling with custom colors
# st.markdown(
#     f"""
#     <style>
#         body {{
#             background-color: {custom_background_color};
#             font-family: 'Arial', sans-serif;
#         }}
#         h1, .stApp {{
#             color: {custom_primary_color};
#             text-align: center;
#         }}
#         h2, h3, .stMarkdown {{
#             color: {custom_secondary_color};
#         }}
#         .stTextInput, .stFileUploader, .stButton, .stTextArea {{
#             border-color: {custom_primary_color};
#         }}
#         .stTextInput, .stFileUploader, .stButton:hover {{
#             background-color: {custom_primary_color};
#             color: white;
#         }}
#     </style>
#     """
#     , unsafe_allow_html=True
# )

# # Streamlit App
# st.title("Question Answering Application")
# st.header("Generative AI-based Question Answering")

# # Question paper upload
# uploaded_file = st.file_uploader("Upload Question Paper (Text file or PDF):", type=["txt", "pdf"])

# # Button for generating answers
# submit_question_answer = st.button("Generate Answers")

# # Handle button click for question answering
# if submit_question_answer:
#     if uploaded_file is not None:
#         content_type = uploaded_file.type
#         question_paper_content = uploaded_file.read()

#         if content_type == 'text/plain':
#             # Text file, decode as UTF-8
#             question_paper_content = question_paper_content.decode("utf-8")
#         elif content_type == 'application/pdf':
#             # PDF file, extract text using PyPDF2
#             pdf_reader = PyPDF2.PdfReader(io.BytesIO(question_paper_content))
#             question_paper_content = ''
#             for page_num in range(len(pdf_reader.pages)):
#                 question_paper_content += pdf_reader.pages[page_num].extract_text()

#         # Filter out non-English questions
#         english_question_paper_content = filter_english_questions(question_paper_content)

#         st.subheader("Generated Answers:")
#         answer = get_generative_ai_answer(english_question_paper_content)
#         st.write(answer)
#     else:
#         st.warning("Please upload a question paper.")











# with custom buttons
#############################################################
##############################################################
############################################################



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
            pdf_reader = PyPDF2.PdfReader(io.BytesIO(question_paper_content))
            question_paper_content = ''
            for page_num in range(len(pdf_reader.pages)):
                question_paper_content += pdf_reader.pages[page_num].extract_text()

        # Filter out non-English questions
        english_question_paper_content = filter_english_questions(question_paper_content)

        st.subheader("Generated Answers:")
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



