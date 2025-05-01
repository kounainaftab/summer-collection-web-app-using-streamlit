import streamlit as st
from PIL import Image
import os

# Set up image directory
IMAGE_DIR = "summer_images"
os.makedirs(IMAGE_DIR, exist_ok=True)

st.set_page_config(page_title="☀️ Summer Collection", layout="wide")

st.title("☀️ Summer Collection Showcase")
st.markdown("Discover our fresh, vibrant summer styles and products!")

# Upload Section
st.sidebar.header("➕ Add to Collection")
with st.sidebar.form("upload_form", clear_on_submit=True):
    uploaded_file = st.file_uploader("Upload image", type=["jpg", "jpeg", "png"])
    title = st.text_input("Item Name")
    description = st.text_area("Short Description")
    submit = st.form_submit_button("Add to Collection")

    if submit and uploaded_file:
        filepath = os.path.join(IMAGE_DIR, uploaded_file.name)
        with open(filepath, "wb") as f:
            f.write(uploaded_file.getbuffer())
        with open(filepath + ".txt", "w") as f:
            f.write(f"{title}\n{description}")
        st.sidebar.success("Item added!")

# Display Collection
st.subheader("🌴 Our Summer Picks")
cols = st.columns(3)
images = [f for f in os.listdir(IMAGE_DIR) if f.lower().endswith(('png', 'jpg', 'jpeg'))]

if not images:
    st.info("No summer items yet. Use the sidebar to upload.")
else:
    for i, img_file in enumerate(images):
        img_path = os.path.join(IMAGE_DIR, img_file)
        meta_path = img_path + ".txt"

        with cols[i % 3]:
            image = Image.open(img_path)
            st.image(image, use_column_width=True)
            
            title = "Untitled"
            description = ""
            if os.path.exists(meta_path):
                with open(meta_path, "r") as f:
                    lines = f.readlines()
                    if lines:
                        title = lines[0].strip()
                    if len(lines) > 1:
                        description = lines[1].strip()
            st.subheader(title)
            st.caption(description)

st.markdown("---")
st.markdown("👩‍💻 Made with ❤️ by Kounain Aftab", unsafe_allow_html=True)