from dotenv import load_dotenv

load_dotenv()
import base64
import streamlit as st
import os
import io
import textwrap
import tempfile
from PIL import Image
import fitz
import google.generativeai as genai
from prompts import (
    input_prompt1,
    input_prompt2,
    input_prompt3,
    input_prompt4,
    input_prompt5,
    input_prompt6,
    input_prompt7,
    input_prompt8,
)

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


def extract_field_from_description(description):
    return input_role


def construct_prompt(template, field):
    return template.replace("[User-Specified Field]", field)


def to_markdown(text):
    text = text.replace("•", "  *")
    return textwrap.indent(text, "> ", predicate=lambda _: True)


def get_gemini_response(input, pdf_content, prompt):
    model = genai.GenerativeModel("gemini-pro-vision")
    response = model.generate_content([input, pdf_content[0], prompt])
    #   return response.text
    return to_markdown(response.text)


def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        file_content = uploaded_file.getvalue()
        if file_content:
            try:
                doc = fitz.open(stream=file_content, filetype="pdf")
                if len(doc) > 0:
                    page = doc.load_page(0)  # first page
                    pix = page.get_pixmap()
                    img_byte_arr = pix.tobytes("png")  # get bytes directly

                    pdf_parts = [
                        {
                            "mime_type": "image/png",
                            "data": base64.b64encode(img_byte_arr).decode(),
                        }
                    ]
                    return pdf_parts
                else:
                    raise ValueError("PDF does not contain any pages.")
            except Exception as e:
                st.error(f"Error processing PDF: {e}")
                raise e
            finally:
                doc.close()
        else:
            st.error("Uploaded file is empty or invalid.")
            raise ValueError("Uploaded file is empty or invalid.")
    else:
        st.error("No file uploaded.")
        raise FileNotFoundError("No file uploaded")


# Streamlit App

st.set_page_config(
    page_title="ATS Resume Expert",
    page_icon="🔥",
)
st.header("ATS Friendly Resume and Analysis")
input_name = st.text_input("Enter your name: ", key="name", placeholder="John Doe")
input_role = st.text_input(
    "Role you are applying for: ", key="role", placeholder="Software Engineer"
)

input_text = st.text_area(
    "Job Description: ", key="input", placeholder="Paste the job description here..."
)
uploaded_file = st.file_uploader("Upload your resume(PDF)", type=["pdf"])


if "input_text" not in st.session_state:
    st.session_state["input_text"] = input_text

if "input_name" not in st.session_state:
    st.session_state["input_name"] = input_name

if "input_role" not in st.session_state:
    st.session_state["input_role"] = input_role

if "input_text" not in st.session_state:
    st.session_state["input_text"] = input_text

if "uploaded_file" not in st.session_state:
    st.session_state["uploaded_file"] = uploaded_file


if uploaded_file is not None:
    st.write("PDF uploaded successfully!")

    # Prompts here

field = extract_field_from_description(input_text)


dynamic_prompt1 = construct_prompt(input_prompt1, field)
dynamic_prompt2 = construct_prompt(input_prompt2, field)
dynamic_prompt3 = construct_prompt(input_prompt3, field)
dynamic_prompt4 = construct_prompt(input_prompt4, field)
dynamic_prompt5 = construct_prompt(input_prompt5, field)
dynamic_prompt6 = construct_prompt(input_prompt6, field)
dynamic_prompt7 = construct_prompt(input_prompt7, field)
dynamic_prompt8 = construct_prompt(input_prompt8, field)
# Check if both the job description and the PDF file are provided
if input_text and uploaded_file:
    try:
        pdf_content = input_pdf_setup(uploaded_file)
        is_pdf_valid = True

    except Exception as e:
        st.error(f"Error processing the PDF file: {e}")
        is_pdf_valid = False

    if is_pdf_valid:
        # Process for each tab if PDF is valid
        field = extract_field_from_description(input_text)

        st.subheader("Name : " + input_name)
        st.subheader("Role : " + input_role)

        tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs(
            [
                "HR/Human Resume Analysis",
                "ATS/AI Resume Analysis",
                "Skills Review",
                "ATS Friendly Resume",
                "Cover Letter",
                "LinkedIn",
                "Interview Questions",
                "Similar Companies",
            ]
        )

        with tab1:
            st.header("HR/Human - Detailed Resume Analysis")
            if uploaded_file is not None:
                response = get_gemini_response(dynamic_prompt1, pdf_content, input_text)
                st.write(response)
            else:
                st.write("Please upload the resume")

        with tab2:
            st.header("ATS/AI - Detailed Resume Analysis")
            if uploaded_file is not None:
                response = get_gemini_response(dynamic_prompt2, pdf_content, input_text)
                st.write(response)
            else:
                st.write("Please upload the resume")

        with tab3:
            st.header("Skills Recommended for the Role")
            if uploaded_file is not None:
                response = get_gemini_response(dynamic_prompt3, pdf_content, input_text)
                st.write(response)
            else:
                st.write("Please upload the resume")
        with tab4:
            st.header("ATS Friendly and optimized Resume")
            if uploaded_file is not None:
                response = get_gemini_response(dynamic_prompt4, pdf_content, input_text)
                st.write(response)
            else:
                st.write("Please upload the resume")
        with tab5:
            st.header("Cover Letter for your resume")
            if uploaded_file is not None:
                response = get_gemini_response(dynamic_prompt5, pdf_content, input_text)
                st.write(response)
            else:
                st.write("Please upload the resume")
        with tab6:
            st.header("LinkedIn Profile Recommendations")
            if uploaded_file is not None:
                response = get_gemini_response(dynamic_prompt6, pdf_content, input_text)
                st.write(response)
            else:
                st.write("Please upload the resume")
        with tab7:
            st.header("Interview Questions and Questions to ask the interviewer")
            if uploaded_file is not None:
                response = get_gemini_response(dynamic_prompt7, pdf_content, input_text)
                st.write(response)
            else:
                st.write("Please upload the resume")
        with tab8:
            st.header("Similar companies you can apply for")
            if uploaded_file is not None:
                response = get_gemini_response(dynamic_prompt8, pdf_content, input_text)
                st.write(response)
            else:
                st.write("Please upload the resume")

else:
    st.write("Please provide the job description and upload the resume PDF.")
