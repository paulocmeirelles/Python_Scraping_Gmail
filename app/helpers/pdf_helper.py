from PyPDF2 import PdfFileReader, PdfReader
import fitz

class Extract_PDF():
  @staticmethod
  def decrypt_pdf(input_path, password=''):
    try:
      with open(input_path, 'rb') as input_file:

        try:
          reader = PdfReader(input_file)
        except:
          reader = PdfFileReader(input_file)
          reader.decrypt(password)

        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"

        return text

    except Exception as ex:
      print(ex)

  @staticmethod
  def read_pdf(input_path,password=''):
    try:
      with fitz.open(input_path) as doc:
        try:
          doc.authenticate(password)
        except:
          pass
        text = ""
        for page in doc:
          text += page.get_text()

      return text

    except Exception as ex:
      print(ex)