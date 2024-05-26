from fastapi import FastAPI, File, UploadFile, HTTPException
from PIL import Image
import io
import os
import google.generativeai as genai
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain.chains import LLMChain
from config import template

load_dotenv()

app = FastAPI()

# Configuration
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))  # Replace with your API key
llm = ChatGroq(temperature=0, model_name="mixtral-8x7b-32768")

# Utility functions
def do_ocr(img_blob):
    model = genai.GenerativeModel("gemini-pro-vision")
    response = model.generate_content(img_blob)
    return response.text

def generate_response(question, answer):
    prompt = PromptTemplate(template=template, input_variables=["question","answer"])
    llm_chain = LLMChain(prompt=prompt, llm=llm)
    response = llm_chain.invoke({"question":question, "answer":answer})
    return response


# Define endpoints
@app.post("/process_images/")
async def process_images(question_img: UploadFile = File(...), answer_img: UploadFile = File(...)):
    question_image = Image.open(io.BytesIO(await question_img.read()))
    answer_image = Image.open(io.BytesIO(await answer_img.read()))
    
    question_text = do_ocr(question_image)
    answer_text = do_ocr(answer_image)
    
    response = generate_response(question_text, answer_text)
    # return {"response": response, "question_text": question_text, "answer_text": answer_text}
    return {"response": response}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8002)

#! RUN COMMAND uvicorn main:app --reload --port=8002 --host=0.0.0.0
#! Hit POST request on "http://localhost:8000/process_images/" with question_img and answer_img as request body

