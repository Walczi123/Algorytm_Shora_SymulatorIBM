import ipywidgets as widgets
from tests.tests import run_tests
from IPython.display import display, Markdown, clear_output


button = widgets.Button(description="Start tests")
output = widgets.Output()


def on_button_clicked(_):
    with output:
        clear_output()
        run_tests()

button.on_click(on_button_clicked)


vbox = widgets.VBox([ button, output])

info = Markdown("""# Shor's algorithm""")


def start_gui():
    display(info, vbox)
