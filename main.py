from PyPDF2 import PdfFileMerger

pdfs = ['G:/MergePDF/Баулина.pdf', 'G:/MergePDF/Клюев.pdf']
merger = PdfFileMerger()


def merge(pdf_files):
    print(pdf_files)
    for pdf in pdf_files:
        merger.append(pdf)

    merger.write("result.pdf")
    merger.close()


if __name__ == '__main__':
    merge(pdfs)
