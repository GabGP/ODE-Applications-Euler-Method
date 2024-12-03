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
    radioButton: str
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

        GUI.layout()

        dpg.setup_dearpygui()
        dpg.show_viewport()
        dpg.set_primary_window("main_window", True)
        dpg.start_dearpygui()
        dpg.destroy_context()


    def layout():
        # Using table as layout
        with dpg.table(header_row=False, borders_innerV=True, policy=dpg.mvTable_SizingStretchProp, parent="main_window"):

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


    def inputSection():    
        with dpg.group():
            
            # Adds the Initial Values section
            dpg.add_text("Initial Values: ", indent=40)
            with dpg.group(horizontal=True):
                dpg.add_text("x0=")
                GUI.initX = dpg.add_input_float(step=0.5, width=100, format="%.4f", min_clamped=True, min_value=0.0000)

            with dpg.group(horizontal=True):
                dpg.add_text("y0=")
                GUI.initY = dpg.add_input_float(step=0.5, width=100, format="%.4f", min_clamped=True, min_value=0.0000)

            dpg.add_text() # Adds whitespace

            # Adds the Stepsize section
            dpg.add_text("Stepsize: ", indent=40)
            with dpg.group(horizontal=True):
                dpg.add_text(" h=")
                GUI.stepSize = dpg.add_input_float(step=0.05, width=100, format="%.4f", min_clamped=True, min_value=0.0000)

            dpg.add_text() # Adds whitespace

            # Adds the Solve for y(x) section
            dpg.add_text("Solve for y(x): ", indent=40)
            with dpg.group(horizontal=True):
                dpg.add_text(" x=")
                GUI.goalX = dpg.add_input_float(step=0.5, width=100, format="%.4f", min_clamped=True, min_value=0.0000)

            dpg.add_text() # Adds whitespace

            # Select Method section
            with dpg.group(horizontal=True):
                GUI.radioButton = dpg.add_radio_button(["Euler Method", "Improved Euler Method"], callback=GUI.radioButtonAction, 
                                                       default_value="Euler Method")

            dpg.add_text() # Adds whitespace

            # Adds the Equation Selection section
            dpg.add_text("Select a First-Order ODE to Solve...", indent=40)
            with dpg.group(horizontal=True):
                dpg.add_text("y\'=")                
                GUI.selectedEquation = dpg.add_combo(items=GUI.equations, width=300)

            dpg.add_button(label="Solve", indent=286, callback=GUI.solveButton)


    def solutionTable():
        # Creates the solution table
        with dpg.table(borders_outerH=True, borders_innerV=True, borders_innerH=True, borders_outerV=True,
                       height=156, scrollY=True, freeze_rows=1, tag="solution_table"):

            dpg.add_table_column(label="x", tag="column1")
            dpg.add_table_column(label="y (Exact Solution)", tag="column2")
            dpg.add_table_column(label="y (Euler Method)", tag="column3")
            dpg.add_table_column(label="Absolute Error", tag="column4")
            dpg.add_table_column(label="Relative Error", tag="column5")


    def clearTable():
        # Clearing table
        for i in range(0, GUI.rowAmmount):
            dpg.delete_item(f"row{i}")


    def updateTable():
        # Always clear the table before updating it
        GUI.clearTable()

        # Updating table
        GUI.rowAmmount = len(ODE.approx_xAxis)
        for rowNumber in range(0, GUI.rowAmmount):
            with dpg.table_row(tag=f"row{rowNumber}", parent="solution_table"):

                # Column: x
                with dpg.table_cell():
                        dpg.add_text(ODE.fourDecimals.format(ODE.approx_xAxis[rowNumber]))

                # Column: Exact Solution
                with dpg.table_cell():
                    dpg.add_text("Exact Solution") # Placeholder
                
                # Column: Euler Method/Improved Euler Method
                with dpg.table_cell():
                        if (dpg.get_value(GUI.radioButton) == "Euler Method"):
                            dpg.add_text(ODE.fourDecimals.format(ODE.approx_yAxis[rowNumber]))
                        else:
                            dpg.add_text("Improved Euler Method") # Placeholder

                # Column: Absolute Error
                with dpg.table_cell():
                        if (dpg.get_value(GUI.radioButton) == "Euler Method"):
                            dpg.add_text("Euler Method") # Placeholder
                        else:
                            dpg.add_text("Improved Euler Method") # Placeholder

                # Column: Relative Error
                with dpg.table_cell():
                        if (dpg.get_value(GUI.radioButton) == "Euler Method"):
                            dpg.add_text("Euler Method") # Placeholder
                        else:
                            dpg.add_text("Improved Euler Method") # Placeholder


    def solutionGraph():
        # creates the solution graph
        with dpg.plot(label="y(x) vs. x", height=490, width=928):

            dpg.add_plot_legend()

            dpg.add_plot_axis(dpg.mvXAxis, label="x", auto_fit=True)
            dpg.add_plot_axis(dpg.mvYAxis, label="y(x)", auto_fit=True, tag="y_axis")

            dpg.add_line_series(ODE.exact_xAxis, ODE.exact_yAxis, label="Exact Solution", parent="y_axis", tag="exact_graph")
            dpg.add_line_series(ODE.approx_xAxis, ODE.approx_yAxis, label="Approximate Solution", parent="y_axis", tag="approx_graph")


    def updateGraph():
        dpg.set_value("approx_graph", [ODE.approx_xAxis, ODE.approx_yAxis])
        dpg.set_value("exact_graph", [ODE.exact_xAxis, ODE.exact_yAxis])


    def radioButtonAction():
        print(f"Radio Button Action: {dpg.get_value(GUI.radioButton)}") # TODO: Remove at the end

        match dpg.get_value(GUI.radioButton):

            #if the radio button selection matches the case, then does what's in there
            case "Euler Method":
                GUI.clearTable()
                dpg.configure_item("column3", label="y (Euler Method)") # Changes the name of the third column
                GUI.updateTable()
                GUI.updateGraph()
            
            case "Improved Euler Method":
                GUI.clearTable()
                dpg.configure_item("column3", label="y (Improved Euler Method)") # Changes the name of the third column
                GUI.updateTable()
                GUI.updateGraph()
            
    
    def solveButton():
        print("Clicked \"Solve\"\n") # TODO: Remove at the end
        print(dpg.get_value(GUI.radioButton))

        # Checks if there's a selected equation
        if (dpg.get_value(GUI.selectedEquation) != ""):
            ODE.eulerMethod(x0=dpg.get_value(GUI.initX), y0=dpg.get_value(GUI.initY), stepSize=dpg.get_value(GUI.stepSize), x=dpg.get_value(GUI.goalX))

            ODE.exactSolution(selectedEquation=dpg.get_value(GUI.selectedEquation), x0=dpg.get_value(GUI.initX), x=dpg.get_value(GUI.goalX), 
                                    stepSize=dpg.get_value(GUI.stepSize))
            
            GUI.updateGraph()
            GUI.updateTable()

        else:
            GUI.popupWindow("Select an Equation to Continue")


    def popupWindow(message: str):

        windowCenter = (len(message)/2)*6

        dpg.add_window(popup=True, modal=True, no_resize=True, no_title_bar=True, tag="popup_window")
        dpg.add_text(parent="popup_window")
        dpg.add_text(message, parent="popup_window")
        dpg.add_button(label="OK", indent=windowCenter, callback=lambda: dpg.delete_item("popup_window"), parent="popup_window")
        
        
GUI.mainWindow()