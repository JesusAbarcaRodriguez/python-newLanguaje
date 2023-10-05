from PyQt5.QtCore import Qt, QRegExp
from PyQt5.QtGui import QSyntaxHighlighter, QColor, QTextCharFormat  # Añade QTextCharFormat aquí


class LexicalHighlighter(QSyntaxHighlighter):
    def __init__(self, parent=None):
        super(LexicalHighlighter, self).__init__(parent)
        self.highlighting_rules = []
        orange_color = QColor(255, 124, 0)
        red_color = QColor(255, 62, 0)
        comments_color = QColor(128, 128, 128)
        keyword_formatBlue = QTextCharFormat()
        keyword_formatOrange = QTextCharFormat()
        keyword_formatRed = QTextCharFormat()
        keyword_formatGreen = QTextCharFormat()
        string_format = QTextCharFormat()
        comments_format = QTextCharFormat()
        keyword_formatGreen.setForeground(Qt.green)
        keyword_formatRed.setForeground(red_color)
        keyword_formatBlue.setForeground(Qt.blue)
        keyword_formatOrange.setForeground(orange_color)

        keywords = ["ENTERO", "FLOTANTE","BOOLEANO", "CADENA", "CARACTER"]  # Agrega aquí más palabras clave si es necesario
        for keyword in keywords:
            pattern = "\\b" + keyword + "\\b"
            rule = (QRegExp(pattern), keyword_formatBlue)
            self.highlighting_rules.append(rule)
        keywords = ["MIENTRAS", "DE", "CUANDO", "SINO"]  # Agrega aquí más palabras clave si es necesario
        for keyword in keywords:
                pattern = "\\b" + keyword + "\\b"
                rule = (QRegExp(pattern), keyword_formatOrange)
                self.highlighting_rules.append(rule)
        
        keywords = ["PROCEDIMIENTO", "FUNCION"]
        for keyword in keywords:
                pattern = "\\b" + keyword + "\\b"
                rule = (QRegExp(pattern), keyword_formatRed)
                self.highlighting_rules.append(rule)
        keywords = ["INICIO", "FIN", "LEER", "ESCRIBIR"]
        for keyword in keywords:
                pattern = "\\b" + keyword + "\\b"
                rule = (QRegExp(pattern), keyword_formatGreen)
                self.highlighting_rules.append(rule)

        
        pattern = r'"[^"]*"' # Reconoce cadenas entre comillas
        string_format.setForeground(orange_color)  # Color de texto para las cadenas
        rule = (QRegExp(pattern), string_format)
        self.highlighting_rules.append(rule)
        
        pattern = r'\$[^$]*\$' # RECONOCE TEXTO ENTRE $ 
        comments_format.setForeground(comments_color)  # Color de texto para las cadenas
        rule = (QRegExp(pattern), comments_format)
        self.highlighting_rules.append(rule)

    def highlightBlock(self, text):
        for pattern, format in self.highlighting_rules:
            expression = QRegExp(pattern)
            index = expression.indexIn(text)
            while index >= 0:
                length = expression.matchedLength()
                self.setFormat(index, length, format)
                index = expression.indexIn(text, index + length)
