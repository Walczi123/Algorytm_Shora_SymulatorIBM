import ipywidgets as widgets
from algorithms.shor import *
from IPython.display import display, Markdown, clear_output

factoring_number = widgets.IntText(
    value=15,
    description='Type number for factoring:')

timeout = widgets.IntText(
    value=0,
    description='Type the timeout value:')

button = widgets.Button(description="Start Shor's algorithm")
output = widgets.Output()


def on_button_clicked(_):
    with output:
        clear_output()
        display(Markdown(f"Factoring for: {factoring_number.value} (timeout: {timeout.value})"))

        factor_list1 = find_factor(factoring_number.value, a=7, qubits_count=8, timeout = timeout.value)
        factor_list2 = find_factor(factoring_number.value, a=7, qubits_count=8, timeout = timeout.value)
        if len(factor_list1) == 0:
            display(Markdown(f"TIMEOUT: no factor found for the first run"))
        else:
            display(Markdown(f"Found factors first run: {factor_list1}"))
        if len(factor_list2) == 0:
            display(Markdown(f"TIMEOUT: no factor found for the second run"))
        else:
            display(Markdown(f"Found factors second run: {factor_list2}"))


button.on_click(on_button_clicked)


vbox = widgets.VBox([factoring_number, timeout, button, output])

info = Markdown("""# Shor's algorithm
- Write positive number""")


def start_gui():
    display(info, vbox)
