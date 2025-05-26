import streamlit as st
import os
from datetime import datetime

# Title
st.title("ItsmeTapi - My Data Journey")

#st.image("https://realpython.com/cdn-cgi/image/width=640,format=auto/https://files.realpython.com/media/Pythons-Math-Module-Guide_Watermarked.c882e267cbd0.jpg.jpg",
#             caption="(Tapioca would still approve this image!)", use_container_width=True)

# Show the image at the top (using relative path)
image_path = os.path.join(os.path.dirname(__file__), "pictures", "2_Pythons-Math-Module-Guide.png")
st.image(image_path, caption="Python Math Module Guide", use_container_width=True)


# Load posts from posts/ folder
posts_dir = os.path.join(os.path.dirname(__file__), "posts")
post_files = sorted(os.listdir(posts_dir), reverse=True)

for post_file in post_files:
    with open(os.path.join(posts_dir, post_file), "r") as f:
        post_content = f.read()

    st.markdown(f"### {post_file.replace('.md', '')}")
    st.markdown(post_content)
    st.markdown("---")


# Footer
st.write(f"Written with love and Python - {datetime.now().strftime('%B %d, %Y')}")

# Comments section
note = st.text_area("Leave a note on my blog:")
if st.button("Send"):
    st.success("Thanks for your message! 💌")

