import tkinter as tk
from tkinter import ttk
# from tkinter import messagebox
from tkinter import filedialog
from AHOCorasick import AHOCorasick
from typing import List
import os

class MainPage:
    root: tk.Tk
    file_frm: ttk.LabelFrame
    output_frm = ttk.LabelFrame
    upload_button: ttk.Button
    solve_button: ttk.Button
    file_path: str
    file_name: str
    file_label: ttk.Label
    text_output: tk.Text
    solution_pack = AHOCorasick
    output_content: List[str]

    def __init__ (self):
        self.root = tk.Tk()
        self.root.title("AHO-Corasick String Matcher")
        self.root.geometry("825x675")
        self.file_path = ""
        self.file_name = "File: "
        self.construct_file_frm()
        self.construct_upload_button()
        self.construct_chosen_file()
        self.construct_solve()
        self.construct_output_frm()
        self.construct_text_output()
        self.output_content = []
        self.root.mainloop()

    def construct_file_frm(self):
        self.file_frm = ttk.LabelFrame(self.root, padding=10, text="Upload JSON Here")
        self.file_frm.pack()
        self.file_frm.grid(row=0,column=0,padx=0,pady=20,ipadx=200,ipady=10)

    def construct_output_frm(self):
        self.output_frm = ttk.LabelFrame(self.root, padding=10,text="Output")
        self.output_frm.grid(row=2,column=0,padx=20,pady=20,ipadx=50)

    def construct_upload_button(self):
        self.upload_button = ttk.Button(self.file_frm,text="Choose File",command=self.process_file)
        self.upload_button.grid(row=0,column=0,pady=20)

    def construct_chosen_file(self):
        self.file_label = ttk.Label(self.file_frm, text=self.file_name)
        self.file_label.grid(row=0,column=1,padx=10,pady=0)

    def construct_text_output(self):
        self.text_output = tk.Text(self.output_frm,wrap="word")
        self.text_output.pack(padx=10, pady=10)
        self.text_output.config(state=tk.DISABLED)

    def construct_solve(self):
        self.solve_button = ttk.Button(self.root, padding=10, text="Solve",command=self.solve_file)
        self.solve_button.grid(row=1,column=0,pady=20)

    def process_file(self):
        filename = filedialog.askopenfilename(
            title="Choose a JSON file",
            filetypes=[("JSON files","*.json")]
        )
        self.file_path = filename
        self.file_name = "File: "
        self.file_name += os.path.basename(filename)
        self.construct_chosen_file()

    def solve_file(self):
        if self.file_path != "":
            self.solution_pack = AHOCorasick(self.file_path)
        for i in self.solution_pack.hashmap:
            self.output_content.append(f'Pola "{i}" ditemukan {len(self.solution_pack.hashmap[i])}x, ditemukan pada indeks {self.solution_pack.hashmap[i]}\n')
        self.text_output.config(state=tk.NORMAL)
        for i in self.output_content:
            self.text_output.insert(tk.END,i)
        self.text_output.config(state=tk.DISABLED)