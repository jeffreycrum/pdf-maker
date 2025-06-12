import pandas as pd
from fpdf import FPDF

df = pd.read_csv("topics.csv")
pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)
header_line = 20
footer_line = 265

for index, row in df.iterrows():
    pdf.add_page()

    # set the header
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(180, 100, 180)
    pdf.cell(w=0, h=12, txt=row['Topic'], align="L", ln=1)
    for l in range(header_line, footer_line, 10):
        pdf.line(10, l, 200, l)

    # set the footer
    pdf.ln(footer_line)
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=row['Topic'], align="R")

    for i in range(row['Pages'] - 1):
        pdf.add_page()

        pdf.ln(footer_line)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row['Topic'], align="R")

        for l in range(header_line, footer_line, 10):
            pdf.line(10, l, 200, l)

pdf.output("output.pdf")
