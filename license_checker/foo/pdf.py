"""PDF format style"""
from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        # Arial bold 15
        self.set_font('Arial', 'B', 14)
        # Move to the right
        self.cell(60)
        # Title
        self.cell(90, 15, 'License Compatibility Report', 1, 0, 'C')
        # Line break
        self.ln(20)

    # Page footer
    # def footer(self):
    #     # Position at 1.5 cm from bottom
    #     self.set_y(-15)
    #     # Arial italic 8
    #     self.set_font('Arial', 'I', 8)
    #     # Page number
    #     self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')