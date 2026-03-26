import streamlit as st
import pandas as pd
import base64

st.set_page_config(page_title="Decision Tree ID3 Presentation", layout="wide")

# ---------- BACKGROUND IMAGE ----------
def set_bg(image_file):

    with open(image_file, "rb") as file:
        encoded = base64.b64encode(file.read()).decode()

    st.markdown(
        f"""
        <style>

        .stApp {{
            background-image: url("data:image/png;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}

        h1,h2,h3,h4,h5,h6,p,li {{
            color:white;
        }}

        .slide-box{{
        height:80vh;
        display:flex;
        justify-content:center;
        align-items:center;
        }}

        .slide-content{{
        text-align:left;
        font-size:28px;
        margin-top:-110px;
        }}

        .slide-title{{
        text-align:center;
        font-size:48px;
        font-weight:bold;
        margin-bottom:25px;
        }}

        </style>
        """,
        unsafe_allow_html=True
    )

set_bg("stream3.png")


# ---------- SIDEBAR ----------
st.sidebar.title("Presentation Slides")

st.sidebar.markdown(
"""
### Project Link
[Open Colab Project](https://colab.research.google.com/drive/1_29o5uKeD-zDnlRTZCiQKx4ydy-l849B#scrollTo=ieQtS3sgADqW)

📊 **PPT Presentation**  
[Open PPT Presentation](https://onedrive.live.com/personal/7cf96e7fa5ee36e6/_layouts/15/doc.aspx?resid=cd200921-e43f-4c72-8b23-4eae4d168a3c&cid=7cf96e7fa5ee36e6)

"""
)

slide = st.sidebar.radio(
    "Go to",
    [
        "Title",
        "Aim",
        "Purpose",
        "Decision Tree Concept",
        "Working Principle",
        "Applications",
        "Advantages"
    ]
)


# -------- TITLE SLIDE --------
if slide == "Title":

    st.markdown("""
    <div style="
    height:80vh;
    display:flex;
    flex-direction:column;
    justify-content:center;
    align-items:center;
    text-align:center;
    color:white;
    font-family:'Patrick Hand', cursive;
    ">

    <p style="font-size:45px;">	 
    Decision Tree using ID3 Algorithm <br>

    <h2>Machine Learning Algorithm Lab</h2>
	
    <h3>MSc DS & AI</h3>​ 
    
    <h3>Shyam Sundar V</h3> 

    <h3>Reg No: 253692301025</h3> 

    </p>

    </div>
    """, unsafe_allow_html=True)


# -------- AIM --------
elif slide == "Aim":

    st.markdown("""
    <div class="slide-box">
    <div class="slide-content">

    <div class="slide-title">Aim</div>

    • Understand the concept of decision tree classification <br>
    • Study how ID3 algorithm selects optimal attributes <br>
    • Learn entropy and information gain fundamentals <br>
    • Build a basic predictive model using decision tree

    </div>
    </div>
    """, unsafe_allow_html=True)


# -------- PURPOSE --------
elif slide == "Purpose":

    st.markdown("""
    <div class="slide-box">
    <div class="slide-content">

    <div class="slide-title">Purpose</div>

    • To understand how machine learning models make structured decisions from data <br>
    • To explore how decision trees simplify complex decision-making problems <br>
    • To demonstrate how entropy and information gain guide the tree building process

    </div>
    </div>
    """, unsafe_allow_html=True)


# -------- DECISION TREE --------
elif slide == "Decision Tree Concept":

    st.markdown("""
    <div class="slide-box">
    <div class="slide-content">

    <div class="slide-title">Decision Tree Concept</div>

    • A supervised machine learning model used for classification <br>
    • Represents decisions using a tree-like hierarchical structure <br>
    • Root node represents the complete dataset <br>
    • Leaf nodes represent the final prediction outcomes

    </div>
    </div>
    """, unsafe_allow_html=True)


# -------- WORKING PRINCIPLE --------
elif slide == "Working Principle":

    st.markdown("""
    <div class="slide-box">
    <div class="slide-content">

    <div class="slide-title">Working Principle</div>

    • Decision trees split the dataset based on selected attributes <br>
    • Entropy measures randomness or impurity in the dataset <br>
    • Information gain helps select the best splitting attribute <br>
    • Highest gain attribute becomes the next decision node

    </div>
    </div>
    """, unsafe_allow_html=True)



# -------- APPLICATIONS --------
elif slide == "Applications":

    st.markdown("""
    <div class="slide-box">
    <div class="slide-content">

    <div class="slide-title">Applications</div>

    • Medical diagnosis and disease prediction <br>
    • Customer churn analysis in business <br>
    • Credit risk and loan approval systems <br>
    • Fraud detection in banking and finance

    </div>
    </div>
    """, unsafe_allow_html=True)


# -------- ADVANTAGES --------
elif slide == "Advantages":

    st.markdown("""
    <div class="slide-box">
    <div class="slide-content">

    <div class="slide-title">Advantages</div>

    • Easy to understand and interpret <br>
    • Works well with categorical data <br>
    • Requires minimal data preprocessing <br>
    • Provides clear decision-making structure

    </div>
    </div>
    """, unsafe_allow_html=True)
