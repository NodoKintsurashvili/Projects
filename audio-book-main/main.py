import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout,
    QPushButton, QLabel, QTextEdit,
    QListWidget, QListWidgetItem,
    QLineEdit, QComboBox
)
from database import init_db, get_documents, get_sections, save_document
from logic import Ebook, Essay


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.conn = init_db()

        self.setWindowTitle("Smart Book Manager")
        self.setGeometry(200, 200, 850, 650)

        layout = QVBoxLayout()

        self.title_input = QLineEdit()
        self.title_input.setPlaceholderText("Title")

        self.author_input = QLineEdit()
        self.author_input.setPlaceholderText("Author")

        self.type_box = QComboBox()
        self.type_box.addItems(["Ebook", "Essay"])

        self.text_input = QTextEdit()

        self.add_btn = QPushButton("Add Document")
        self.add_btn.clicked.connect(self.add_document)

        self.doc_list = QListWidget()
        self.section_list = QListWidget()
        self.output = QTextEdit()
        self.output.setReadOnly(True)

        self.doc_list.itemClicked.connect(self.load_sections)
        self.section_list.itemClicked.connect(self.show_text)

        layout.addWidget(QLabel("Title"))
        layout.addWidget(self.title_input)
        layout.addWidget(QLabel("Author"))
        layout.addWidget(self.author_input)
        layout.addWidget(QLabel("Type"))
        layout.addWidget(self.type_box)
        layout.addWidget(QLabel("Text"))
        layout.addWidget(self.text_input)
        layout.addWidget(self.add_btn)
        layout.addWidget(QLabel("Documents"))
        layout.addWidget(self.doc_list)
        layout.addWidget(QLabel("Sections"))
        layout.addWidget(self.section_list)
        layout.addWidget(QLabel("Content"))
        layout.addWidget(self.output)

        self.setLayout(layout)
        self.load_documents()

    def add_document(self):
        title = self.title_input.text()
        author = self.author_input.text()
        text = self.text_input.toPlainText()
        doc_type = self.type_box.currentText()

        if not title or not text:
            return

        if doc_type == "Ebook":
            document = Ebook(title, author, text, genre="General")
        else:
            document = Essay(title, author, text)

        save_document(self.conn, document)

        self.title_input.clear()
        self.author_input.clear()
        self.text_input.clear()

        self.load_documents()

    def load_documents(self):
        self.doc_list.clear()
        for doc in get_documents(self.conn):
            item = QListWidgetItem(f"{doc[0]} - {doc[1]}")
            item.setData(1, doc[0])
            self.doc_list.addItem(item)

    def load_sections(self, item):
        self.section_list.clear()
        self.output.clear()
        doc_id = item.data(1)
        for sec in get_sections(self.conn, doc_id):
            sec_item = QListWidgetItem(sec[0])
            sec_item.setData(1, sec[1])
            self.section_list.addItem(sec_item)
        
        doc_id = item.data(1)
        print(get_sections(self.conn, doc_id))

    def show_text(self, item):
        self.output.setText(item.data(1))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec_())