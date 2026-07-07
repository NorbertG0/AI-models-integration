import sys, os
from dotenv import load_dotenv

from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QTextEdit, QLineEdit, QPushButton
)

from PySide6.QtCore import Qt

from claude import claude_prompt
from gemini import gemini_prompt
from grok import grok_prompt
from gpt import openai_prompt


# LOAD ENV VALUES
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GROK_API_KEY = os.getenv("GROK_API_KEY")
CLAUDE_API_KEY = os.getenv("CLAUDE_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


app = QApplication(sys.argv)

window = QWidget()
window.resize(1200, 700)

main_layout = QVBoxLayout()
chats_layout = QHBoxLayout()

def create_column(name):
    col = QVBoxLayout()

    label = QLabel(name)
    text = QTextEdit()

    col.addWidget(label)
    col.addWidget(text)

    return col, text

gemini_col, gemini = create_column("Gemini")
grok_col, grok = create_column("Grok")
anthropic_col, anthropic = create_column("Anthropic")
openai_col, openai_box = create_column("OpenAI")

chats_layout.addLayout(gemini_col)
chats_layout.addLayout(grok_col)
chats_layout.addLayout(anthropic_col)
chats_layout.addLayout(openai_col)

input_box = QLineEdit()
input_box.setFixedWidth(500)
input_box.setFixedHeight(50)

button = QPushButton("Wyślij")
button.setFixedWidth(200)
button.setFixedHeight(50)

# API CALLS FUNCTION
def prompt_request():
    prompt = input_box.text()

    if not prompt:
        return

    try:
        gemini_response = gemini_prompt(prompt, GEMINI_API_KEY)
    except Exception as e:
        gemini_response = f'Error: {e}'

    try:
        grok_response = grok_prompt(prompt, GROK_API_KEY)
    except Exception as e:
        grok_response = f'Error: {e}'

    try:
        anthropic_response = claude_prompt(prompt, CLAUDE_API_KEY)
    except Exception as e:
        anthropic_response = f'Error: {e}'

    try:
        openai_response = openai_prompt(prompt, OPENAI_API_KEY)
    except Exception as e:
        openai_response = f'Error: {e}'

    gemini.append(f"YOU:\n{prompt}\n\nGEMINI:\n{gemini_response}\n")
    grok.append(f"YOU:\n{prompt}\n\nGROK:\n{grok_response}\n")
    anthropic.append(f"YOU:\n{prompt}\n\nCLAUDE:\n{anthropic_response}\n")
    openai_box.append(f"YOU:\n{prompt}\n\nCHAT GPT:\n{openai_response}\n")



button.clicked.connect(prompt_request)

main_layout.addSpacing(20)
main_layout.addWidget(input_box, alignment=Qt.AlignCenter)
main_layout.addWidget(button, alignment=Qt.AlignCenter)
main_layout.addSpacing(80)
main_layout.addLayout(chats_layout)

window.setWindowTitle("AI Comparsion")
window.setLayout(main_layout)
window.show()

sys.exit(app.exec())