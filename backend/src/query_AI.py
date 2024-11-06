import os
from retrieval import get_query_results
from huggingface_hub import InferenceClient

def query_AI(conditions, docs):

    query = f"""
    Generate the best question on {conditions["message"]} in the 
    subject {conditions["subject"]} at the level of {conditions["level"]}
    of the exam board {conditions["board"]} Ignore this number : 58
    Add the marks to the question in square brackets and give us an answer in a markscheme for the question 
    NO HELP GIVEN ONLY QUESTION 
    HARSH MARKING 
    """ 
    context_string = " ".join([doc["text"] for doc in docs])
    print(context_string)
    prompt = f"""Use the following pieces of context to answer the question at the end.
    {context_string}
    Question: {query}
    """
    llm = InferenceClient(
    "mistralai/Mistral-7B-Instruct-v0.3",
    token = os.getenv("huggingFace"))

    output = llm.chat_completion(
    messages=[{"role": "user", "content": prompt}],
    max_tokens=500
    )
    print(context_string)
    print(output.choices[0].message.content)
conditions = {
    "message" : "Rounding",
    "subject": "Maths",
    "board": "AQA",
    "level": "GCSE"
}
query_AI(conditions,get_query_results(conditions))

