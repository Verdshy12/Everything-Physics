import sys
import random
from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QGraphicsDropShadowEffect
)
from PyQt5.QtGui import QFont, QColor, QPainter
from PyQt5.QtCore import Qt, QTimer


class HoverButton(QPushButton):
    def __init__(self, text):
        super().__init__(text)
        self.default_font_size = 20
        self.setFont(QFont("Segoe UI", self.default_font_size))
        self.setStyleSheet("""
            QPushButton {
                background-color: #2a9df4;
                color: white;
                border-radius: 12px;
                padding: 10px;
            }
        """)
        # Add shadow effect
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(20)
        shadow.setXOffset(0)
        shadow.setYOffset(0)
        shadow.setColor(QColor(0, 0, 0, 180))
        self.setGraphicsEffect(shadow)

    def enterEvent(self, event):
        self.setFont(QFont("Segoe UI", self.default_font_size + 2))
        self.setStyleSheet("""
            QPushButton {
                background-color: #1a8de0;
                color: white;
                border-radius: 12px;
                padding: 10px;
            }
        """)
        super().enterEvent(event)

    def leaveEvent(self, event):
        self.setFont(QFont("Segoe UI", self.default_font_size))
        self.setStyleSheet("""
            QPushButton {
                background-color: #2a9df4;
                color: white;
                border-radius: 12px;
                padding: 10px;
            }
        """)
        super().leaveEvent(event)


class PhysicsWorldHome(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Physics World")
        self.setGeometry(300, 150, 800, 500)
        self.setStyleSheet("background-color: black;")

        # Floating equations
        self.equations = [
            "E = mc²", "F = ma", "∇·E = ρ/ε₀", "iħ∂ψ/∂t = Ĥψ",
            "V = IR", "pV = nRT", "λ = h/p", "Δx·Δp ≥ ħ/2"
        ]
        self.floating_texts = [
            [random.randint(0, 750), random.randint(0, 450), random.choice(self.equations)]
            for _ in range(10)
        ]
        self.timer = QTimer()
        self.timer.timeout.connect(self.animate_equations)
        self.timer.start(100)

        # Layout
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)

        title = QLabel("Let's Learn Physics")
        title.setFont(QFont("Georgia", 32, QFont.Bold))
        title.setStyleSheet("color: white; margin-bottom: 40px;")
        title.setAlignment(Qt.AlignCenter)

        explore_btn = HoverButton("Explore Science Facts")
        calc_btn = HoverButton("Calculate")

        layout.addWidget(title)
        layout.addWidget(explore_btn)
        layout.addWidget(calc_btn)

        self.setLayout(layout)

    def animate_equations(self):
        for eq in self.floating_texts:
            eq[1] -= 1  # move up
            if eq[1] < -20:
                eq[1] = 500
                eq[0] = random.randint(0, 750)
                eq[2] = random.choice(self.equations)
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(QColor(255, 255, 255, 50))
        painter.setFont(QFont("Courier", 14))
        for x, y, eq in self.floating_texts:
            painter.drawText(x, y, eq)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PhysicsWorldHome()
    window.show()
    sys.exit(app.exec_())
