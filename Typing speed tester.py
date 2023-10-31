import tkinter as tk
import random
import time
# Create the main application window
root = tk.Tk()
root.title("Typing Speed Tester")

# Create a text box
text_box = tk.Text(root, height=10, width=40)
text_box.pack()

# Create a label for displaying the generated text
text_label = tk.Label(root, text="")
text_label.pack()

# Function to generate random text for typing
def generate_random_text():
    # Add your list of random texts here
    random_texts = ["This is a typing speed test.", "OpenAI is amazing!", "Python programming is fun."]
    text_label.config(text=random.choice(random_texts))
    text_box.delete("1.0", tk.END)  # Clear the text box

# Create a "Start" button to generate text
start_button = tk.Button(root, text="Start", command=generate_random_text)
start_button.pack()

# Function to calculate typing speed
def calculate_speed():
    text = text_label.cget("text")
    user_input = text_box.get("1.0", "end-1c")  # Get user input
    words = text.split()
    user_words = user_input.split()
    correct_words = sum(1 for w1, w2 in zip(words, user_words) if w1 == w2)
    wpm = int((correct_words / len(words)) * 60)  # Calculate words per minute
    result_label.config(text=f"Your typing speed: {wpm} WPM")

# Create a "Submit" button to calculate typing speed
submit_button = tk.Button(root, text="Submit", command=calculate_speed)
submit_button.pack()

# Create a label to display typing speed result
result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
