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
    initX: float # Initial X (x0)
    initY: float # Initial Y (y0)
    stepSize: float # Stepsize h
    goalX: float # X in y(x)
    equations = ["e^(2y)", "(x + y - 5)²", "0.9y - 1.8y²", "2xy", "1 + y²", "xy + sqrt(y)"]
    selectedEquation: str
    rowAmmount = 0

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
                GUI.initX = dpg.add_input_float(step=0.5, width=100)

            with dpg.group(horizontal=True):
                dpg.add_text("y0=")
                GUI.initY = dpg.add_input_float(step=0.5, width=100)

            dpg.add_text() # Adds whitespace

            # Adds the Stepsize section
            dpg.add_text("Stepsize: ", indent=40)
            with dpg.group(horizontal=True):
                dpg.add_text(" h=")
                GUI.stepSize = dpg.add_input_float(step=0.05, width=100)

            dpg.add_text() # Adds whitespace

            # Adds the Solve for y(x) section
            dpg.add_text("Solve for y(x): ", indent=40)
            with dpg.group(horizontal=True):
                dpg.add_text(" x=")
                GUI.goalX = dpg.add_input_float(step=0.5, width=100)

            dpg.add_text() # Adds whitespace

            # Adds the Equation Selection section
            dpg.add_text("Select a First-Order ODE to Solve...", indent=40)
            with dpg.group(horizontal=True):
                dpg.add_text("y\'=")                
                GUI.selectedEquation = dpg.add_combo(items=GUI.equations, width=300)

            dpg.add_button(label="Solve", indent=286, callback=GUI.solveButton)


    def solutionTable():
        with dpg.table(borders_outerH=True, borders_innerV=True, borders_innerH=True, borders_outerV=True,
                       height=156, scrollY=True, freeze_rows=1, tag="solution_table"):

            dpg.add_table_column(label="x_n", tag="column1")
            dpg.add_table_column(label="Euler Method", tag="column2")
            dpg.add_table_column(label="Improved Euler Method", tag="column3")
            dpg.add_table_column(label="Absolute Error", tag="column4")
            dpg.add_table_column(label="Relative Error", tag="column5")


    def solutionGraph():
        with dpg.plot(label="y(x) vs. x", height=490, width=928):

            dpg.add_plot_legend()

            dpg.add_plot_axis(dpg.mvXAxis, label="x", auto_fit=True)
            dpg.add_plot_axis(dpg.mvYAxis, label="y(x)", auto_fit=True, tag="y_axis")

            dpg.add_line_series(ODE.exact_xAxis, ODE.exact_yAxis, label="Exact Solution", parent="y_axis", tag="exact_graph")
            dpg.add_line_series(ODE.approx_xAxis, ODE.approx_yAxis, label="Approximate Solution", parent="y_axis", tag="approx_graph")


    def solveButton():
        print("Clicked \"Solve\"\n") # TODO: Remove at the end
        ODE.eulerMethod(x0=dpg.get_value(GUI.initX), y0=dpg.get_value(GUI.initY), stepSize=dpg.get_value(GUI.stepSize), x=dpg.get_value(GUI.goalX))
        dpg.set_value("approx_graph", [ODE.approx_xAxis, ODE.approx_yAxis])

        ODE.exactSolution(selectedEquation=dpg.get_value(GUI.selectedEquation), x0=dpg.get_value(GUI.initX), x=dpg.get_value(GUI.goalX), 
                          stepSize=dpg.get_value(GUI.stepSize))
        dpg.set_value("exact_graph", [ODE.exact_xAxis, ODE.exact_yAxis])

        # Clearing table
        for i in range(0, GUI.rowAmmount):
            dpg.delete_item(f"row{i}")

        GUI.rowAmmount = len(ODE.approx_xAxis)

        # Updating table
        for i in range(0, GUI.rowAmmount):
            with dpg.table_row(tag=f"row{i}", parent="solution_table"):
                for j in range(0, 5):
                    with dpg.table_cell():
                        dpg.add_text(ODE.fourDecimals.format(ODE.approx_xAxis[i])) # Placeholder

GUI.mainWindow()