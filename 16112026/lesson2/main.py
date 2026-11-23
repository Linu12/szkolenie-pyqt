import sys
from PySide6.QtWidgets import QApplication, QWidget

app = QApplication(sys.argv)

okno = QWidget()

okno.setWindowTitle("Lekcja 2")
# okno.resize(400,400)

okno.setFixedSize(600, 500)   # rozmiar stały, użytkownik nie może zmienić
okno.move(100, 100)           # pozycja lewego górnego rogu na ekranie
okno.setMinimumSize(300, 200) # nie da się zmniejszyć poniżej tego rozmiaru

okno.show()
sys.exit(app.exec())