from PyPDF2 import PdfFileMerger

pdfs = ['G:/MergePDF/Баулина.pdf', 'G:/MergePDF/Клюев.pdf']
merger = PdfFileMerger()


def merge(pdf_files):
    try:
        print(pdf_files)
        for pdf in pdf_files:
            print(pdf)
            merger.append(pdf)

        merger.write("result.pdf")
        merger.close()
    except Exception as exc:
        print(exc)


if __name__ == '__main__':
    merge(pdfs)
