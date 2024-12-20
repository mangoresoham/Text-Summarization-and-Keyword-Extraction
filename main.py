import streamlit as st
from groq import Groq
import os
st.set_page_config(layout="wide")

# Streamlit UI
st.title("Summarization and Keyword Extraction")
st.markdown("**Provide a text document or input text directly to generate a summary, identify the domain, and extract keywords.**")

# Sidebar for API key input
st.sidebar.header("Configuration")
api_key = st.sidebar.text_input("Enter your GROQ API Key", type="password")

# Input options
uploaded_file = st.file_uploader("Upload a text file", type=["txt"])
text_input = st.text_area("Or paste your text here")

# Process the input and fetch results
if st.button("Analyze"):
    if not api_key:
        st.error("Please provide your GROQ API Key in the sidebar.")
    else:
        # Initialize Groq client
        client = Groq(api_key=api_key)
        document_text = ""

        if uploaded_file:
            document_text = uploaded_file.read().decode("utf-8")
        elif text_input.strip():
            document_text = text_input.strip()

        if document_text:
            try:
                # Call Groq API for summarization and keyword extraction
                chat_completion = client.chat.completions.create(
                    messages=[
                        {
                            "role": "user",
                            "content": (
                                f"Summarize this document, "
                                f"Identify the domain of the document text, and "
                                f"list down domain-specific keywords: {document_text}"
                            ),
                        }
                    ],
                    model="llama3-8b-8192",
                )
                response = chat_completion.choices[0].message.content

                # Split response into sections
                summary_start = response.find("**Summary:**")
                domain_start = response.find("**Domain:**")
                keywords_start = response.find("**Domain-specific keywords:**")

                # Extract each section
                summary = response[summary_start + len("**Summary:**"):domain_start].strip()
                domain = response[domain_start + len("**Domain:**"):keywords_start].strip()
                keywords = response[keywords_start + len("**Domain-specific keywords:**"):].strip()

                # Clean up keywords (remove any extraneous brackets or list artifacts)
                keywords = keywords.replace("[", "").replace("]", "").replace("'", "")

                # Display results
                st.subheader("Summary")
                st.write(summary)

                st.subheader("Domain")
                st.write(domain)

                st.subheader("Keywords")
                st.write(keywords)
            except Exception as e:
                st.error(f"An error occurred: {e}")
        else:
            st.warning("Please provide a valid text input.")
