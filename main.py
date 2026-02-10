import os
import re
from datetime import datetime

from utils.file_reader import read_file
from utils.classifier import classify_document
from utils.report_generator import generate_pdf
from utils.logger import log_event

# =========================
# BASE DIRECTORY (IMPORTANT)
# =========================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

INPUT_DIR = os.path.join(BASE_DIR, "input_documents")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")

SUMMARY_DIR = os.path.join(OUTPUT_DIR, "summaries")
CATEGORY_DIR = os.path.join(OUTPUT_DIR, "categories")
REPORT_DIR = os.path.join(OUTPUT_DIR, "reports")

# =========================
# CREATE FOLDERS IF NOT EXIST
# =========================
os.makedirs(INPUT_DIR, exist_ok=True)
os.makedirs(SUMMARY_DIR, exist_ok=True)
os.makedirs(CATEGORY_DIR, exist_ok=True)
os.makedirs(REPORT_DIR, exist_ok=True)

print("Program started...")
print("Checking input_documents folder...")

# =========================
# CHECK IF INPUT FOLDER EMPTY
# =========================
files = os.listdir(INPUT_DIR)

if not files:
    print("❌ No files found in input_documents folder.")
    print("👉 Please add at least one .txt / .pdf / .docx / .xlsx file.")
else:
    for file in files:
        print("Found file:", file)

        try:
            file_path = os.path.join(INPUT_DIR, file)

            # Read file
            text = read_file(file_path)

            if not text.strip():
                print("⚠ No text extracted from:", file)
                continue

            # Classify
            category = classify_document(text)

            # Analysis
            words = text.split()
            word_count = len(words)
            char_count = len(text)

            dates = re.findall(r"\d{2}/\d{2}/\d{4}", text)
            amounts = re.findall(r"\₹?\d+", text)

            summary = " ".join(words[:60])

            # =========================
            # WRITE SUMMARY FILE
            # =========================
            summary_file = os.path.join(SUMMARY_DIR, f"{file}.txt")
            with open(summary_file, "w", encoding="utf-8") as f:
                f.write(summary)

            # =========================
            # WRITE CATEGORY FILE
            # =========================
            category_file = os.path.join(CATEGORY_DIR, f"{file}.txt")
            with open(category_file, "w", encoding="utf-8") as f:
                f.write(category)

            # =========================
            # GENERATE PDF REPORT
            # =========================
            report_data = {
                "File Name": file,
                "Category": category,
                "Word Count": word_count,
                "Character Count": char_count,
                "Dates Found": ", ".join(dates) if dates else "None",
                "Amounts Found": ", ".join(amounts) if amounts else "None",
                "Summary": summary
            }

            generate_pdf(file, report_data)

            print(f"✅ Processed successfully: {file}")
            log_event(f"{file} | Category: {category}")

        except Exception as e:
            print("❌ ERROR processing:", file)
            print(e)
            log_event(f"ERROR processing {file}: {str(e)}")

print("Program finished.")
