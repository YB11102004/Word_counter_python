from tkinter import *
from tkinter import messagebox
import fitz

# word counting function
def word_counter(text_content):
    count = 0
    sentences = text_content.split(".")
    for i in sentences:
        words_in_sentence = i.split()
        count += len(words_in_sentence)
    print(count)
    root1.destroy()

# text based or paragraph
def text_based():
    def on_submit():
        text_content = text_area.get("1.0", "end-1c")
        if not text_content.strip():
            messagebox.showwarning("Warning", "Please type something on the text area before submitting.")
        else:
            messagebox.showinfo("Message Box", "Your output is shown in the console.")
            word_counter(text_content)
            root.destroy()
            
    root = Tk()
    text_area = Text(root, height=10, width=50, bg='#000000', fg='#FFFFFF', insertbackground='white', font=("Comic Sans MS", 20), borderwidth=10)
    label = Label(root, text='Enter the text/paragraph: ', font=("Comic Sans MS", 30, "bold"), bg='#000000', fg='#FF8C00')
    label.pack()
    text_area.pack(fill=BOTH, expand=True)
    submit_button = Button(root, text="S U B M I T", command=on_submit, width=10, height=2, bg='#000000', fg="#FF8C00", font=("Comic Sans MS", 14, "bold"), relief=SOLID, justify=CENTER)
    submit_button.pack()
    root.title('The Word Counter')
    root.configure(bg='#000000')
    root.mainloop()

# file based
def file_based():
    def on_submit():
        file_name = e.get()
        if not file_name:
            messagebox.showwarning("Warning", "Please enter the file name.")
        else:
            try:
                with open(file_name, 'r') as file:
                    content = file.read()
                    word_counter(content)
                    messagebox.showinfo("Message Box", "Word count result shown in the console.")
                    root2.destroy()
            except FileNotFoundError:
                messagebox.showerror("Error", "File not found. Please enter a valid file name.")

    root2 = Tk()
    label = Label(root2, text='Enter the file with txt extension: ', font=("Comic Sans MS", 30, "bold"), bg='#000000', fg='#FF8C00')
    label.pack()
    e = Entry(root2)
    e.pack()
    submit_button = Button(root2, text="S U B M I T", command=on_submit, width=10, height=2, bg='#000000', fg="#FF8C00", font=("Comic Sans MS", 14, "bold"), relief=SOLID, justify=CENTER)
    submit_button.pack()
    root2.title('The Word Counter - File Input')
    root2.configure(bg='#000000')
    root2.mainloop()

# pdf file based
def pdf_based():
    def on_submit():
        file_name = e.get()
        if not file_name:
            messagebox.showwarning("Warning", "Please enter the file name.")
        else:
            try:
                doc = fitz.open(file_name)
                text = ""
                for page_num in range(doc.page_count):
                    page = doc.load_page(page_num)
                    text += page.get_text("text")
                word_counter(text)
                messagebox.showinfo("Message Box", "Word count result shown in the console.")
                root3.destroy()
            except Exception as ef:
                messagebox.showerror("Error", f"An error occurred: {str(ef)}")

    root3 = Tk()
    label = Label(root3, text='Enter the PDF file name: ', font=("Comic Sans MS", 30, "bold"), bg='#000000', fg='#FF8C00')
    label.pack()
    e = Entry(root3)
    e.pack()
    submit_button = Button(root3, text="S U B M I T", command=on_submit, width=10, height=2, bg='#000000', fg="#FF8C00", font=("Comic Sans MS", 14, "bold"), relief=SOLID, justify=CENTER)
    submit_button.pack()
    root3.title('The Word Counter - PDF Input')
    root3.configure(bg='#000000')
    root3.mainloop()

# the main Gui window
root1 = Tk()
label1 = Label(root1, text='Select any option whether to count words from file or text/paragraph ', font=("Comic Sans MS", 24, "bold"), bg='#000000', fg='#FF8C00')
label1.pack()
radio_font = ("Comic Sans MS", 18)
radio_bg = '#000000'
radio_fg = '#FF8C00'
selected_radio = IntVar()
radio_options = ["Text/Paragraph", "File","Pdf"]
for i in range(3):
        radio = Radiobutton(root1, text=radio_options[i], variable=selected_radio, value=i+1, font=radio_font, bg=radio_bg,fg=radio_fg)
        radio.pack()

def on_submit1():
    if selected_radio.get() == 0:
        messagebox.showwarning("Warning", "Please select any option.")
    elif selected_radio.get() == 1:
        text_based()
    elif selected_radio.get() == 2:
        file_based()
    elif selected_radio.get()==3:
        pdf_based()
submit_button = Button(root1, text="S U B M I T", command=on_submit1, width=10, height=2, bg='#000000', fg="#FF8C00", font=("Comic Sans MS", 14, "bold"), relief=SOLID, justify=CENTER)
submit_button.pack()
root1.title('The Word Counter')
root1.configure(bg='#000000')
root1.mainloop()