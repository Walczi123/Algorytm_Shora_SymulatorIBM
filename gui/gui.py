import ipywidgets as widgets
from IPython.display import display, Markdown, clear_output

factoring_number = widgets.IntText(
    value=15,
    description='Type number for factoring:')

button = widgets.Button(description="Start Shor's algorithm")
output = widgets.Output()


def on_button_clicked(_):
    with output:
        clear_output()
        display(Markdown(f"Factoring for: {factoring_number.value}"))


button.on_click(on_button_clicked)


vbox = widgets.VBox([factoring_number, button, output])

info = Markdown("""# Shor's algorithm
- Write positive number""")


def start_gui():
    display(info, vbox)
