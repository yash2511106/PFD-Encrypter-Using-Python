from PyPDF2 import PdfReader, PdfWriter

# Open the current PDF
with open('File_path', 'rb') as file:
    reader = PdfReader(file)
    
    # Object for PDF writer
    writer = PdfWriter()

   

    # Add each page to the writer
    for page in reader.pages:
        writer.add_page(page)

# Password to encrypt the PDF
password = "Password"

# Encrypt the PDF with the password
writer.encrypt(password)

# Write the encrypted PDF to a new file
with open("encryptedfile.pdf", "wb") as filename:
    writer.write(filename)

print("PDF has been encrypted and saved as 'encryptedfile.pdf'")
