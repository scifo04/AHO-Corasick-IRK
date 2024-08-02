import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from AHOCorasick import AHOCorasick
from PIL import Image, ImageTk
from typing import List
from Canvas import LeGraph
from tkinter import PhotoImage
import os

class MainPage:
    root: tk.Tk
    file_frm: ttk.LabelFrame
    output_frm: ttk.LabelFrame
    button_frm: ttk.Frame
    upload_button: ttk.Button
    solve_button: ttk.Button
    visualize_button: ttk.Button
    file_path: str
    file_name: str
    file_label: ttk.Label
    bg_label: ttk.Label
    bg_image: PhotoImage
    upload_image: ImageTk.PhotoImage
    solve_image: ImageTk.PhotoImage
    visualize_image: ImageTk.PhotoImage
    text_output: tk.Text
    solution_pack: AHOCorasick
    output_content: List[str]
    to_graph: List[str]

    def __init__ (self):
        self.root = tk.Tk()
        self.root.title("AHO-Corasick String Matcher")
        self.root.geometry("825x775")
        self.file_path = ""
        self.file_name = "File: "
        self.create_background()
        self.construct_file_frm()
        self.construct_upload_button()
        self.construct_chosen_file()
        self.construct_button_frm()
        self.construct_solve_button()
        self.construct_visualize_button()
        self.visualize_button.config(state=tk.DISABLED)
        self.construct_output_frm()
        self.construct_text_output()
        self.output_content = []
        self.root.mainloop()

    def create_background(self):
        self.bg_image = PhotoImage(file='../img/bg.png')
        self.bg_label = tk.Label(self.root, image=self.bg_image)
        self.bg_label.place(relheight=1,relwidth=1)

    def construct_file_frm(self):
        self.file_frm = ttk.LabelFrame(self.root, padding=10, text="Upload JSON Here")
        self.file_frm.grid(row=0, column=0, padx=0, pady=20, ipadx=200, ipady=10)

    def construct_output_frm(self):
        self.output_frm = ttk.LabelFrame(self.root, padding=10, text="Output")
        self.output_frm.grid(row=2, column=0, padx=20, pady=20, ipadx=50)

    def construct_upload_button(self):
        upload_image = Image.open('../img/upload.png')
        upload_image = upload_image.resize((50,50))
        self.upload_image = ImageTk.PhotoImage(upload_image)
        self.upload_button = tk.Button(self.file_frm, text="Choose File", command=self.process_file, image=self.upload_image, borderwidth=0)
        self.upload_button.grid(row=0, column=0, pady=20)

    def construct_chosen_file(self):
        self.file_label = ttk.Label(self.file_frm, text=self.file_name)
        self.file_label.grid(row=0, column=1, padx=10, pady=0)

    def construct_button_frm(self):
        self.button_frm = ttk.Frame(self.root)
        self.button_frm.grid(row=1, column=0, pady=20)

    def construct_solve_button(self):
        solve_image = Image.open('../img/solve.png')
        solve_image = solve_image.resize((125,50))
        self.solve_image = ImageTk.PhotoImage(solve_image)
        self.solve_button = tk.Button(self.button_frm, text="Solve", command=self.solve_file,image=self.solve_image,borderwidth=0)
        self.solve_button.pack(side="left", padx=5, pady=20)

    def construct_visualize_button(self):
        visualize_image = Image.open('../img/visu.png')
        visualize_image = visualize_image.resize((125,50))
        self.visualize_image = ImageTk.PhotoImage(visualize_image)
        self.visualize_button = tk.Button(self.button_frm, text="Visualize", command=self.visualize_file,image=self.visualize_image,borderwidth=0)
        self.visualize_button.pack(side="left", padx=5, pady=20)

    def construct_text_output(self):
        self.text_output = tk.Text(self.output_frm, wrap="word")
        self.text_output.pack(padx=10, pady=10)
        self.text_output.config(state=tk.DISABLED)

    def process_file(self):
        filename = filedialog.askopenfilename(
            title="Choose a JSON file",
            filetypes=[("JSON files","*.json")]
        )
        self.file_path = filename
        self.file_name = "File: " + os.path.basename(filename)
        self.construct_chosen_file()

    def solve_file(self):
        self.output_content = []
        if self.file_path != "":
            self.solution_pack = AHOCorasick(self.file_path)
        for i in self.solution_pack.hashmap:
            self.output_content.append(f'Pattern "{i}" found {len(self.solution_pack.hashmap[i])}x at indexes {self.solution_pack.hashmap[i]}\n')
        self.text_output.config(state=tk.NORMAL)
        self.text_output.delete("1.0", tk.END)
        for i in self.output_content:
            self.text_output.insert(tk.END, i)
        self.text_output.config(state=tk.DISABLED)
        self.visualize_button.config(state=tk.NORMAL)

    def visualize_file(self):
        LeGraph(self.solution_pack.to_graph)

