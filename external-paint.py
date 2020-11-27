import tkinter

class Pen:
    def __init__(self, color, width=1, **options):
        self.color = color
        self.width = width

class Brush:
    def __init__(self, color, **options):
        self.color = color

class Font:
    def __init__(self, color, font):
        self.color = color
        self.font = font
        self.tkfont = None # cache for tkFont objects

class Draw:
    def __init__(self, canvas):
        self.canvas = canvas

    def clear(self):
        self.canvas.delete("all")

    def draw(self, method, xy, pen, brush, **options):
        # pens and brushes can be given in any order
        if isinstance(pen, Pen):
            options["outline"] = pen.color
            options["width"] = pen.width
        elif isinstance(brush, Pen):
            options["outline"] = brush.color
            options["width"] = brush.width
        else:
            options["outline"] = ""
        if isinstance(brush, Brush):
            options["fill"] = brush.color
        elif isinstance(pen, Brush):
            options["fill"] = pen.color
        else:
            options["fill"] = ""
        if pen or brush:
            return method(xy, **options)

    def line(self, xy, pen=None):
        if pen:
            return self.canvas.create_line(
                xy, fill=pen.color, width=pen.width
                )

    def ellipse(self, xy, pen=None, brush=None):
        return self.draw(self.canvas.create_oval, xy, pen, brush)

    def rectangle(self, xy, pen=None, brush=None):
        return self.draw(self.canvas.create_rectangle, xy, pen, brush)

    def polygon(self, xy, pen=None, brush=None):
        return self.draw(self.canvas.create_polygon, xy, pen, brush)

    def text(self, xy, text, font):
        if font:
            return self.canvas.create_text(
                xy, text=text, font=font.font, fill=font.color, anchor="nw"
                )

    def textsize(self, text, font):
        if not font.tkfont:
            font.tkfont = tkinter.Font(self.canvas, font=font.font)
            font.tkfont.height = font.tkfont.metrics("linespace")
        return font.tkfont.measure(text), font.tkfont.height