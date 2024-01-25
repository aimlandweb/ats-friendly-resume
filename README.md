# ATS Resume Expert

ATS Resume Expert is a Streamlit-based application designed to assist job seekers and HR professionals by analyzing resumes against job descriptions. Utilizing the power of Google's Generative AI model "gemini-pro-vision", it offers insights and recommendations to enhance the resume's alignment with specific job requirements.

## Resume Analysis

- **HR/Human Resume Analysis**: Detailed analysis of how well a resume might be perceived by human recruiters.
- **ATS/AI Resume Analysis**: In-depth insights into how well the resume is likely to be parsed and understood by ATS software.

## Resume Optimization

- **ATS Friendly Resume Suggestions**: Provides recommendations on how to format and structure the resume to be more ATS-friendly.

## Skills Review

- **Skills Matching**: Compares the resume against job descriptions to suggest necessary skills and qualifications that might be missing.

## Additional Tools

- **Cover Letter Generator**: Offers guidance and suggestions for writing compelling cover letters tailored to specific job applications.
- **LinkedIn Profile Recommendations**: Tips on how to improve LinkedIn profiles to attract recruiters and align with the job market.
- **Interview Preparation**: A set of potential interview questions and tips on how to approach interviews.
- **Similar Company Suggestions**: Recommends similar companies to apply to, based on the job description and resume content.

## Interactive and User-Friendly Interface

- **File Uploads**: Easy upload of resumes in PDF format.
- **Responsive Design**: A user-friendly interface that is easy to navigate.
- **Real-Time Analysis**: Quick processing and analysis of uploaded documents.

## Technologies Used

- **Streamlit**: For creating the web application.
- **PyMuPDF**: For PDF processing and analysis.
- **Google GenerativeAI**: For generating content and analysis reports.
- Additional Python libraries: `base64`, `io`, `textwrap`, `tempfile`.

## Installation

To run the ATS Resume Expert application, follow these steps:

1. Clone the repository:

2. Navigate to the app's directory:

3. Install the required dependencies:

4. Set up your environment variables:

- Rename `.env.example` to `.env`.
- Add your `GOOGLE_API_KEY` to the `.env` file.

5.Run the Streamlit app:

## Usage

1. **Start the Application**: Run the command `streamlit run app.py` and navigate to the provided local URL.

2. **Enter Job Description**: Paste the job description in the provided text area.

3. **Upload Resume**: Upload the resume in PDF format.

4. **Choose a Feature**: Select from the available tabs to perform different analyses or tasks.

5. **View Results**: The app will display results based on the selected feature and the provided inputs.

## Troubleshooting

If you encounter issues, especially with PDF uploads, ensure the file is not empty or corrupted. Check the error messages for specifics.

## Contributing

Contributions to enhance ATS Resume Expert are welcome. Please follow standard procedures for contributing to open-source projects.

## License

MIT
