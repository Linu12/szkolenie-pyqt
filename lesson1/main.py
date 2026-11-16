import sys
from PySide6.QtWidgets import QApplication, QLabel

app = QApplication(sys.argv)

label = QLabel("Witaj w PySide6! To jest lekcja1")
label.resize(500, 500)
label.show()

sys.exit(app.exec())