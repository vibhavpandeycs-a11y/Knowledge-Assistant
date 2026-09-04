import tkinter as tk
from tkinter import ttk, scrolledtext, filedialog
import shutil
import os
from local_llm_agent import PDFChatAssistant, NormalChatAssistant

class MainInterface(tk.Frame):
    def __init__(self, window, pdf_screen, normal_screen):
        super().__init__(window)
        self.pdf_screen = pdf_screen
        self.normal_screen = normal_screen
        self.main_bg= tk.PhotoImage(file="main_interface.png")
        self.enter_button_logo = tk.PhotoImage(file="enter_button.png")
        self.exit_button_logo = tk.PhotoImage(file="exit_button.png")

        self.main_bg_label = tk.Label(self, image=self.main_bg)
        self.pdf_chat_enter_button = tk.Button(self, image=self.enter_button_logo, command=self.pdf_chat)
        self.normal_chat_enter_button = tk.Button(self, image=self.enter_button_logo, command=self.normal_chat)
        self.exit_button = tk.Button(self, image=self.exit_button_logo ,command= self.exit_screen)

        self.main_bg_label.pack()
        self.pdf_chat_enter_button.place(x=687, y=613, width=50, height=49)
        self.normal_chat_enter_button.place(x= 1200, y=613, width=50, height=49)
        self.exit_button.place(x=10, y=10, width=50, height=49)

    def pdf_chat(self):
        self.pack_forget()
        self.pdf_screen.pack()

    def normal_chat(self):
        self.pack_forget()
        self.normal_screen.pack()

    def exit_screen(self):
        window.destroy()

class ChatbotInterface(tk.Frame):
    def __init__(self, window):
        super().__init__(window)
        self.chatbot_bg = tk.PhotoImage(file="chatbot_background.png")
        self.enter_button_logo = tk.PhotoImage(file="enter_button.png")
        self.back_button_logo = tk.PhotoImage(file="back_button.png")

        self.chatbot_bg_label = tk.Label(self, image=self.chatbot_bg)
        self.style = ttk.Style()
        self.question_entry = ttk.Entry(self, font=("Lexend",10,"bold"))
        self.style.theme_use('clam')
        self.style.configure('TEntry', padding=6, relief="flat", fieldbackground="#f0f0f0")
        self.enter_button = tk.Button(self, image=self.enter_button_logo, command= self.save_question)
        self.back_button = tk.Button(self, image=self.back_button_logo ,command= self.back_to_main)
        self.file_name = None

        self.chatbot_bg_label.pack()
        self.question_entry.place(x=940, y=81, width=380, height=50)
        self.enter_button.place(x=1270, y=82, width=50, height=49)
        self.back_button.place(x=10, y=10, width=50, height= 49)
        self.question_entry.bind("<Return>", lambda press_key: self.enter_button.invoke())

    def pdf_select(self):
        if self.file_name is not None:
            return self.file_name
        try:
            file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
        except Exception:
            return 
        shutil.copy2(file_path, "E:\\AI-Powered local knowledge assistant/")
        self.file_name = os.path.basename(file_path)

    def save_question(self):
        self.user_query = self.question_entry.get()
        self.question_entry.delete(0, tk.END)
        self.load_response(self.user_query)

    def back_to_main(self):
        self.pack_forget()
        main_screen.pack()

class WithPDFScreen(ChatbotInterface):

    def __init__(self, window):
        super().__init__(window)
        self.pdf_input_logo = tk.PhotoImage(file="pdf_input_logo.png")
        self.pdf_input_button = tk.Button(self, image=self.pdf_input_logo, command=self.pdf_select)

        self.pdf_input_button.place(x=580, y=81, width=50, height=49)

    def load_response(self, user_query):
        file_name = self.file_name

        if file_name == None:
            new_text = "Select a pdf document to continue."
        else:
            chatbot_response = PDFChatAssistant(user_query, file_name)
            response = chatbot_response.pdf_llm_response()
            new_text = f"{user_query}\n\n{response}"

        text_area = scrolledtext.ScrolledText(self, wrap= tk.WORD, font=("Lexend",10,"bold"))
        text_area.place(x=745, y=250, width=535, height=470)
        text_area.delete("1.0", tk.END)
        text_area.insert("1.0", new_text)

class WithoutPDFScreen(ChatbotInterface):

    def __init__(self, window):
        super().__init__(window)

    def load_response(self, user_query):
        chatbot_response = NormalChatAssistant(user_query)
        response = chatbot_response.normal_llm_response()

        new_text = f"{user_query}\n\n{response}"
        text_area = scrolledtext.ScrolledText(self, wrap= tk.WORD, font=("Lexend",10,"bold"))
        text_area.place(x=745, y=250, width=535, height=470)
        text_area.delete("1.0", tk.END)
        text_area.insert("1.0", new_text)

window = tk.Tk()
window.title("Knowledge Assistant")
icon = tk.PhotoImage(file="chatbot_logo.png")
window.iconphoto(True, icon)

pdf_screen = WithPDFScreen(window)
normal_screen = WithoutPDFScreen(window)
main_screen = MainInterface(window, pdf_screen, normal_screen)

main_screen.pack()

pdf_screen.pack_forget()
normal_screen.pack_forget()

window.mainloop()