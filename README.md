# pdf-Reader
# Document Classification & Processing System

A Python-based system that automatically reads, classifies, and analyzes various document formats (PDF, DOCX, TXT, XLSX) into predefined categories (HR, Finance, Operations, Legal).

## Features

- **Multi-format Support**: Processes PDF, DOCX, TXT, and XLSX files
- **Automatic Classification**: Categorizes documents based on keyword detection
- **Text Analysis**: Extracts word count, character count, dates, and amounts
- **Report Generation**: Creates detailed PDF reports for each processed document
- **Logging**: Maintains system logs for tracking processed files
- **Batch Processing**: Automatically processes all files in input folder

## Project Structure
document-processor/
├── main.py
├── utils/
│ ├── file_reader.py 
│ ├── classifier.py 
│ ├── report_generator.py
│ └── logger.py 
├── input_documents/ 
├── output/
│ ├── summaries/ 
│ ├── categories/
│ └── reports/ 
└── logs/ 



## Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)
### Dependencies

Install required packages:

```bash
pip install pdfplumber python-docx openpyxl reportlab

### setup

Clone or download the project:
```bash
git clone <your-repository-url>
cd document-processor
