
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