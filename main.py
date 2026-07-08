from downloader import download_pdf

url = "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf"

pdf_path = download_pdf(url)

print(f"PDF downloaded successfully: {pdf_path}")


