import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter.ttk import Progressbar, Style
from tkinter.font import Font
from concurrent.futures import ThreadPoolExecutor, as_completed
import time
import os

class FileConverterApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("File Converter")
        self.geometry("600x400")
        self.configure(bg="#2b2b2b")
        self.executor = ThreadPoolExecutor(max_workers=5)
        self.file_list = []
        self.futures = []
        self.cancelled = False
        
        self.title_font = Font(family="Helvetica", size=18, weight="bold")
        self.button_font = Font(family="Helvetica", size=12)
        
        self.style = Style()
        self.style.configure("TButton", font=self.button_font, padding=6, background="#4CAF50", foreground="white")
        self.style.configure("TProgressbar", thickness=30, troughcolor="#5a5a5a", background="#4CAF50")

        self.create_widgets()

    def create_widgets(self):
        title_label = tk.Label(self, text="File Converter", font=self.title_font, fg="white", bg="#2b2b2b")
        title_label.grid(row=0, column=0, columnspan=3, pady=20, padx=20)

        self.select_files_btn = tk.Button(self, text="Select Files", command=self.select_files, bg="cyan", fg="white", font=self.button_font)
        self.select_files_btn.grid(row=1, column=0, padx=20, pady=10, sticky="ew")

        self.format_var = tk.StringVar(value="PDF to DOCX")
        self.format_option = tk.OptionMenu(self, self.format_var, "PDF to DOCX", "Image Resize", "Other")
        self.format_option.config(bg="cyan", fg="white", font=self.button_font)
        self.format_option.grid(row=1, column=1, padx=20, pady=10, sticky="ew")

        self.start_btn = tk.Button(self, text="Start Conversion", command=self.start_conversion, bg="cyan", fg="white", font=self.button_font)
        self.start_btn.grid(row=1, column=2, padx=20, pady=10, sticky="ew")

        self.progress_bar = Progressbar(self, length=500, mode="determinate", style="TProgressbar")
        self.progress_bar.grid(row=2, column=0, columnspan=3, padx=20, pady=20, sticky="ew")

        self.cancel_btn = tk.Button(self, text="Cancel", command=self.cancel_conversion, bg="#f44336", fg="white", font=self.button_font, state=tk.DISABLED)
        self.cancel_btn.grid(row=3, column=0, columnspan=3, padx=20, pady=10, sticky="ew")

        self.status_label = tk.Label(self, text="No files selected", font=self.button_font, fg="white", bg="#2b2b2b")
        self.status_label.grid(row=4, column=0, columnspan=3, padx=20, pady=10)

    def select_files(self):
        files = filedialog.askopenfilenames()
        self.file_list = list(files)

        if self.file_list:
            self.status_label.config(text=f"{len(self.file_list)} files selected")

    def start_conversion(self):
        if not self.file_list:
            messagebox.showwarning("No Files", "Please select files to convert!")
            return

        self.start_btn.config(state=tk.DISABLED)
        self.cancel_btn.config(state=tk.NORMAL)
        self.cancelled = False
        self.progress_bar["value"] = 0
        self.progress_bar["maximum"] = len(self.file_list)
        self.futures = []
        for file in self.file_list:
            future = self.executor.submit(self.convert_file, file)
            self.futures.append(future)
        self.check_progress()

    def check_progress(self):
        completed = 0
        for future in as_completed(self.futures):
            if future.done():
                completed += 1
                self.progress_bar["value"] = completed

        if completed < len(self.file_list) and not self.cancelled:
            self.after(100, self.check_progress)

        if completed == len(self.file_list):
            self.status_label.config(text="Conversion complete!")
            self.reset_buttons()

    def convert_file(self, file):
        if self.cancelled:
            return

        file_name = os.path.basename(file)
        self.status_label.config(text=f"Converting {file_name} to {self.format_var.get()}")
        time.sleep(2)

    def cancel_conversion(self):
        self.cancelled = True
        for future in self.futures:
            future.cancel()
        self.status_label.config(text="Conversion cancelled")
        self.reset_buttons()

    def reset_buttons(self):
        self.start_btn.config(state=tk.NORMAL)
        self.cancel_btn.config(state=tk.DISABLED)
        self.progress_bar["value"] = 0

if __name__ == "__main__":
    app = FileConverterApp()
    app.mainloop()
