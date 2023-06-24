# gradio 
import openai
import gradio as gr 
openai.api_key = "" # replace with your api key
prompt = "You're a virtual assistant that offers short and concise answers"

def openai_chat(prompt):
    completion = openai.Completion.create(
        model = 'text-davinci-003',
        prompt = prompt,
        temperature = 0.9,
        max_tokens =150,
        top_p=1,
        frequency_penalty = 0,
        presence_penalty = 0.6,
    )
    return completion.choices[0].text



with gr.Blocks() as Demo:
    state = gr.State()
    gr.Markdown("""<h1> My Virtual Assistant Created by Dhiraj Python Developer </h1>""")
    msg = gr.Textbox(placeholder= "What do you have in mind?")
    chatbot = gr.Chatbot()
    
    ints = [msg,state]
    outs = [chatbot,state]

    def Respond_Chat(input,chat_history):
        chat_history = chat_history or []
        sum_chat_history = list(sum(chat_history,()))
        sum_chat_history.append(input)
        sum_chat_history_inp = ' '.join(sum_chat_history)
        output = openai_chat(sum_chat_history_inp)
        chat_history.append((input,output))
        return chat_history,chat_history

    msg.submit(Respond_Chat,inputs=ints,outputs=outs)

Demo.launch(debug=True)