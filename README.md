# PDF to Word Converter (Offline)

Hey there! 👋
This is a simple offline PDF to Word converter built in Python. It comes with a friendly GUI so you can easily turn any PDF into an editable Word document without needing an internet connection.

Think of it as your little assistant for quickly editing PDFs!

## Features

- Convert PDFs into Word (.docx) in a few clicks
- Pick where to save your Word files
- Simple GUI: Browse → Convert → Done!
- After conversion, choose to convert more PDFs or exit

## What You Need

# Before you get started, make sure you have:
- Python 3.8+ installed
- The library pdf2docx (pip install pdf2docx)
- Tkinter (comes with Python by default)
- Optional: PyInstaller if you want a standalone app

## How to Get It Running (Step by Step)

# 1. Clone the repository (or download it as ZIP):
```
git clone https://github.com/sharan-johijode-dotcom/PDF-to-Word-Converter.git
cd pdf-to-word-converter
```

# 2. Install the required library:
```
pip install pdf2docx
```

# 3. Run the app:
```
python pdf_to_word_gui_v2.py
```

# 4. Use it:

- Click “Select PDF & Convert”
- Pick your PDF
- Choose where to save the Word file
- Wait a few seconds for the conversion
- A popup will ask: “Convert another file?”
    - Yes → pick another PDF
    - No → app closes

And that’s it! 🎉

## Make It a Standalone App (Optional)

Want to give it to friends or colleagues without them needing Python? You can make a single executable file:

# 1. Install PyInstaller:
```
pip install pyinstaller
```

# 2. Run this command :
```
Windows    -> pyinstaller --onefile --windowed --icon=icon.ico pdf_to_word_gui_v2.py
Mac        -> pyinstaller --onefile --windowed main.py
Linux/unix -> pyinstaller --onefile main.py
```

# 3. Find your app in the dist/ folder:
```
dist/pdf_to_word_gui_v2(.exe/.app/.deb)
```
Double-click it and it runs just like a normal app (Windows).


## Things to Keep in Mind

Works best with text-based PDFs. Scanned PDFs aren’t supported yet.
Layout may not always be perfect, especially with complex tables or multi-column PDFs.
Right now, you can only convert one file at a time.
Fully offline — no internet required.
