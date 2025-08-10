import sys
import subprocess
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLabel,
    QScrollArea, QStackedWidget
)
from PyQt5.QtGui import QFont, QPainter, QColor
from PyQt5.QtCore import Qt
from laws import laws
from equations import equations

# -------------------------
# DATA STRUCTURE
# -------------------------
physics_data = {
    "Laws": laws,
    "Equations": equations
}

class PhysicsWorld(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Everything Physics / Explore")
        self.setGeometry(200, 100, 900, 600)

        self.stack = QStackedWidget()
        layout = QVBoxLayout()
        layout.addWidget(self.stack)
        self.setLayout(layout)

        self.category_page = QWidget()
        self.items_page = QWidget()
        self.detail_page = QWidget()

        self.load_categories()


    # go_home
    def go_home(self):
        self.close() #closes current setWindowTitle
        subprocess.Popen(["python3", "home.py"])
    # -------------------------
    # Background paint
    # -------------------------
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.fillRect(self.rect(), QColor(20, 20, 20))
        painter.setPen(QColor(100, 255, 100, 120))
        font = QFont("Courier", 14)
        painter.setFont(font)

        eqs = [
            "E = mc²", "F = ma", "Δx Δp ≥ ħ/2",
            "V = IR", "a² + b² = c²", "∇·E = ρ/ε₀",
            "pV = nRT"
        ]
        for i, eq in enumerate(eqs):
            painter.drawText(50 + (i * 80) % self.width(),
                             50 + (i * 60) % self.height(), eq)

    # -------------------------
    # Categories page
    # -------------------------
    def load_categories(self):
        layout = QVBoxLayout()

        title = QLabel("What to Learn?")
        title.setFont(QFont("Arial", 20, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        for category in physics_data.keys():
            btn = QPushButton(category)
            btn.setFont(QFont("Arial", 14))
            btn.setFlat(True)
            btn.setStyleSheet("""
                QPushButton {
                    background-color: transparent;
                    color: white;
                    text-align: left;
                    padding: 8px;
                }
                QPushButton:hover {
                    background-color: rgba(255, 255, 255, 0.1);
                    border-radius: 5px;
                }
            """)
            btn.clicked.connect(lambda _, cat=category: self.load_items(cat))
            layout.addWidget(btn)


        layout.addStretch()
        self.category_page.setLayout(layout)
        self.stack.addWidget(self.category_page)
        self.stack.setCurrentWidget(self.category_page)

    # -------------------------
    # Items page
    # -------------------------

    def load_items(self, category):
        self.items_page = QWidget()
        layout = QVBoxLayout()

        title = QLabel(category)
        title.setFont(QFont("Arial", 20, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        container = QWidget()
        vbox = QVBoxLayout()

        for entry in physics_data[category]:
            item = entry["name"]
            btn = QPushButton(item)
            btn.setFont(QFont("Arial", 12))
            btn.setFlat(True)
            btn.setStyleSheet("""
                QPushButton {
                    background-color: transparent;
                    color: white;
                    text-align: AlignCenter;
                    padding: 6px;
                }
                QPushButton:hover {
                    background-color: rgba(255, 255, 255, 0.1);
                    border-radius: 5px;
                }
            """)
            btn.clicked.connect(lambda _, c=category, i=item: self.load_detail(c, i))
            vbox.addWidget(btn)


        container.setLayout(vbox)
        scroll.setWidget(container)
        layout.addWidget(scroll)

        back_btn = QPushButton("← Go Back")
        back_btn.clicked.connect(lambda: self.stack.setCurrentWidget(self.category_page))
        layout.addWidget(back_btn)

        home_btn = QPushButton("🏠 Home")
        home_btn.clicked.connect(self.go_home)
        layout.addWidget(home_btn)

        self.items_page.setLayout(layout)
        self.stack.addWidget(self.items_page)
        self.stack.setCurrentWidget(self.items_page)

    # -------------------------
    # Detail page
    # -------------------------
    def load_detail(self, category, item_name):
        self.detail_page = QWidget()
        layout = QVBoxLayout()

        # Find the entry
        info = next((x for x in physics_data[category] if x["name"] == item_name), None)

        if info:
            title = QLabel(info["name"])
            title.setFont(QFont("Arial", 20, QFont.Bold))
            title.setAlignment(Qt.AlignCenter)
            layout.addWidget(title)

            statement = QLabel(f"<b>Statement:</b> {info['statement']}")
            statement.setWordWrap(True)
            statement.setFont(QFont("Arial", 12))
            statement.setStyleSheet("color: white;")
            layout.addWidget(statement)

            equation = QLabel(f"<b>Equation:</b> {info['equation']}")
            equation.setWordWrap(True)
            equation.setFont(QFont("Arial", 12))
            equation.setStyleSheet("color: lightgreen;")
            layout.addWidget(equation)

        back_btn = QPushButton("← Back")
        back_btn.clicked.connect(lambda: self.stack.setCurrentWidget(self.items_page))
        layout.addWidget(back_btn)

        home_btn = QPushButton("🏠 Home")
        home_btn.clicked.connect(self.go_home)
        layout.addWidget(home_btn)

        self.detail_page.setLayout(layout)
        self.detail_page.setStyleSheet("background-color: black;")
        self.stack.addWidget(self.detail_page)
        self.stack.setCurrentWidget(self.detail_page)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = PhysicsWorld()
    win.show()
    sys.exit(app.exec_())
