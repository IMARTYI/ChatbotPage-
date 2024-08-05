from flask import Flask, render_template, request, jsonify
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = """
Answer the question below.
    Here is the conversation history: {context}

    Question: {question}

    Answer:
"""

model = OllamaLLM(model ="llama3")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model


app = Flask(__name__)

def userCreate():
    name = input("Whats is your Name ?")
@app.route('/chat')

def handle_conversation():
    context = ""
    print("welcome to Martybot! Type !quit to leave the chat")
    while True:
        userVal = input(f"")
        if userVal =="!quit":
            break
        result = model.invoke(userVal)

        print("MartyBot:",result)
        context = f"\n User: {userVal} \n AI: {result}"
       

# Function to send Chatbot response to client
def response():
    pass

@app.route('/')
def home():
    return render_template('./index.html')

if __name__ == '__main__':
    app.run(debug=True)
    userCreate()
    handle_conversation()