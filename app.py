import streamlit as st
import pickle
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

ps = PorterStemmer()


def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    y = []
    for i in text:
        if i.isalnum():
            y.append(i)
    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)



tfidf = pickle.load(open('vectorizer.pkl', 'rb'))


model = pickle.load(open('model.pkl', 'rb'))

st.title("Email/SMS Spam Classifier")

input_email = st.text_input("Enter your email ")

input_sms = st.text_area("Enter the message")

if st.button('Predict'):

    transform_sms = transform_text(input_sms)

    vector_input = tfidf.transform([transform_sms])

    result = model.predict(vector_input)

    if result == 1:
        st.header("spam")
        st.warning('Do you want to report this email address ? ', icon="⚠️")

    else:
        st.header("Not Spam")



def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<report>{f.read()}<style/>", unsafe_allow_html=True)

local_css("report.py")