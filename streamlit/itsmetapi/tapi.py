import streamlit as st
import os
from datetime import datetime

# Title
st.title("ItsmeTapi - My Data Journey")

# Load posts from posts/ folder
posts_dir = os.path.join(os.path.dirname(__file__), "posts")
post_files = sorted(os.listdir(posts_dir))

for post_file in post_files:
    with open(os.path.join(posts_dir, post_file), "r") as f:
        post_content = f.read()

    st.markdown(f"### {post_file.replace('.md', '')}")
    st.markdown(post_content)
    st.markdown("---")

    st.image("https://imgs.search.brave.com/tyTVOoRZY6yPK-hgqH1rFvtSo56YX-kOJBfnhD0ftA0/rs:fit:500:0:0:0/g:ce/aHR0cHM6Ly9maWxl/cy5yZWFscHl0aG9u/LmNvbS9tZWRpYS9Q/eXRob25zLU1hdGgt/TW9kdWxlLUd1aWRl/X1dhdGVybWFya2Vk/LmM4ODJlMjY3Y2Jk/MC5qcGc.jpg",
             caption="(Tapioca would still approve this image!)", use_container_width=True)

# Footer
st.write(f"Written with love and Python - {datetime.now().strftime('%B %d, %Y')}")

# Comments section
note = st.text_area("Leave a note on my blog:")
if st.button("Send"):
    st.success("Thanks for your message! 💌")

