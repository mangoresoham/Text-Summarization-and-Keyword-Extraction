# Summarization and Keyword Extraction Tool

This project is a web-based application for summarizing text, identifying its domain, and extracting domain-specific keywords. The application is built using **Streamlit** and utilizes the **Groq API** for text processing. It is deployed on **Hugging Face Spaces** for easy access and usage.

## Features
- Upload a text file or input text directly.
- Generate a concise summary of the text.
- Identify the domain of the text (e.g., Technology, Healthcare, etc.).
- Extract domain-specific keywords.
- Easy-to-use interface with streamlined processing.

## How It Works
1. **Input Options**: Users can either upload a `.txt` file or paste the text directly into the provided text area.
2. **API Integration**: The application uses the Groq API to process the input and generate results.
3. **Output**: Results include a summary, domain identification, and a list of keywords displayed directly on the app.

## Deployed Platform
The application is deployed on **Hugging Face Spaces**, leveraging the simplicity and scalability of Streamlit for rapid prototyping.

[Visit the App on Hugging Face Spaces](https://huggingface.co/spaces/mangoresoham/Summarizer)

## Installation and Usage (Local Deployment)

To run the application locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/summarization-keyword-extraction.git
   cd summarization-keyword-extraction
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   streamlit run app.py
   ```

4. Open your browser and navigate to `http://localhost:8501`.

## Configuration
- The app requires a valid **GROQ API Key** for functionality.
- Enter the API key in the sidebar under the "Configuration" section.

## File Structure
- `app.py`: Main application file.
- `requirements.txt`: Contains the list of Python dependencies.
- `README.md`: Documentation for the project.

## Requirements
- Python 3.7+
- Streamlit
- Groq API

## Example Usage
### Input
- **Uploaded file**: Upload a `.txt` file containing your document.
- **Text area**: Paste or type text directly into the app.

### Output
- **Summary**: A brief overview of the document.
- **Domain**: The primary domain of the text.
- **Keywords**: A list of extracted domain-specific keywords.



