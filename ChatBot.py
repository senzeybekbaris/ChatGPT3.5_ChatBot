
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 08:45:33 2023

@author: Simge
"""
import sys
from openai import OpenAI

client = OpenAI(api_key="YOUR-API-KEY")
import logging
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)
from dotenv import load_dotenv
import os

load_dotenv()


class ChatApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("ChatGPT Chat Bot")
        self.setGeometry(100, 100, 400, 100)

        # Central widget
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Creating a layout
        layout = QVBoxLayout()

        # Textbox for input
        self.user_input = QTextEdit(self)
        layout.addWidget(self.user_input)


        # Textbox for response
        self.output_text = QTextEdit(self)
        self.output_text.setReadOnly(True)  # Set output text box as read-only
        layout.addWidget(self.output_text)

        # Sending the message via clicking to the button or pressing enter
        send_button = QPushButton("Send the message")
        send_button.clicked.connect(self.chatWithGPT)
        layout.addWidget(send_button)

        central_widget.setLayout(layout)

    def GPT(self, text):
        try:
            response = client.chat.completions.create(model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": f"{text}"},
            ])
            return response.choices[0].message.content
        except Exception as e:
            logging.error(f"Error communicating with GPT: {e}")
            return "An error occurred while processing your request."

    def chatWithGPT(self):
        # Input from the user
        user_input = self.user_input.toPlainText()

        # ChatGPT's response
        response = self.GPT(user_input)

        # Response to the output
        self.output_text.setPlainText(response)


def main():
    app = QApplication(sys.argv)
    window = ChatApp()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()