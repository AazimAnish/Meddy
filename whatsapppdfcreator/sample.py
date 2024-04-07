import tempfile
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle, KeepTogether, Frame
from heyoo import WhatsApp
import requests
# Create a PDF file
pdf = SimpleDocTemplate(
    "prescription.pdf",
    pagesize=letter,
    rightMargin=30,
    leftMargin=30,
    topMargin=30,
    bottomMargin=30
)
width, height = letter
# Sample text fields

title = "PRESCRIPTION"
subtitle = "Dr. John Doe"
content = """
DEA# GB 05455616\n
Age: 30\n
Date: 07-04-2024<br></br>

Medication:\n
- Medication 1: 1 pill, twice daily\n
- Medication 2: 1 pill, once daily\n

Instructions:\n
Take with food.\n

Signature:\n
"""

# Sample image (signature)
image_filename = "image.png"
styles = getSampleStyleSheet()
"""
# Styles

title_style = styles["Heading1"]
subtitle_style = styles["Heading2"]
content_style = ParagraphStyle(
    "content_style",
    parent=styles["BodyText"],
    fontSize=12,
    leading=15,
)
signature_style = ParagraphStyle(
    "signature_style",
    parent=styles["BodyText"],
    fontSize=12,
    leading=15,
    alignment=2  # right-aligned
)
"""
# Content
content_elements = []


word1 = 'DEA# GB 2434234'
word2 = 'LIC # 9823423'
total_length = 160
middle_space_length = total_length - len(word1) - len(word2)
xml_markup = f'''
    {word1}
    {"&nbsp;" * middle_space_length}
    {word2}
'''
# Title
content_elements.append(Paragraph(xml_markup, styles['Normal']))
content_elements.append(Spacer(1, 30))

content_elements.append(Paragraph("Rajagiri Hospital", ParagraphStyle('CenteredStyle', parent=styles['Heading1'], alignment=1)))
content_elements.append(Paragraph("Near GTN Junction, Munnar Rd, Chungamvely", ParagraphStyle('CenteredStyle', parent=styles['Heading5'], alignment=1)))
content_elements.append(Paragraph("Aluva, Kochi, Kerala 683112", ParagraphStyle('CenteredStyle', parent=styles['Heading5'], alignment=1)))


content_elements.append(Image("image copy 4.png", width=700, height=50))

content_elements.append(Paragraph("Name: mishal k faisal", styles['Heading3']))
content_elements.append(Spacer(1, -12))
content_elements.append(Paragraph("Address: Kalamassery, Kochi", styles['Heading3']))
content_elements.append(Spacer(1, -12))
content_elements.append(Paragraph("Age: 21", styles['Heading3']))
content_elements.append(Spacer(1, -12))
content_elements.append(Paragraph("Gender: M", styles['Heading3']))
content_elements.append(Spacer(1, -12))
content_elements.append(Paragraph("Date: 04-04-2024", styles['Heading3']))

content_elements.append(Spacer(1, 15))
content_elements.append(Image("image copy 5.png", width=75, height=75, hAlign="LEFT"))


data = [['Name', 'Age', 'Gender'],
            ['John Doe', '30', 'Male'],
            ['Jane Doe', '25', 'Female']]
    
table = Table(data, colWidths=[width/3, width/3, width/3])
table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ('LEFTPADDING', (0, 0), (-1, 0), 12),
    ('RIGHTPADDING', (0, 0), (-1, 0), 12),
    ('TOPPADDING', (0, 0), (-1, 0), 12),
    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
    ('GRID', (0, 0), (-1, -1), 1, colors.black)
]))
    
content_elements.append(table)
"""
# Subtitle
content_elements.append(Paragraph(subtitle, subtitle_style))
content_elements.append(Spacer(1, 12))

# Content
content_elements.append(Paragraph(content, content_style))
content_elements.append(Spacer(1, 12))

# Signature
content_elements.append(Spacer(1, 36))  # space before signature
content_elements.append(Paragraph("Dr. John Doe", signature_style))
content_elements.append(Image(image_filename, width=150, height=50))

"""
# Build PDF

messenger = WhatsApp("EAAGL5dZCRyoEBO5zEVXpckSwl7RMrjfMc4IYu3EWpVdGuj0CYDm08o5pkQD39mfmg6tikNOFsCpxgJjoNapnPZAcpivNZCZCr3gQMNaZCCSZCI0g6IHqnAYy7ZAVCR9jLJJKW2tQzCZB0cjkDigRXnXfgDoZC7oNxmrw3Qaz3ZCcV2icSGClvtOMNkZB6DAWzPg9DLMvHn0NkaUML6rDuUwopiB", phone_number_id="259164670622151")
messenger.send_document(
        document="https://pdfobject.com/pdf/sample.pdf",
        recipient_id="918129953715",
        caption="Lab Reports"
    )
