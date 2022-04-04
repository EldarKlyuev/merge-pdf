from PyPDF2 import PdfFileMerger

pdfs = ['Баулина.pdf', 'Клюев.pdf', 'Сандаков.pdf']
merger = PdfFileMerger()


def merge(pdf_files):
    for pdf in pdf_files:
        merger.append(pdf)

    merger.write("result.pdf")
    merger.close()


if __name__ == '__main__':
    merge(pdfs)
