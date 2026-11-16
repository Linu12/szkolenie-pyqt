import sys
from pathlib import Path
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget

app = QApplication(sys.argv)


# Ścieżka do style.qss względem lokalizacji main.py
style_path = Path(__file__).with_name("style.qss")

# Wczytanie stylów
app.setStyleSheet(style_path.read_text(encoding="utf-8"))

okno = QMainWindow()
okno.label = QLabel("Witaj w PySide6! To jest lekcja3", okno)
okno.setWindowTitle("Moje główne okno")
# okno.label.setGeometry(0, 0, 300, 350)

# central = QWidget()
okno.setCentralWidget(okno.label)

# layout = QVBoxLayout(central)
# layout.addWidget(okno.label)



okno.resize(500, 350)
okno.statusBar().showMessage("Gotowe!")
okno.show()

sys.exit(app.exec())