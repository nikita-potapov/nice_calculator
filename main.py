from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QApplication
import sys

WAITING_NUMBER = 0
ENTERING_NUMBER = 1
ERROR = 2


def get_num(string):
    if '.' in string:
        return float(string)
    return int(string)


class NiceCalculatorWindowUiForm(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(360, 510)
        Form.setMinimumSize(QtCore.QSize(360, 510))
        Form.setMaximumSize(QtCore.QSize(360, 510))
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.table = QtWidgets.QLCDNumber(Form)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.table.setFont(font)
        self.table.setDigitCount(12)
        self.table.setObjectName("table")
        self.verticalLayout.addWidget(self.table)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.btn8 = QtWidgets.QPushButton(Form)
        self.btn8.setMinimumSize(QtCore.QSize(80, 80))
        self.btn8.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(36)
        self.btn8.setFont(font)
        self.btn8.setObjectName("btn8")
        self.buttonGroup_digits = QtWidgets.QButtonGroup(Form)
        self.buttonGroup_digits.setObjectName("buttonGroup_digits")
        self.buttonGroup_digits.addButton(self.btn8)
        self.gridLayout.addWidget(self.btn8, 2, 1, 1, 1)
        self.btn2 = QtWidgets.QPushButton(Form)
        self.btn2.setMinimumSize(QtCore.QSize(80, 80))
        self.btn2.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(36)
        self.btn2.setFont(font)
        self.btn2.setObjectName("btn2")
        self.buttonGroup_digits.addButton(self.btn2)
        self.gridLayout.addWidget(self.btn2, 0, 1, 1, 1)
        self.btn_plus = QtWidgets.QPushButton(Form)
        self.btn_plus.setMinimumSize(QtCore.QSize(80, 80))
        self.btn_plus.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(36)
        self.btn_plus.setFont(font)
        self.btn_plus.setObjectName("btn_plus")
        self.buttonGroup_binary = QtWidgets.QButtonGroup(Form)
        self.buttonGroup_binary.setObjectName("buttonGroup_binary")
        self.buttonGroup_binary.addButton(self.btn_plus)
        self.gridLayout.addWidget(self.btn_plus, 0, 3, 1, 1)
        self.btn_eq = QtWidgets.QPushButton(Form)
        self.btn_eq.setMinimumSize(QtCore.QSize(80, 80))
        self.btn_eq.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(36)
        self.btn_eq.setFont(font)
        self.btn_eq.setObjectName("btn_eq")
        self.gridLayout.addWidget(self.btn_eq, 3, 2, 1, 1)
        self.btn0 = QtWidgets.QPushButton(Form)
        self.btn0.setMinimumSize(QtCore.QSize(80, 80))
        self.btn0.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(36)
        self.btn0.setFont(font)
        self.btn0.setObjectName("btn0")
        self.buttonGroup_digits.addButton(self.btn0)
        self.gridLayout.addWidget(self.btn0, 3, 0, 1, 1)
        self.btn_div = QtWidgets.QPushButton(Form)
        self.btn_div.setMinimumSize(QtCore.QSize(80, 80))
        self.btn_div.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(36)
        self.btn_div.setFont(font)
        self.btn_div.setObjectName("btn_div")
        self.buttonGroup_binary.addButton(self.btn_div)
        self.gridLayout.addWidget(self.btn_div, 3, 3, 1, 1)
        self.btn1 = QtWidgets.QPushButton(Form)
        self.btn1.setMinimumSize(QtCore.QSize(80, 80))
        self.btn1.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(36)
        self.btn1.setFont(font)
        self.btn1.setObjectName("btn1")
        self.buttonGroup_digits.addButton(self.btn1)
        self.gridLayout.addWidget(self.btn1, 0, 0, 1, 1)
        self.btn9 = QtWidgets.QPushButton(Form)
        self.btn9.setMinimumSize(QtCore.QSize(80, 80))
        self.btn9.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(36)
        self.btn9.setFont(font)
        self.btn9.setObjectName("btn9")
        self.buttonGroup_digits.addButton(self.btn9)
        self.gridLayout.addWidget(self.btn9, 2, 2, 1, 1)
        self.btn_dot = QtWidgets.QPushButton(Form)
        self.btn_dot.setMinimumSize(QtCore.QSize(80, 80))
        self.btn_dot.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(36)
        self.btn_dot.setFont(font)
        self.btn_dot.setObjectName("btn_dot")
        self.gridLayout.addWidget(self.btn_dot, 3, 1, 1, 1)
        self.btn3 = QtWidgets.QPushButton(Form)
        self.btn3.setMinimumSize(QtCore.QSize(80, 80))
        self.btn3.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(36)
        self.btn3.setFont(font)
        self.btn3.setObjectName("btn3")
        self.buttonGroup_digits.addButton(self.btn3)
        self.gridLayout.addWidget(self.btn3, 0, 2, 1, 1)
        self.btn4 = QtWidgets.QPushButton(Form)
        self.btn4.setMinimumSize(QtCore.QSize(80, 80))
        self.btn4.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(36)
        self.btn4.setFont(font)
        self.btn4.setObjectName("btn4")
        self.buttonGroup_digits.addButton(self.btn4)
        self.gridLayout.addWidget(self.btn4, 1, 0, 1, 1)
        self.btn5 = QtWidgets.QPushButton(Form)
        self.btn5.setMinimumSize(QtCore.QSize(80, 80))
        self.btn5.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(36)
        self.btn5.setFont(font)
        self.btn5.setObjectName("btn5")
        self.buttonGroup_digits.addButton(self.btn5)
        self.gridLayout.addWidget(self.btn5, 1, 1, 1, 1)
        self.btn7 = QtWidgets.QPushButton(Form)
        self.btn7.setMinimumSize(QtCore.QSize(80, 80))
        self.btn7.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(36)
        self.btn7.setFont(font)
        self.btn7.setObjectName("btn7")
        self.buttonGroup_digits.addButton(self.btn7)
        self.gridLayout.addWidget(self.btn7, 2, 0, 1, 1)
        self.btn6 = QtWidgets.QPushButton(Form)
        self.btn6.setMinimumSize(QtCore.QSize(80, 80))
        self.btn6.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(36)
        self.btn6.setFont(font)
        self.btn6.setObjectName("btn6")
        self.buttonGroup_digits.addButton(self.btn6)
        self.gridLayout.addWidget(self.btn6, 1, 2, 1, 1)
        self.btn_minus = QtWidgets.QPushButton(Form)
        self.btn_minus.setMinimumSize(QtCore.QSize(80, 80))
        self.btn_minus.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(36)
        self.btn_minus.setFont(font)
        self.btn_minus.setObjectName("btn_minus")
        self.buttonGroup_binary.addButton(self.btn_minus)
        self.gridLayout.addWidget(self.btn_minus, 1, 3, 1, 1)
        self.btn_mult = QtWidgets.QPushButton(Form)
        self.btn_mult.setMinimumSize(QtCore.QSize(80, 80))
        self.btn_mult.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(36)
        self.btn_mult.setFont(font)
        self.btn_mult.setObjectName("btn_mult")
        self.buttonGroup_binary.addButton(self.btn_mult)
        self.gridLayout.addWidget(self.btn_mult, 2, 3, 1, 1)
        self.btn_pow = QtWidgets.QPushButton(Form)
        self.btn_pow.setMinimumSize(QtCore.QSize(80, 80))
        self.btn_pow.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(36)
        self.btn_pow.setFont(font)
        self.btn_pow.setObjectName("btn_pow")
        self.buttonGroup_binary.addButton(self.btn_pow)
        self.gridLayout.addWidget(self.btn_pow, 4, 0, 1, 1)
        self.btn_sqrt = QtWidgets.QPushButton(Form)
        self.btn_sqrt.setMinimumSize(QtCore.QSize(80, 80))
        self.btn_sqrt.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(36)
        self.btn_sqrt.setFont(font)
        self.btn_sqrt.setObjectName("btn_sqrt")
        self.gridLayout.addWidget(self.btn_sqrt, 4, 1, 1, 1)
        self.btn_fact = QtWidgets.QPushButton(Form)
        self.btn_fact.setMinimumSize(QtCore.QSize(80, 80))
        self.btn_fact.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(36)
        self.btn_fact.setFont(font)
        self.btn_fact.setObjectName("btn_fact")
        self.gridLayout.addWidget(self.btn_fact, 4, 2, 1, 1)
        self.btn_clear = QtWidgets.QPushButton(Form)
        self.btn_clear.setMinimumSize(QtCore.QSize(80, 80))
        self.btn_clear.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(36)
        self.btn_clear.setFont(font)
        self.btn_clear.setStyleSheet("background-color: rgb(254, 166, 43);")
        self.btn_clear.setObjectName("btn_clear")
        self.gridLayout.addWidget(self.btn_clear, 4, 3, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Красивый калькулятор"))
        self.btn8.setText(_translate("Form", "8"))
        self.btn2.setText(_translate("Form", "2"))
        self.btn_plus.setText(_translate("Form", "+"))
        self.btn_eq.setText(_translate("Form", "="))
        self.btn0.setText(_translate("Form", "0"))
        self.btn_div.setText(_translate("Form", "/"))
        self.btn1.setText(_translate("Form", "1"))
        self.btn9.setText(_translate("Form", "9"))
        self.btn_dot.setText(_translate("Form", "."))
        self.btn3.setText(_translate("Form", "3"))
        self.btn4.setText(_translate("Form", "4"))
        self.btn5.setText(_translate("Form", "5"))
        self.btn7.setText(_translate("Form", "7"))
        self.btn6.setText(_translate("Form", "6"))
        self.btn_minus.setText(_translate("Form", "-"))
        self.btn_mult.setText(_translate("Form", "*"))
        self.btn_pow.setText(_translate("Form", "^"))
        self.btn_sqrt.setText(_translate("Form", "√"))
        self.btn_fact.setText(_translate("Form", "!"))
        self.btn_clear.setText(_translate("Form", "С"))


class NiceCalculatorWindow(NiceCalculatorWindowUiForm, QWidget):
    def __init__(self):
        super(NiceCalculatorWindow, self).__init__()
        self.setupUi(self)

        self.program_state = None

        self.buffer = None
        self.operand = None
        self.again = None
        self.last_operation = None

        self.btn_clear_clicked()

        for i in range(10):
            getattr(self, 'btn%d' % i).clicked.connect(self.btn_digits_clicked)

        self.btn_plus.clicked.connect(self.btn_plus_minus_clicked)
        self.btn_minus.clicked.connect(self.btn_plus_minus_clicked)
        self.btn_mult.clicked.connect(self.btn_mult_clicked)
        self.btn_div.clicked.connect(self.btn_div_clicked)
        self.btn_pow.clicked.connect(self.btn_pow_clicked)
        self.btn_sqrt.clicked.connect(self.btn_sqrt_clicked)
        self.btn_fact.clicked.connect(self.btn_fact_clicked)
        self.btn_eq.clicked.connect(self.btn_eq_clicked)
        self.btn_dot.clicked.connect(self.btn_dot_clicked)
        self.btn_clear.clicked.connect(self.btn_clear_clicked)

    def btn_digits_clicked(self):
        digit = (self.sender().text())
        if self.operand == '0' or \
            self.program_state == WAITING_NUMBER:
            if self.program_state == WAITING_NUMBER:
                self.program_state = ENTERING_NUMBER

            self.operand = digit
        else:
            self.operand += digit
        self.update_display()

    def btn_plus_minus_clicked(self):
        state = self.program_state

        if not self.buffer:
            self.last_operation = self.sender().text()
            self.buffer = '0'

        current_operation = self.sender().text()
        self.again = False
        if current_operation == self.last_operation:
            self.again = True
        self.last_operation = current_operation

        if state == ENTERING_NUMBER:
            self.program_state = WAITING_NUMBER
            if self.last_operation == '+':
                self.buffer = str(get_num(self.buffer) + get_num(self.operand))
            elif self.last_operation == '-':
                self.buffer = str(get_num(self.buffer) - get_num(self.operand))

            if self.again:
                self.table.display(self.buffer)

    def btn_mult_clicked(self):
        state = self.program_state

        if not self.buffer:
            self.last_operation = self.sender().text()
            self.buffer = '1'

        current_operation = self.sender().text()
        self.again = False
        if current_operation == self.last_operation:
            self.again = True
        self.last_operation = current_operation

        if state == ENTERING_NUMBER:
            self.program_state = WAITING_NUMBER

            self.buffer = str(get_num(self.buffer) * get_num(self.operand))

            if self.again:
                self.table.display(self.buffer)

    def btn_div_clicked(self):
        state = self.program_state

        if not float(self.operand):
            self.program_state = ERROR
            self.update_display()
            return

        current_operation = self.sender().text()
        self.again = False
        if current_operation == self.last_operation:
            self.again = True
        self.last_operation = current_operation

        if state == ENTERING_NUMBER:
            self.program_state = WAITING_NUMBER
            if self.buffer:
                self.btn_eq_clicked(self.again)
            else:
                self.buffer = self.operand

    def btn_pow_clicked(self):
        state = self.program_state

        if not self.buffer:
            self.program_state = WAITING_NUMBER
            self.buffer = self.operand
            return

        current_operation = self.sender().text()
        self.again = False
        if current_operation == self.last_operation:
            self.again = True
        self.last_operation = current_operation

        if state == ENTERING_NUMBER:
            self.program_state = WAITING_NUMBER

            self.buffer = str(get_num(self.buffer) ** get_num(self.operand))

            if self.again:
                self.table.display(self.buffer)

    def btn_sqrt_clicked(self):
        pass

    def btn_fact_clicked(self):
        pass

    def btn_eq_clicked(self, show_result=True):
        op_functions = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: a / b if '.' in str(a) + str(b) or a % b != 0 else a // b
        }

        op = self.last_operation
        if op in '+-*/':
            try:
                self.buffer = str(op_functions[op](get_num(self.buffer), get_num(self.operand)))

                self.display_show(self.buffer)
            except Exception as e:
                print(e)
                self.program_state = ERROR
                self.update_display()
        print(self.buffer, self.operand)

    def btn_dot_clicked(self):
        if self.operand.count('.') == 0:
            self.operand += '.'
            self.program_state = ENTERING_NUMBER
            self.update_display()

    def btn_clear_clicked(self):
        self.program_state = WAITING_NUMBER

        self.buffer = ''
        self.operand = '0'
        self.again = False
        self.last_operation = ''
        self.display_show(self.operand)

    def update_display(self):
        if self.program_state != ERROR:
            self.display_show(self.operand)
        else:
            self.btn_clear_clicked()
            self.table.display('ERROR')

    def display_show(self, arg):
        arg = str(arg)
        if 'e' in arg:
            arg, power = arg[:arg.index('e')], arg[arg.index('e'):]
            self.table.display(arg[:12 - len(power)] + power)
        else:                                                               
            print(arg)
            if len(arg) > 12:
                if '.' in arg:
                    before = arg[:arg.index('.')]
                    after = arg[arg.index('.') + 1:]
                    power = len(before) - 1 + len(after)
                    arg = before + after
                    arg = arg[0] + '.' + after
                    arg = arg[:12 - len('e' + str(power))] + 'e' + str(power)

                else:
                    power = 'e' + str(len(arg[12:]))
                    arg = arg[:12 - len(power)]
                    arg = arg + power

            self.table.display(arg)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = NiceCalculatorWindow()
    ex.show()
    sys.exit(app.exec())
