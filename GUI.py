import dearpygui.dearpygui as dpg
from ODE import *

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

class GUI:
    def mainWindow():
        dpg.create_context()
        dpg.create_viewport(title="ODE Applications: Euler Method", width=1280, height=720, resizable=False)

        # Creates the menu bar of the viewpoint
        with dpg.viewport_menu_bar():
            with dpg.menu(label="File"):
                dpg.add_menu_item(label="Export Table as .CSV") #TODO: export table as .csv

            with dpg.menu(label="Help"):
                dpg.add_menu_item(label="Open README.md") #TODO: open the README

        # Creates the main window
        with dpg.window(tag="main_window", menubar=True):
            dpg.add_text("Euler Method")
            dpg.add_separator()

            # Using table as layout
            with dpg.table(header_row=False, borders_innerV=True, policy=dpg.mvTable_SizingStretchProp):

                dpg.add_table_column()
                dpg.add_table_column()

                with dpg.table_row(height=658):
                    with dpg.table_cell(): # Left Column
                        GUI.inputSection()

                    with dpg.table_cell(): # Right Column

                        with dpg.table(header_row=False):

                            dpg.add_table_column()

                            with dpg.table_row(): # Upper-Right Row
                                with dpg.table_cell(): 
                                    GUI.solutionTable()

                            with dpg.table_row(): # Down-Right Row
                                with dpg.table_cell(): 
                                    GUI.solutionGraph()

        dpg.setup_dearpygui()
        dpg.show_viewport()
        dpg.set_primary_window("main_window", True)
        dpg.start_dearpygui()
        dpg.destroy_context()


    def inputSection():    
        with dpg.group():
            
            # Adds the Initial Values section
            dpg.add_text("Initial Values: ", indent=40)
            with dpg.group(horizontal=True):
                dpg.add_text("x0=")
                dpg.add_input_float(step=0.5, width=100)

            with dpg.group(horizontal=True):
                dpg.add_text("y0=")
                dpg.add_input_float(step=0.5, width=100)

            dpg.add_text() # Adds whitespace

            # Adds the Stepsize section
            dpg.add_text("Stepsize: ", indent=40)
            with dpg.group(horizontal=True):
                dpg.add_text(" h=")
                dpg.add_input_float(step=0.05, width=100)

            dpg.add_text() # Adds whitespace

            # Adds the Solve for y(x) section
            dpg.add_text("Solve for y(x): ", indent=40)
            with dpg.group(horizontal=True):
                dpg.add_text(" x=")
                dpg.add_input_float(step=0.5, width=100)

            dpg.add_text() # Adds whitespace

            # Adds the Equation section
            dpg.add_text("Equation: ", indent=40)
            with dpg.group(horizontal=True):
                dpg.add_text("y\'=")
                dpg.add_input_text(hint="Type a First-Order ODE to Solve...", width=300)

            dpg.add_button(label="Solve", indent=286, callback=GUI.solve) #TODO: Add action to the button


    def solutionTable():
        with dpg.table(borders_outerH=True, borders_innerV=True, borders_innerH=True, borders_outerV=True,
                       height=156, scrollY=True, freeze_rows=1):

            dpg.add_table_column(label="x_n")
            dpg.add_table_column(label="Euler Method")
            dpg.add_table_column(label="Improved Euler Method")
            dpg.add_table_column(label="Absolute Error")
            dpg.add_table_column(label="Relative Error")

            # Placeholder content
            for i in range(0, 10):
                with dpg.table_row():
                    for j in range(0, 5):
                        with dpg.table_cell():
                            dpg.add_text()

    def solutionGraph():
        with dpg.plot(label="y(x) vs. x", height=490, width=928):

            dpg.add_plot_axis(dpg.mvXAxis, label="x", auto_fit=True)
            dpg.add_plot_axis(dpg.mvYAxis, label="y(x)", auto_fit=True, tag="y_axis")

    def solve():
        print("Clicked \"Solve\"")
        ODE.eulerMethod(x0=0, y0=1, x=4, stepSize=1)

GUI.mainWindow()