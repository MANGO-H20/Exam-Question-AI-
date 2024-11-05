import os
from retrieval import get_query_results
from huggingface_hub import InferenceClient

def query_AI(conditions, docs):

    query = f"""
    Generate the best question on {conditions["message"]} in the 
    subject {conditions["subject"]} at the level of {conditions["level"]}
    of the exam board {conditions["board"]} Ignore this number : 2
    Add the marks to the question in square brackets 
    NO HELP GIVEN ONLY QUESTION 
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
    max_tokens=200
    )
    print(context_string)
    print(output.choices[0].message.content)
conditions = {
    "message" : "Kp",
    "subject": "A-levelChemistry",
    "board": "AQA",
    "level": "A-level"
}
query_AI(conditions,get_query_results(conditions))

