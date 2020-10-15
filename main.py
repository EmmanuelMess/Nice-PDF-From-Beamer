from PyPDF2 import PdfFileWriter, PdfFileReader

if __name__ == '__main__':
    # Read pdf from file
    infile = PdfFileReader('in.pdf')
    # Get total amount of pages
    totpages = infile.getNumPages()
    # Get starting page number from each page
    pdfpagenuminfo = infile.trailer["/Root"]["/PageLabels"]["/Nums"]
    pdfpagenumaliases = pdfpagenuminfo[0::2]
    # Shift page number of interest to get only the page of the last overlay for each frame
    pagestokeep = [x-1 for x in pdfpagenumaliases[1::]] + [totpages-1]

    # Initialize output
    output = PdfFileWriter()
    # Add content to output
    for i in pagestokeep:
        p = infile.getPage(i)
        p.cropBox.lowerLeft = (0, 10)

        output.addPage(p)
    # Write to output file
    with open('out.pdf', 'wb') as f:
        output.write(f)
