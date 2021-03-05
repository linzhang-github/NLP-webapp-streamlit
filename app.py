import streamlit as st
import pandas as pd
import numpy as np

import streamlit as st
from readability import Readability
import nltk
import string 
from nltk.corpus import stopwords 
from PIL import Image 
from nltk.sentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt 
#pip insrall Pillow
# pip install matplotlib
# add sidebar 
@st.cache(suppress_st_warning=True,ttl=60*5,max_entries=20)
def sentiment_score(content): 
    sia = SentimentIntensityAnalyzer()
    new_key = {'neg':'Negative', 'neu':'Neutral', 'pos':'Positive'}
    dic_result = sia.polarity_scores(content)
    dic_rm_compd = {k:dic_result[k] for k in list(dic_result.keys())[:3]} 
    dic_replace_key = dict((new_key[key], value) for (key, value) in dic_rm_compd.items())
    max_tuple = max(dic_replace_key.items(), key = lambda k : k[1]) 
    return max_tuple, dic_replace_key, f'Predict: {max_tuple[0]} with {100*round(max_tuple[1],2)}% confidence' 


def readability_score(content): 
	r = Readability(content)
	read_name = ['flesch kincaid','flesch','gunning fog','coleman liau','dale chall','ari', 'linsear write', 'spache'] 
	read_metric = [r.flesch_kincaid(),r.flesch(),r.gunning_fog(),r.coleman_liau(),r.dale_chall(),r.ari(),r.linsear_write(),r.spache()]
	read_dic = dict(zip(read_name,read_metric))
	read_metric_new = [str(read_dic[k]) for k in read_dic]
	read_dic_new = dict(zip(read_name,read_metric_new)) 
	df = pd.DataFrame.from_dict(read_dic_new, orient = 'index').reset_index()
	df.columns = ['readability metric','score']
	return df  


#this is to remove the matplot error with streamlit 
st.set_option('deprecation.showPyplotGlobalUse', False)
st.sidebar.header('About this product:')
st.sidebar.write("Hello, I am Lin Zhang. Check on my [Github](https://github.com/linzhang-github)\
				for this product deployment detail. Feel free to reach out to me via \
				[LinkedIn](https://www.linkedin.com/in/linzhang-us/).\
				 I'd love to know your thoughts :).")
st.sidebar.write("The product is built on:")  
# image

im1= Image.open("NLP-image.jpg")
im2 = Image.open("streamlit-logo.jpg")
im3= Image.open("docker-logo.jpg")
im4= Image.open("aws-logo.jpg")


st.sidebar.image(im1)
st.sidebar.image(im2)
st.sidebar.image(im3)
st.sidebar.image(im4)

st.title('Text Analyzer')
st.write(' This Text Analyzer tool is designed to allow people to do quick sentiment analysis\
			and readability metrics analysis for their text, help them better understand and write their content.')
st.markdown('## **1. Sentiment Analysis**')
st.write("Do you want to identify the emotional tone behind a series of words? Paste your text in the box and see what happens.") 
sentence_1 = st.text_input('')  


if st.button('Click me for Sentiment Result'):
	if sentence_1:
		st.write(sentiment_score(sentence_1)[2])  


st.markdown('## **2. Readability Metrics**')
st.write("Do you want to judge how easy your text is to understand by audience? \
		That's how Readability Score matters. A readability score is an objective\
		measure of the complexity of text.\
		A great readability score means your content is easy to read.\
		Our Readability Metrics Analyzer will give you different metric scores which can\
		help you determine how easy your text is to understand by audience!") 
	
sentence_2 = st.text_input('Paste your text here, must over 100 words.')   

try: 
	if st.button('Click me for the Readability Result'): 
		if sentence_2: 
			st.table(readability_score(sentence_2)) 

except:
	st.error("At least 100 words required.")
	st.stop() 













