from pypdf import PdfReader

class PdfService:

    def load_text(self, file_path: str) -> str:
        reader = PdfReader(file_path)

        text = ""

        for page in reader.pages:
            text += page.extract_text() + "\n"

        return text