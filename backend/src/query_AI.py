import os
from retrieval import get_query_results
from huggingface_hub import InferenceClient
from langchain_openai import ChatOpenAI

def query_AI(conditions):
    docs = get_query_results(conditions)
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
    token = os.getenv("chatgpt");
    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0,
        max_tokens=500,
        api_key= token

    )
    message = [
        {"role": "user", "content": prompt}
    ]
    output = llm.invoke(message
    )
    #out = output.choices[0].message.content
    return output.content
conditions = {
    "message" : "Rounding",
    "subject": "Maths",
    "board": "AQA",
    "level": "GCSE"
}
print(query_AI(conditions))

