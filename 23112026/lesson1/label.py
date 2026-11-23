import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

app = QApplication(sys.argv)

okno = QWidget()
okno.setWindowTitle("QLabel - etykiety")
okno.resize(350, 200)

etykieta1 = QLabel("Witaj w aplikacji!")
etykieta2 = QLabel("<b>Pogrubiony</b> i <i>pochylony</i> tekst")
etykieta3 = QLabel("Tekst wyśrodkowany")
etykieta3.setStyleSheet("color: darkgreen; font-size: 18px;")

layout = QVBoxLayout()
layout.addWidget(etykieta1)
layout.addWidget(etykieta2)
layout.addWidget(etykieta3)
okno.setLayout(layout)

okno.show()
sys.exit(app.exec())