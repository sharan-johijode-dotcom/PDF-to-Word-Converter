import tkinter as tk
from tkinter import filedialog, messagebox
from pdf2docx import Converter
import os

def convert_pdf_to_word():
    while True:
        # Ask user to select a PDF file
        pdf_file = filedialog.askopenfilename(
            title="Select PDF file to convert",
            filetypes=[("PDF Files", "*.pdf")]
        )
        if not pdf_file:
            break  # user canceled

        # Ask user where to save the Word file
        save_file = filedialog.asksaveasfilename(
            title="Save Word file as",
            defaultextension=".docx",
            filetypes=[("Word Documents", "*.docx")]
        )
        if not save_file:
            break  # user canceled

        try:
            # Convert PDF to Word
            cv = Converter(pdf_file)
            cv.convert(save_file, start=0, end=None)
            cv.close()
            messagebox.showinfo("Success", f"PDF successfully converted to:\n{save_file}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to convert PDF:\n{str(e)}")

        # Ask user if they want to convert another PDF
        again = messagebox.askyesno("Convert Again?", "Do you want to convert another PDF?")
        if not again:
            break

if __name__ == "__main__":
    # Initialize Tkinter root (hide main window)
    root = tk.Tk()
    root.withdraw()  # Hide main window
    convert_pdf_to_word()
