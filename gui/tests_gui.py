import ipywidgets as widgets
from algorithms.shor import *
from IPython.display import display, Markdown, clear_output
from cirq_modules.cirq_shor import find_factor_cirq, naive_order_finder, quantum_order_finder
from tests.tests_stats import aggregate_resuls1, aggregate_resuls2

file_path = widgets.Text(
    value='./tests_results_local.csv',
    description='Type path to file with test results.')

separator = widgets.Text(
    value=',',
    description='Type the separator')

button = widgets.Button(description="Show results")
output = widgets.Output()


def on_button_clicked(_):
    with output:
        clear_output()
        df1 = aggregate_resuls1(file_path.value, separator.value)
        display(df1)
        df2 = aggregate_resuls2(file_path.value, separator.value)
        display(df2)


button.on_click(on_button_clicked)


vbox = widgets.VBox([file_path, separator, button, output])

info = Markdown("""# Show results of tests""")


def start_gui():
    display(info, vbox)
