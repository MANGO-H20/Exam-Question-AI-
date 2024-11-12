# Exam-Question-AI-
this a project that uses langchain and mongoDB to host a website that can take input from a user to generate
pratice exam questions alongside with a mark schemce for the user to allow them to pratice their exams skills

Requirements:
You will need python however python 3.13 will not work since it will not allow you to download the correct versions of numpy
for use with langchain (numpy 2.0.0>2.16.4)
You will need to download all the libaries listed in the requirment.txt and to install them you can use pip install -r requirment.txt
you will also need to place your own mongoDB pass and Chatgpt Api key into .env file
the following should be done in order:

1.you will be required to donwload pdfs using either a webscraper or manually and then you will be required to sort the pdfs by subject and 
wether the pdf is a markschemce or an exam paper

2.then you will required to run the create_database.py file this will place all the pdfs into the database to be used as context for chat gpt

3.then you will need to run create-index.py which will for your database collection will create a vector index with a similarity of cosine
with the prefilters of level, subject, markscheme and board of your files and then wait once it has been indexed throughout your database

4.run the life server for the frontend so the website is set up

5.then run app.py and this will run the api and then you can use the website and the function should work
