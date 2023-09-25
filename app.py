import pickle
import streamlit as st
from nltk.stem.porter import PorterStemmer
import nltk
from sklearn.feature_extraction.text import CountVectorizer

model = pickle.load(open('model.pkl', 'rb'))
cv = pickle.load(open('cv.pkl', 'rb'))


st.title('Fake News Predictor')
data = st.text_input("Enter Article Text")

def preprocess(text):
        ps = PorterStemmer()
        preprocessed_data = []
        words = nltk.word_tokenize(text) #tokenize the words
        stemmed_word = [ps.stem(word) for word in words]
        review = ' '.join(stemmed_word)
        preprocessed_data.append(review)
        return preprocessed_data

def predict(text):
    preprocess_data = preprocess(text)
    data = cv.transform(preprocess_data)
    prediction =model.predict(data)
    return prediction[0]

if st.button("Predict"):
    pred = predict(data)

    if pred  == 0:
        st.write('News is fake')

    else :
        st.write('News is real')