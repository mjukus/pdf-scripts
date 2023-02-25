from pypdf import PdfWriter, PdfReader
from typing import Union, Literal, List
import sys


def pdf_combiner(*args):
    merger = PdfWriter()
    for pdf in input_pdfs:
        merger.append(pdf)
    merger.write("merged_pdf.pdf")
    merger.close()

def watermarker(
        content_pdf,
        stamp_pdf,
        page_indices: Union[Literal["ALL"], List[int]] = "ALL",
):
    reader = PdfReader(content_pdf)
    if page_indices == "ALL":
        page_indices = list(range(0, len(reader.pages)))
    
    writer = PdfWriter()
    for index in page_indices:
        content_page = reader.pages[index]
        mediabox = content_page.mediabox

        reader_stamp = PdfReader(stamp_pdf)
        image_page = reader_stamp.pages[0]

        image_page.merge_page(content_page)
        image_page.mediabox = mediabox
        writer.add_page(image_page)
    
    with open("watermarked_pdf.pdf", "wb") as file:
        writer.write(file)


content_pdf = sys.argv[1]
stamp_pdf = sys.argv[2]
watermarker(content_pdf, stamp_pdf, "ALL")