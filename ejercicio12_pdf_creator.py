from reportlab.pdfgen.canvas import Canvas

canvas = Canvas("Hello")
canvas.drawString(72,800, "Hello, World")
canvas.save()

