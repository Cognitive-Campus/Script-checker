#! Standalone script that just takes in extract OCR text and returns a rating with a reason
# in json format

#! Creatting a merged report from the OCR text WILL BE FROM THE WEBSITE END

#! So this is just a simple AI micro-service that takes in an image as input and gives an output text as the rating for that image, with the reason. Now the website, will manage every user's uploaded image and the rating for that image in MongoDB. I was wondering if we could do this:

#! Teacher clicks on SCRIPT CHECKER 
#! Teacher sees an interface with a button saying "ADD AN IMAGE TO CHECK". When the teacher clicks on that image, they can upload image (or multiple images but it should be only one question at a time) and then the teacher clicks on "CHECK".
#! The teacher sees the rating and the reason for the rating.
#! The teacher can do this multiple times by clciking again the "ADD AN IMAGE TO CHECK" button and then clicking on "CHECK" again.
#! The teacher can then click on "ADD TO REPORT" and all checked images will be added to the merged report. The teacher can then download the merged report.

#! OR

#! The teacher clicks on the script checker
#! The teacher can click on new project (and name it to the SUBJECT NAME)
#! Teacher has to upload a pdf of question ppr for that project and we will extract the questions and their marks and store them for that project.
#! Inside the project, the teacher sees a dashboard with a excel like interface, one column containing question name, another column containing the student roll no, and another column containing the uploaded image option containing the student's answer. The teacher then clicks on "CHECK" and then a third column will be populated containing the rating and reason for that image. 
#! The teacher can click on "ADD ANOTHER QUESTION" and then the teacher can upload another image and then click on "CHECK" and then the rating and reason will be populated in the third column.
#! At the end, once the teacher has done uploading all answer images of that subject for all students, they can click "REPORT GENERATE", and then we will create a report for every student roll no. This will work by looking at the student's roll no column and then creating a report for every student roll no. The teacher can then download the report for every student roll no.

from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq

from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain

llm = ChatGroq(temperature=0, model_name="mixtral-8x7b-32768", groq_api_key="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")

template =  """<s>[INST] You are an expert teacher that provides response in JSON format. You are given a question and its answer. You need to do the following things:

    1. You need to rate the relevance of the answer to the question. If the answers satisfies all things asked in the question, you give a good rating.
    If the answer doesnt satisfy the question, or fails to satisfy some part of it, you give a bad rating. 

    2. You also check for any grammatical errors or speeling mistakes as well and
    deduct marks if there are alot of errors present. 

    3. Also, you should make sure that the answers contain detailed explanation if the question requires a detailed answer. If it is mentioned in the question that the answer should be long, then if the answer isn't long, deduct alot of marks for that.

Below is an example JSON output of a good rating:

    ```
    (
        "rating":7,
        "reason":"Answer satisfied all parts of the question, it clearly explained the things asked and gave relevant examples as well, as mentioned in the question",
        "improvement":"Answer could improve further if it was more coherent. Moreover, there were a few grammatical errors present in the text as well"
    )
    ```
You need to follow this JSON format only, DO NOT write anything else other than this format. I repeat, DO NOT OUTPUT ANYTHING ELSE OTHER THAN THE JSON FORMAT. Provide accurate rating, reason, and improvement based on the question and answer provided, in one or two sentences only.

    Below is the question:
    {question}

    Corresponding answer:
    {answer} [/INST] </s>

    JSON response:
"""

def generate_response(question, answer):
  prompt = PromptTemplate(template=template, input_variables=["question","answer"])
  llm_chain = LLMChain(prompt=prompt, llm=llm)
  response = llm_chain.invoke({"question":question, "answer":answer})
  return response

#! Check it out!
# question = "What are the technical and non-technical advantages of E-commerce in detail?"

# answer = """

# Technical advantage are that ecommerce is online, cashless payments etc. Non-technical are that people can buy things from home.
# """
# res = generate_response(question, answer)
# print(res)
















# temp = """

# <s>[INST] You are an expert teacher that provides response in JSON format. You are given a question, an answer, and a reference answer. The reference answer is the correct answer to the question. You need to do the following things:

# 1. You need to rate the relevance of the answer to the question. If the answers satisfies all things asked in the question, you give a good rating. If the answer doesnt satisfy the question, or fails to satisfy some part of it, you give a bad rating.

# 2. You also need to determine if the answer is similar in meaning to the reference answer. If the answer is similar in meaning to the reference answer, you give a good rating. If the answer is not similar in meaning to the reference answer, you give a bad rating.

# 3. Also, you should make sure that the answers contain detailed explanation if the question requires a detailed answer. If it is mentioned in the question that the answer should be long, then if the answer isn't long, deduct alot of marks for that.

# Below is an example JSON output of a good rating:

#     ```(
#         "rating":7,
#         "reason":"Answer satisfied all parts of the question and it is also similar in meaning to the reference answer, it clearly explained the things asked and gave relevant examples as well, as mentioned in the question",
#         "improvement":"Answer could improve further if it was more coherent. Moreover, there were a few grammatical errors present in the text as well"
#     )
#     ```
#     You need to follow this JSON format only, DO NOT write anything else other than this format. I repeat, DO NOT OUTPUT ANYTHING ELSE OTHER THAN THE JSON FORMAT. Provide accurate rating, reason, and improvement based on the question and answer provided, in one or two sentences only.
    
#     Below is the question:
#     {question}

#     Corresponding reference actual answer:
#     {reference_answer} 
    
#     Answer:
#     {answer}[/INST] </s>

#     JSON response:

# """
