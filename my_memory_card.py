from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QHBoxLayout, QButtonGroup, QWidget, QPushButton, QLabel, QVBoxLayout, QRadioButton, QGroupBox
from random import randint, shuffle

asks = {
    'сколько живёт Путин?': ['хлеб', '4', '76598569850109 лет', 'а?'],
    'кто ты такой?': ['я презедент украины', 'а ты кто?' , 'я гусь', 'да блин к чему это?'],
    'ты любишь майнкрафт?': ['дааааааааааааааааааа', 'неет', 'не обязан', 'да отстань ты от меня']
}
print(list(asks.items())[randint(0, len(asks)-1)])
app = QApplication([])
x = QWidget()
x.setWindowTitle('гусь')
x.move(1000, 90)
x.resize(500, 00)
lb_Question = QLabel('сколько живёт Путин?')
RadioGroupBox = QGroupBox('Варики ответов')

b1 = QRadioButton('хлеб')
b2 = QRadioButton('4')
b3 = QRadioButton('76598569850109 лет')
b4 = QRadioButton('а?')
btn_OK = QPushButton('ответить')

RadioGroup = QButtonGroup()
RadioGroup.addButton(b1)
RadioGroup.addButton(b2)
RadioGroup.addButton(b3)
RadioGroup.addButton(b4)

line_h = QHBoxLayout()
line_v = QVBoxLayout()
line_v2 = QVBoxLayout()

line_v.addWidget(b1, alignment=Qt.AlignCenter)
line_v.addWidget(b2, alignment=Qt.AlignCenter)
line_v2.addWidget(b3, alignment=Qt.AlignCenter)
line_v2.addWidget(b4, alignment=Qt.AlignCenter)

line_h.addLayout(line_v)
line_h.addLayout(line_v2)

RadioGroupBox.setLayout(line_h)

layout_l1 = QHBoxLayout()
layout_l2 = QHBoxLayout()
layout_l3 = QHBoxLayout()

AnsGroupBox = QGroupBox('Результат')
lb_result = QLabel('прав ты или нет?')
lb_Correct = QLabel('ответ здеся')
layout_res = QVBoxLayout()
layout_res.addWidget(lb_result, alignment=(Qt.AlignCenter | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)

layout_l1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_l2.addWidget(RadioGroupBox)
layout_l2.addWidget(AnsGroupBox)
layout_l3.addStretch(1)
layout_l3.addWidget(btn_OK, stretch=2)
layout_l3.addStretch(1)

AnsGroupBox.hide()

layout_card = QVBoxLayout()
layout_card.addLayout(layout_l1, stretch=2)
layout_card.addLayout(layout_l2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_l3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)

x.setLayout(layout_card)

def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('ответитттттттьюббиижвяапбжфулузгшйгнещцорагнр')
    RadioGroup.setExclusive(False)
    b1.setChecked(False)
    b2.setChecked(False)
    b3.setChecked(False)
    b4.setChecked(False)
    RadioGroup.setExclusive(True)

answers = [b1, b2, b3, b4]

def ask():
    all = list(asks.items())
    vopros, otvet = all[randint(0, len(asks)-1)]
    answers[0].setText(otvet[0])
    answers[1].setText(otvet[1])
    answers[2].setText(otvet[2])
    answers[3].setText(otvet[3])
    lb_Question.setText(vopros)
    lb_Correct.setText(otvet[0])
    show_question()


def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('new vopros')


btn_OK.clicked.connect(show_result)

def show_correct(res):
    lb_result.setText(res)
    show_result()

def check_answer():
    if answers[0].isCheked():
        show_correct('Правильно!')
    else:
        if answers[1].isChecked() or answers[2].isCheked() or answers[3].isChecked():
            show_correct('ты по моему перепутал')
        
def click_OK():
    if btn_OK.text() == 'ответить':
        check_answer()
    else:
        ask()

ask()
x.show()
app.exec_()