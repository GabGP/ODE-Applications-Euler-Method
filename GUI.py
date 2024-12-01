import dearpygui.dearpygui as dpg

"""
TODO:
- INPUT:
    - Stepsize h
    - Initial Value (x0, y0)
    - Value to Calculate x

- OUTPUT:
    - Solution of the Euler Method
    - Solution of the improved Euler Method
    - Plotting of the Exact Solution and Aproximate Solution
    - Table Error per Iteration (Absolute and Relative Error)
"""

dpg.create_context()
dpg.create_viewport(title="ODE Applications: Euler Method", width=800, height=600, resizable=False)

# Creates the menu bar of the viewpoint
with dpg.viewport_menu_bar():
    with dpg.menu(label="Help"):
        dpg.add_menu_item(label="Open README.md") #TODO: open the README

# Creates a the main window
with dpg.window(tag="main_window", menubar=True):
    dpg.add_text("Euler Method")
    dpg.add_separator()

    dpg.add_text("Equation")

    # Creates a group to add a label to the left of the input box
    with dpg.group(horizontal=True):
        dpg.add_text("y\'=")
        dpg.add_input_text(tag="equation_input", hint="Type a First-Order Equation to Solve...")

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("main_window", True)
dpg.start_dearpygui()
dpg.destroy_context()