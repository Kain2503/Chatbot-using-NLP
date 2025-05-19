import nltk
import random
import tkinter as tk
from tkinter import scrolledtext
from nltk.chat.util import Chat, reflections

# Importing the patterns from the patterns.py file
from patterns import patterns_responses

# Initialize the chatbot with patterns and reflections
chatbot = Chat(patterns_responses, reflections)

# Function to handle chat
def chatbot_response(user_input):
    return chatbot.respond(user_input)

# GUI to interact with the chatbot using Tkinter
def run_chatbot_gui():
    window = tk.Tk()
    window.title("chatbot")

    # Creating a scrollable text area to display conversation
    conversation_window = scrolledtext.ScrolledText(window, width=50, height=20, font=("Arial", 12), wrap=tk.WORD)
    conversation_window.grid(row=0, column=0, padx=10, pady=10)
    conversation_window.config(state=tk.DISABLED)  # Make the conversation window read-only

    # Function to process input from user
    def process_input():
        user_input = input_box.get()
        if user_input.lower() == 'quit':
            window.quit()
        conversation_window.config(state=tk.NORMAL)
        conversation_window.insert(tk.END, f"You: {user_input}\n")
        bot_response = chatbot_response(user_input)
        conversation_window.insert(tk.END, f"ChatBot: {bot_response}\n")
        conversation_window.config(state=tk.DISABLED)  # Make the conversation window read-only
        input_box.delete(0, tk.END)

    # Input box for user to type
    input_box = tk.Entry(window, width=50, font=("Arial", 12))
    input_box.grid(row=1, column=0, padx=10, pady=10)

    # Button to send input
    send_button = tk.Button(window, text="Send", width=10, height=2, font=("Arial", 12), command=process_input)
    send_button.grid(row=2, column=0, padx=10, pady=10)

    # Start the GUI loop
    window.mainloop()

# Start the chatbot GUI
if __name__ == "__main__":
    run_chatbot_gui()
s
