import sys
import PySide6.QtWidgets

app = PySide6.QtWidgets.QApplication(sys.argv)

okno = PySide6.QtWidgets.QWidget()
okno.setWindowTitle("QLineEdit - pole tekstowe")
okno.resize(350, 200)

etykieta = PySide6.QtWidgets.QLabel("Podaj swoje imię:")
pole = PySide6.QtWidgets.QLineEdit()
przycisk = PySide6.QtWidgets.QPushButton("Przywitaj mnie")
wynik = PySide6.QtWidgets.QLabel("")


def przywitaj():
    imie = pole.text()
    wynik.setText(f"Cześć, {imie}!")


przycisk.clicked.connect(przywitaj)

layout = PySide6.QtWidgets.QVBoxLayout()
layout.addWidget(etykieta)
layout.addWidget(pole)
layout.addWidget(przycisk)
layout.addWidget(wynik)
okno.setLayout(layout)

okno.show()
sys.exit(app.exec())