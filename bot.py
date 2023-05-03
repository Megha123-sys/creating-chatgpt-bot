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

text_frame = customtkinter.CTkFrame(master = app)
text_frame.pack(pady=20)
my_text = Text(text_frame, bg="#343638", width = 75, relief = "flat", wrap=WORD, fg="white")


app.mainloop()
