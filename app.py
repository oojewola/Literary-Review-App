from fastapi import FastAPI, Form, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import pickle
import re
import nltk
import gensim
from sklearn.feature_extraction.text import TfidfVectorizer

nltk.download('stopwords')
nltk.download('punkt')
import numpy as np
import warnings
warnings.filterwarnings('ignore')
import uvicorn

app = FastAPI()
templates = Jinja2Templates(directory = '/Users/olusinaojewola/Desktop/flask/templates')

#load the model
with open("/Users/olusinaojewola/Desktop/flask/lr_model.pkl", "rb") as file : 
    model = pickle.load(file)
    
with open("/Users/olusinaojewola/Desktop/flask/tfidf_vectorizer.pkl", 'rb') as file:
    tfidf_vectorizer = pickle.load(file)

def preprocess(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]','', text, re.I|re.A)
    text = re.sub(r'\s+', ' ', text)
    vector = tfidf_vectorizer.transform([text])
    return vector

# create a endpoints
@app.get("/", response_class = HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("index.html",{"request":request})

@app.post("/predict/")
async def predict_rating(request: Request, review : str = Form(...)):
    preprocessed_text = preprocess(review)
    prediction  = model.predict(preprocessed_text)
    return templates.TemplateResponse("index.html", {"request": request, "prediction":prediction[0]})

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
