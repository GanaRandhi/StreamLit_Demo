import streamlit as st
import streamlit.components.v1 as components
import base64
from pathlib import Path

# Set page config
st.set_page_config(
    page_title="Famous Art Gallery",
    page_icon="🎨",
    layout="wide"
)

# Function to read and embed HTML
def read_html_file(file_path):
    return Path(file_path).read_text()

# Main app
def main():
    # Inject custom HTML
    html_content = read_html_file("index.html")
    components.html(html_content, height=800)

if __name__ == "__main__":
    main()

