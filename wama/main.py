import streamlit as st
import PyPDF2
from models.summarizer_qa import load_models
from services.text_processing import clean_text, summarize_text, answer_question
from utils.logging_utils import setup_logger

# Set up logger
logger = setup_logger("TextSummarizerQA")

# Load models
summarizer_t5, summarizer_bart, qa_model, tokenizer = load_models()

# Streamlit UI
st.title("Article Summarizer and QA System")

# Sidebar with model information
with st.sidebar:
    st.header("🤖 Models Information")
    st.markdown("### Summarization Models")
    st.markdown("- **T5 (Text-to-Text Transfer Transformer)**")
    st.markdown("  - Fine-tuned for summarization tasks")
    st.markdown("  - Generates abstractive summaries")
    st.markdown("- **BART (Bidirectional Auto-Regressive Transformers)**")
    st.markdown("  - Facebook's pre-trained model")
    st.markdown("  - Optimized for text generation tasks")
    
    st.markdown("### Question Answering Model")
    st.markdown("- **BERT-based QA Model**")
    st.markdown("  - Extractive question answering")
    st.markdown("  - Provides confidence scores")
    
    st.markdown("---")
    st.caption("All models are pre-trained and optimized for performance")

# Input method
input_method = st.radio("Input Method", ("Paste Text", "Upload File"))

# Handle input
article = ""
if input_method == "Paste Text":
    article = st.text_area("Paste your article here:", height=300)
else:
    uploaded_file = st.file_uploader("Upload your article (PDF or TXT)", type=["pdf", "txt"])
    if uploaded_file is not None:
        try:
            if uploaded_file.type == "application/pdf":
                pdf_reader = PyPDF2.PdfReader(uploaded_file)
                for page in pdf_reader.pages:
                    extracted_text = page.extract_text()
                    if extracted_text:
                        article += extracted_text + " "
            else:
                article = uploaded_file.read().decode("utf-8")
        except Exception as e:
            st.error(f"Error reading file: {str(e)}")
            logger.error(f"File reading error: {str(e)}")

# Clean article text
if article:
    try:
        article = clean_text(article)
        st.subheader("Original Article")
        st.text_area("Article Content", article, height=200)

        # Summarization Section
        st.subheader("Summarization")
        summarizer_choice = st.selectbox("Choose Summarization Model", ("T5", "BART"))

        if st.button("Summarize"):
            try:
                summarizer = summarizer_t5 if summarizer_choice == "T5" else summarizer_bart
                summary = summarize_text(article, summarizer)
                st.text_area("Summary", summary, height=150)
                logger.info(f"Generated summary using {summarizer_choice}")
            except Exception as e:
                st.error(f"Error during summarization: {str(e)}")
                logger.error(f"Summarization error: {str(e)}")

        # QA Section
        st.subheader("Question Answering")
        question = st.text_input("Ask a question about the article:")

        if question and st.button("Get Answer"):
            try:
                answer, score = answer_question(question, article, qa_model, tokenizer)
                if answer:
                    st.write(f"Answer: {answer}")
                    st.write(f"Confidence Score: {score:.2f}")
                    logger.info(f"Answered question: {question}")
                else:
                    st.warning("No answer found in the article.")
                    logger.warning(f"No answer found for question: {question}")
            except Exception as e:
                st.error(f"Error during question answering: {str(e)}")
                logger.error(f"QA error: {str(e)}")
    except Exception as e:
        st.error(f"Error processing article: {str(e)}")
        logger.error(f"Article processing error: {str(e)}")
else:
    st.info("Please provide an article to get started.")
    
# Contact section
st.markdown("---")
st.markdown("## 📞 Contact ME")
st.markdown(
    """
    [![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Moataz899/Text-Summarizer-Question-Answering)
    [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/moataz-abdelraouf/)
    [![Email](https://img.shields.io/badge/Email-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](mailto:abdelraoufdahy%40gmail.com)
    """
)