import math as math

## 
# Ordinary Differential Equation
#
class ODE:
    fourDecimals = "{:.4f}"

    approx_xAxis = []
    approx_yAxis = []

    improved_approx_xAxis = []
    improved_approx_yAxis = []

    exact_xAxis = []
    exact_yAxis = []

    def eulerMethod(selectedEquation, x0: float, y0: float, x: float, stepSize: float):

        # formats the arguments to 4 decimals before using them
        x0 = float(ODE.fourDecimals.format(x0))
        y0 = float(ODE.fourDecimals.format(y0))
        x = float(ODE.fourDecimals.format(x))
        stepSize = float(ODE.fourDecimals.format(stepSize))

        # Resets the axis
        ODE.approx_xAxis.clear()
        ODE.approx_yAxis.clear()

        if ((x >= 0.01) and (stepSize >= 0.01)):

            # Initial Values (Step 0)
            ODE.approx_xAxis.append(x0)
            ODE.approx_yAxis.append(y0)
            x0 = float(ODE.fourDecimals.format(x0 + stepSize)) # Next step

            while (x0 <= x): # Do while initial value of x is less or equal than the goal x
                y = y0 + ODE.function(selectedEquation, x0, y0) * stepSize
                y = float(ODE.fourDecimals.format(y)) # Always format to 4 decimals

                ODE.approx_xAxis.append(x0)
                ODE.approx_yAxis.append(y)

                y0 = y
                x0 = float(ODE.fourDecimals.format(x0 + stepSize)) # Always format to 4 decimals

                print(y0)


    def improvedEulerMethod(x0: float, y0: float, x: float, stepSize: float):
        # formats the arguments to 4 decimals before using them
        x0 = float(ODE.fourDecimals.format(x0))
        y0 = float(ODE.fourDecimals.format(y0))
        x = float(ODE.fourDecimals.format(x))
        stepSize = float(ODE.fourDecimals.format(stepSize))

        # Resets the axis
        ODE.improved_approx_xAxis.clear()
        ODE.improved_approx_yAxis.clear()

        if ((x >= 0.5) and (stepSize >= 0.05)):

            while (x0 <= x): # Do while initial value of x is less or equal than the goal x
                # Here goes the improved euler method

                ODE.improved_approx_xAxis.append(x0)
                ODE.improved_approx_yAxis.append(y)

                y0 = y
                x0 = x0 + stepSize


    def exactSolution(selectedEquation, x0: float, x: float, stepSize: float):
        # formats the arguments to 4 decimals before using them
        x0 = float(ODE.fourDecimals.format(x0))
        x = float(ODE.fourDecimals.format(x))
        stepSize = float(ODE.fourDecimals.format(stepSize))

        # Resets the axis
        ODE.exact_xAxis.clear()
        ODE.exact_yAxis.clear()

        if ((x >= 0.01) and (stepSize >= 0.01)):

            while (x0 <= x): # Do while initial value of x is less or equal than the goal x
                y = ODE.exactFunction(selectedEquation, x)

                ODE.exact_xAxis.append(x0)
                ODE.exact_yAxis.append(y)

                x0 = float(ODE.fourDecimals.format(x0 + stepSize)) # Always format to 4 decimals
            

    def function(selectedEquation, x: float, y: float):

        match selectedEquation:
            case "e^(2y)":
                return math.exp(y)
            
            case "(x + y - 5)²":
                return math.pow((x + y - 5), 2)
            
            case "0.9y - 1.8y²":
                return 0.9 * y - 1.8 * math.pow(y, 2)
            
            case "2xy":
                return 2 * x * y
            
            case "1 + y²":
                return 1 + math.pow(y, 2)
            
            case "xy + sqrt(y)":
                return x * y + math.sqrt(y)     
            
            
    def exactFunction(selectedEquation, x: float): # TODO:

        match selectedEquation:
            case "e^(2y)":
                return 1
            
            case "(x + y - 5)²":
                return 1
            
            case "0.9y - 1.8y²":
                return 1
            
            case "2xy":
                return 1
            
            case "1 + y²":
                return 1
            
            case "xy + sqrt(y)":
                return 1     