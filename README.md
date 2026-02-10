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
```
### Setup
Clone or download the project:
```bash
git clone <your-repository-url>
cd document-processor
```
2) The required folder structure will be automatically created on first run.

### Usage
1) Place your documents in the input_documents/ folder

Supported formats: .pdf, .docx, .txt, .xlsx

2) Run the main program:
```bash
python main.py
```
3)Check the results in the output/ folder:

summaries/: First 60 words of each document

categories/: Classification result for each document

reports/: Detailed PDF reports with analysis

4)View logs in logs/system.log for processing history

### Document Classification Categories
The system classifies documents into these categories based on keywords:

HR: Contains words like "employee", "salary", "leave", "recruitment"

Finance: Contains words like "invoice", "payment", "tax", "budget"

Operations: Contains words like "process", "workflow", "logistics"

Legal: Contains words like "agreement", "contract", "law", "compliance"

Unknown: If no keywords match

### Sample Report Content
Each generated PDF report includes:

File Name

Category Classification

Word Count

Character Count

Dates Found (DD/MM/YYYY format)

Amounts Found (numeric values with optional ₹ symbol)

Summary (first 60 words)

### Customization
## Adding New Categories
Edit utils/classifier.py to modify or add categories:

```bash
categories = {
    "HR": ["employee", "salary", "leave", "recruitment"],
    "Finance": ["invoice", "payment", "tax", "budget"],
    "Operations": ["process", "workflow", "logistics"],
    "Legal": ["agreement", "contract", "law", "compliance"],
    # Add your custom category here
    "IT": ["server", "network", "software", "hardware"]
}
```
### Error Handling
The system includes comprehensive error handling:

Empty input folder detection

File reading errors

Text extraction failures

Detailed logging of all errors

### Limitations
Currently supports only English text

Classification is keyword-based (not ML/AI)

PDF text extraction depends on PDF structure

Excel files read cell values only (no formulas)

### Future Enhancements
Potential improvements:

Machine learning-based classification

Support for more file formats

Advanced NLP for better summarization

GUI interface

Database integration for storing results

Email notification system

### Contributing
Fork the repository

Create a feature branch

Commit your changes

Push to the branch

Create a Pull Request

### License
This project is licensed under the MIT License - see the LICENSE file for details.

### Support
For issues or questions:

Check the logs/system.log for error details

Ensure all dependencies are installed

Verify file formats are supported

Create an issue in the GitHub repository


