from tkinter import *
import customtkinter
import openai
import os
import pickle

app = customtkinter.CTk()
app.title("chatGPT bot")
app.geometry("750x600")
app.iconbitmap("C:/Users/Megha Aggarwal/Downloads/bot/ai_lt.ico")

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

def speak():
    print("speak")
    filename = "api key"
    try:
        if os.path.isfile(filename):
            input_file = open(filename,"rb")
            api_key_value =pickle.load(input_file)
        
            openai.api_key = api_key_value
            openai.Model.list()
           
            response = openai.Completion.create(
               model = "text-davinci-003",
               prompt = chat_entry.get(),
               temperature = 0,
               max_tokens = 4000,
               top_p = 1,
               frequency_penalty = 0.0,
               presence_penalty = 0.0
            )  
            editedresponse = response["choices"][0]["text"].strip
            my_text.insert(END, "\n")
            my_text.insert(END, editedresponse)
           
        else:
            my_text.insert(END, "\n\n No open ai key is found, please a give a valid one \n")
    except Exception as e:
        print("exception") 

def new_func(api_key_value):
    openai.api_key = api_key_value                
def clear():
    print("clear")
    my_text.delete(1.0,END)
    chat_entry.delete(0,END)
def api():
    print("api")
    filename="api key"
    try:
        if os.path.isfile(filename):
            input_file = open(filename,"rb")
            api_key_value = pickle.load(input_file)
            api_entry.insert(END, api_key_value)
            input_file.close()
        else:
            input_file = open(filename, "wb")
            input_file.close()
    except Exception as e:
        print("Exception")
        api_Frame.pack(pady=10)
        app.geometry("750x750")
def save():
    filename = "api key"
    try:
        output_file = open(filename, "wb")
        pickle.dump(api_entry.get(), output_file)
        api_entry.delete(0, END)
    except Exception as e:
        print("Exception")    
    api_Frame.forget()
    app .geometry("750x600")
    print("save")
    
text_frame = customtkinter.CTkFrame(master = app)
text_frame.pack(pady=20)
my_text = Text(text_frame, bg="#343638", width = 75, relief = "flat", wrap=WORD, fg="white")
my_text.grid(row=0, column=0)
text_scrool = customtkinter.CTkScrollbar(text_frame, command=my_text.yview)
text_scrool.grid(row=0, column=1,sticky="ns")
my_text.config(yscrollcommand=text_scrool.set)

chat_entry= customtkinter.CTkEntry(master=app, placeholder_text="please send a message....", width=300, height=50, border_width=1)
chat_entry.pack(pady=20)
button_Frame= customtkinter.CTkFrame(master=app, fg_color="#242424")
button_Frame.pack(pady=20)

#first_button -> submit_button
submit_button = customtkinter.CTkButton(button_Frame, text="Ask to chatGPT",command=speak)
submit_button.grid(row=0, column=0, padx=20)
#second_button -> clear_button
clear_button = customtkinter.CTkButton(button_Frame, text="Clear All", command=clear)
clear_button.grid(row=0, column=1, padx=20)
#third_button -> api_button
api_button = customtkinter.CTkButton(button_Frame, text="change api", command=api)
api_button.grid(row=0, column=2, padx=20)
api_Frame= customtkinter.CTkFrame(master=app, border_width=1)

api_entry= customtkinter.CTkEntry(master=api_Frame, placeholder_text="Enter your API key", width=350, height= 50, border_width= 1)
api_entry.grid(row=0, column=0, padx=20, pady=20)
api_save_button= customtkinter.CTkButton(master=api_Frame, text="save", command=save)
api_save_button.grid(row=0, column=1, padx=20)

app.mainloop()
