import streamlit as st
from PIL import Image

css_file = "./style/main.css"
resume_file = "./assets/Resume.pdf"
profile_image = "./assets/avatar_edited.png"

# GLOBAL CONFIG
page_title = "Resume | Nguyen Ba Viet Ha"
page_icon = "🧑‍🎓"
name = "Nguyen Ba Viet Ha"
description = "Senior Data Scientist | Senior Data Analyst"
email = "haviet20@gmail.com"
media = {
    "LinkedIn": "https://www.linkedin.com/in/hanguyen94/",
    "GitHub": "https://github.com/firefox94"
}

# BODY
st.set_page_config(page_title=page_title, page_icon=page_icon, layout="wide")

# load CSS
with open(css_file) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_image = Image.open(profile_image)

# HEADER
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_image, width=230)
with col2:
    st.title(name)
    st.write(description)
    st.download_button(
        label="📃 Download Resume",
        data=PDFbyte,
        file_name="Resume_Nguyen_Ba_Viet_Ha.pdf",
        mime="application/pdf"
    )
    
    st.write("📧", email)


# SOCIAL MEDIA
st.write('#')
cols = st.columns(len(media))
for i, (platform, link) in enumerate(media.items()):
    with cols[i]:
        st.markdown(f"- [{platform}]({link})")

# EXPERIENCE
st.write('#')
st.subheader("Working Experience")
st.write("""
         - **Senior Data Scientist** at [LPBank](https://lpbank.com.vn/ve-lpbank/) (Nov 2024 - Present)
         - **Senior Business Intelligence** at [VPBank](https://www.vpbank.com.vn/ve-chung-toi/) (Jul 2024 - Oct 2024)
         - **Data Analyst | Data Scientist** at [MBAgeas Life](https://www.mbageas.life/page/khoi-nguon/) (Jan 2022 - Jun 2024)
         """)

# SKILLS
st.write('#')
st.subheader("Skills")
st.write("""
         - **Programming Languages:** Python, SQL
         - **Data Visualization:** Power BI, Matplotlib
         - **Machine Learning:** Scikit-learn, XGBoost, LightGBM
         - **Deep Learning:** Pytorch, Keras
         - **Big Data Technologies:**  Spark
         """)

# EDUCATION
st.write('#')   
st.subheader("Education")
st.write("""
         - **Bachelor of Business Management** at [National Economics University](https://www.neu.edu.vn/) (2012 - 2016)
         """)

# PROJECTS
st.write('#')   
st.subheader("Projects")
st.write("""
         - **Customer Churn Prediction:** Developed a model to predict customer churn using machine learning techniques.
         - **ML Health Claim Fraudulent Detection:** Implemented a machine learning model to detect fraudulent health claims.
         - **ML Miss/Force Selling Detection:** Created a model to identify misselling and force selling in insurance.
         - **ML Persistency Prediction:** Developed a model to predict customer who are going to lapse.
         """)
         