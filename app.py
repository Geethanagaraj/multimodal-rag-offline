import streamlit as st
from src.local_llm import LocalLLM

# ------------------------
# Page Config
# ------------------------
st.set_page_config(
    page_title="Multimodal Offline Knowledge Engine",
    layout="wide"
)

# ------------------------
# Initialize LLM
# ------------------------
@st.cache_resource
def load_llm():
    return LocalLLM()

llm = load_llm()

# ------------------------
# Sidebar Navigation
# ------------------------
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Go to",
    ["Home", "Ask Question", "Summarize", "Compare", "Settings"]
)

# ------------------------
# HOME PAGE
# ------------------------
if page == "Home":
    st.title("🧠 Multimodal Offline Knowledge Engine")
    st.markdown("Upload, Search, Analyze — All Offline")

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Documents Indexed", "0")
    col2.metric("Model", "Llama-3.2-3B")
    col3.metric("Modalities", "Text | Image | Audio")
    col4.metric("Status", "Ready")

    st.markdown("---")
    st.info("Use the sidebar to begin querying your knowledge base.")

# ------------------------
# ASK QUESTION PAGE
# ------------------------
elif page == "Ask Question":
    st.title("🔍 Ask a Question")

    query = st.text_area("Enter your question")

    answer_style = st.selectbox(
        "Answer Style",
        ["Brief", "Detailed", "Step-by-step"]
    )

    with st.expander("Advanced Options"):
        top_k = st.slider("Top-K Retrieval", 1, 10, 3)
        modality = st.multiselect(
            "Filter by Modality",
            ["Text", "Image", "Audio"],
            default=["Text", "Image", "Audio"]
        )

    if st.button("Generate Answer"):
        if query.strip() == "":
            st.warning("Please enter a question.")
        else:
            # TODO: Replace with real retrieval
            retrieved_context = "Sample retrieved context."

            with st.spinner("Generating answer..."):
                response = llm.generate(retrieved_context, query)

            st.markdown("## 🧠 Answer")
            st.write(response)

            with st.expander("📄 Sources"):
                st.write("Source details will appear here.")

            st.caption("Confidence: 85% (Prototype estimation)")

# ------------------------
# SUMMARIZE PAGE
# ------------------------
elif page == "Summarize":
    st.title("📄 Summarize Documents")
    st.info("Document selection and summarization will be integrated here.")

# ------------------------
# COMPARE PAGE
# ------------------------
elif page == "Compare":
    st.title("📊 Compare Documents")
    st.info("Document comparison functionality coming soon.")

# ------------------------
# SETTINGS PAGE
# ------------------------
elif page == "Settings":
    st.title("⚙ Settings")
    st.write("Model configuration and indexing controls will be available here.")