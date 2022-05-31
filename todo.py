from js import console
input_tarefa = Element("input_tarefa")

output_tarefa = Element("output_tarefa")

todas_tarefas = []

def anotar(*args, **kwargs):
    tarefa = input_tarefa.element.value
    output_tarefa.element.innerHTML += f'{tarefa}'+'<br>'

def limpar(*args, **kwargs):
    output_tarefa.write('')
