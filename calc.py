# Em js seria o getElemntbyId
number1 = Element("number1")
number2 = Element("number2")
op = Element('result')  

# Valor Default no 'Result'
op.write('0')

# Funções ao apertar o botão
def somar(*args, **kwargs):
    num1 = int(number1.value)
    num2 = int(number2.value)
    operacao = num1 + num2
    op.element.classList.remove("alert-primary")
    op.element.classList.add("alert-success")
    op.write(operacao)  

def subtrair(*args, **kwargs):
    num1 = int(number1.value)
    num2 = int(number2.value)
    operacao = num1 - num2
    op.element.classList.remove("alert-primary")
    op.element.classList.add("alert-success")
    op.write(operacao)  

def multiplicar(*args, **kwargs):
    num1 = int(number1.value)
    num2 = int(number2.value)
    operacao = num1 * num2
    op.element.classList.remove("alert-primary")
    op.element.classList.add("alert-success")
    op.write(operacao)  

def dividir(*args, **kwargs):
    num1 = int(number1.value)
    num2 = int(number2.value)
    operacao = num1 / num2
    op.element.classList.remove("alert-primary")
    op.element.classList.add("alert-success")
    op.write(operacao)  
    

def limpar(*args, **kwargs):
    num1 = int(number1.value)
    num2 = int(number2.value)
    if num1 == '' or num2 == '':
        pass
    else:
        op.write('0')
        op.element.classList.remove("alert-success")
        op.element.classList.add("alert-primary")
        number1.clear()
        number2.clear()