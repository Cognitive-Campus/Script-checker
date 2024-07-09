



import google.generativeai as genai
from dotenv import load_dotenv
from PIL import Image
load_dotenv()

from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain.chains import LLMChain
from config import template

genai.configure(api_key='AIzaSyCrDt5iXSHAyHOYvzv4IBTRTkxaXIxeMpg')
# or use this newer one: 'j0hAAikxUsz3I1Rvqa4'
llm = ChatGroq(temperature=0, model_name="mixtral-8x7b-32768")

def do_ocr(img_blob):
    model = genai.GenerativeModel("gemini-pro-vision")
    response = model.generate_content(["You are an expert OCR software. You need to extract the text exactly as in the image. Just output the extracted text, and nothing else. If you can't find any text, then output NO TEXT DETECTED. Remeber to only output the extracted text!",
                                        img_blob])
    return response.text

def generate_response(question, answer):
  prompt = PromptTemplate(template=template, input_variables=["question","answer", "rating"])
  llm_chain = LLMChain(prompt=prompt, llm=llm)
  response = llm_chain.invoke({"question":question, "answer":answer, "rating":20})
  return response

def process_images(question_img_path, answer_img_path):
  
    question_image = Image.open(question_img_path)
    answer_image = Image.open(answer_img_path)
    
    question_text = do_ocr(question_image)
    answer_text = do_ocr(answer_image)
    
    response = generate_response(question_text, answer_text)
    return response, question_text, answer_text


# Example usage:
question_img_blob = R"D:\fyp\ai models\script checker\SRE.jpg"
answer_img_blob = R"D:\fyp\ai models\script checker\SRE.jpg"
response, question_text, answer_text = process_images(question_img_blob, answer_img_blob)

print("Response:", response)
print("Question Text:", question_text)
print("Answer Text:", answer_text)

