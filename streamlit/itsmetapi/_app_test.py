import streamlit as st
from datetime import datetime

# App Title
st.set_page_config(page_title="ItsmeTapi - My Data Journey", layout="wide")
st.title("Welcome to ItsmeTapi – My Data Journey Begins!")
st.subheader("In honor of my beloved Tapioca")

# Image placeholder
# st.image("https://placekitten.com/800/300", caption="(Tapioca would approve this image!)", use_container_width=True)
st.image("https://files.realpython.com/media/Polars-group_by-and-Aggregations_Watermarked.760a0c543c71.jpg", caption="(Tapioca would approve this image!)", use_container_width=True)

# Blog Content
st.markdown("""
This is not just a blog. It’s a story of transformation, curiosity, a bit of chaos, and a lot of code. A few days ago, I officially dived into the deep waters of Data Science, Machine Learning, and AI with a full-time bootcamp—and what a ride it’s been so far!

I call this space "ItsmeTapi" in honor of my beloved dog Tapioca, whose loyal presence always reminded me to stay grounded and keep a sense of playfulness, even in the most complex moments.


### Week 1: From Zero to API Hero (Almost)

Last week, I dove head-first into the world of **Data Science, Machine Learning, and AI** through a full-time bootcamp—and it’s already been wild, rewarding, and exhausting!

#### Here’s what I’ve explored so far:

- **Basic Python Toolkit**: Lists, loops, functions—my old friends now feel like power tools.
- **Exploratory Data Analysis (EDA)**: With pandas and matplotlib, I became a data detective.
- **APIs & Web Scraping**: Fetching job listings using BeautifulSoup and requests made me feel like a real-world coder.

---

### Student Life Mode: Full-Time Everything

Morning to afternoon, it’s bootcamp mode: lectures, notebooks, and hands-on projects. Then I switch gears and wrestle with German grammar in the evenings. My brain feels like a dual-core processor—running data models on one side and reflexive verbs on the other!

Yes, I’m tired. Yes, sometimes Python throws an error, and I feel like throwing the laptop back. But I also discovered that Python can "sleep"—with `time.sleep()` —and maybe I should, too. (Seriously, sleep matters.)

---

### Why This Blog?

Because every error, every success, and every weird plot is worth remembering. I want to document my learning, my struggles, and my small wins. I hope it inspires others who are thinking of switching careers, diving into tech, or simply wondering “can I really do this?” I want to share not just the *how*, but also the *feeling* of learning something from scratch.

This is my notebook, my digital garden, my tribute to Tapioca—and my way to say:
> **Yes, I can do this. And so can you.**

---

Stay tuned for code snippets, mini-projects, visualizations and everything to showcase what I’m learning. Tapioca would be proud.

Stay curious, and stay tuned!, and future updates!

*#ItsmeTapi #DataScienceDiary #BootcampLife*
""")

st.markdown("### Leave a note on my first post!")
note = st.text_area("Write your comment:")
if st.button("Send"):
    st.success("Thanks for your message! 💌")

# Footer
st.markdown("---")
st.write(f"Written with love and Python - {datetime.now().strftime('%B %d, %Y')}")
