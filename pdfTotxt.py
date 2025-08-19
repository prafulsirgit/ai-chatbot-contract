import fitz  # PyMuPDF
import os

def load_processed_files(log_file_path):
    """Load the list of processed files from the log file."""
    if not os.path.exists(log_file_path):
        return set()
    with open(log_file_path, "r", encoding="utf-8") as f:
        return set(line.strip() for line in f.readlines())

def log_processed_file(log_file_path, filename):
    """Append a processed file name to the log."""
    with open(log_file_path, "a", encoding="utf-8") as f:
        f.write(filename + "\n")

def pdf_to_text(pdf_path, output_folder):
    """Extract text from a PDF and save to a .txt file in output folder."""
    base_name = os.path.splitext(os.path.basename(pdf_path))[0]
    txt_file_name = base_name + ".txt"
    txt_file_path = os.path.join(output_folder, txt_file_name)

    doc = fitz.open(pdf_path)
    full_text = ""
    for page in doc:
        full_text += page.get_text()

    os.makedirs(output_folder, exist_ok=True)

    with open(txt_file_path, "w", encoding="utf-8") as txt_file:
        txt_file.write(full_text)

    print(f"✅ Extracted text saved to '{txt_file_path}'")

def extract_new_pdfs(source_folder, output_folder, log_file_path):
    processed_files = load_processed_files(log_file_path)

    for filename in os.listdir(source_folder):
        if filename.lower().endswith(".pdf") and filename not in processed_files:
            pdf_path = os.path.join(source_folder, filename)
            try:
                pdf_to_text(pdf_path, output_folder)
                log_processed_file(log_file_path, filename)
            except Exception as e:
                print(f"❌ Failed to process '{filename}': {e}")

# 🔧 Configuration
source_folder = r"C:\Users\Asus\Downloads\methi2\project\data"
output_folder = r"C:\Users\Asus\Downloads\methi2\project\data\knowledge_base"
log_file_path = os.path.join(output_folder, "processed_files.log")

# 🚀 Run the script
extract_new_pdfs(source_folder, output_folder, log_file_path)
