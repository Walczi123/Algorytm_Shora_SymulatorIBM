import ipywidgets as widgets
from algorithms.shor import *
from IPython.display import display, Markdown, clear_output
from cirq_modules.cirq_shor import find_factor_cirq, naive_order_finder, quantum_order_finder
from commons.common import run_function

factoring_number = widgets.IntText(
    value=14,
    description='Type number for factoring:')

a_number = widgets.IntText(
    value=2,
    description='Type number for searching value:')

timeout = widgets.IntText(
    value=0,
    description='Type the timeout value:')

button = widgets.Button(description="Start Shor's algorithm")
output = widgets.Output()


def on_button_clicked(_):
    with output:
        clear_output()
        display(Markdown(
            f"Factoring for: {factoring_number.value} (timeout: {timeout.value})"))
        factor_list = run_function(
            find_factor_return1st, factoring_number.value, a_number.value, 8, True, timeout.value)
        display(
            Markdown(f"Algorithm uwing Qiskit founds: {factor_list}"))


button.on_click(on_button_clicked)


vbox1 = widgets.VBox([factoring_number, a_number, timeout, button, output])

info1 = Markdown("""# Shor's algorithm using Qiskit
- Write positive number""")

factoring_number2 = widgets.IntText(
    value=14,
    description='Type number for factoring:')

button2 = widgets.Button(description="Start Shor's algorithm")
output2 = widgets.Output()


def on_button_clicked2(_):
    with output2:
        clear_output()
        display(Markdown(
            f"Factoring for: {factoring_number2.value}"))
        factor_list = run_function(
            find_factor_cirq, factoring_number2.value, naive_order_finder, False)
        display(
            Markdown(f"Function using naive algorithm founds: {factor_list}"))


button2.on_click(on_button_clicked2)


vbox2 = widgets.VBox([factoring_number2, button2, output2])

info2 = Markdown("""# Function using naive algorithm
- Write positive number""")

factoring_number3 = widgets.IntText(
    value=14,
    description='Type number for factoring:')

button3 = widgets.Button(description="Start Shor's algorithm")
output3 = widgets.Output()


def on_button_clicked3(_):
    with output3:
        clear_output()
        display(Markdown(
            f"Factoring for: {factoring_number3.value}"))
        factor_list = run_function(
            find_factor_cirq, factoring_number3.value, quantum_order_finder, False)
        display(
            Markdown(f"Algorithm using Cirq founds: {factor_list}"))


button3.on_click(on_button_clicked3)


vbox3 = widgets.VBox([factoring_number3, button3, output3])

info3 = Markdown("""# Shor's algorithm using Cirq
- Write positive number""")


def start_gui():
    display(info1, vbox1)
    display(info2, vbox2)
    display(info3, vbox3)
