import streamlit as st
import requests
import json
from streamlit_lottie import st_lottie

st.set_page_config(page_title="Report Page", page_icon=":tada:",layout="wide")

def load_lottieurl (url) :
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
lottie_coding = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_3rwasyjy.json")

with st.container():
    st.write("---")
    left_column,right_column = st.columns([3,1])
    with right_column:
        st_lottie(lottie_coding, height=250, key="coding")

    with left_column:
     st.title("Report ")
     contact_form = """
          <form action="https://formsubmit.co/shreyanigam129@gmail.com" method="POST">
             <input type="hidden" name="_captcha" value="false">
             <input type="text" name="name" placeholder="Enter your name" required>
             <input type="email" name="email"  placeholder="Enter the email address you want to report"  required>
              <textarea name="message" placeholder="Detail your problem"></textarea>
              <button type="submit">Submit</button>
          </form>
          """


     st.markdown(contact_form , unsafe_allow_html=True)

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}<style/>", unsafe_allow_html=True)

local_css("style.css")