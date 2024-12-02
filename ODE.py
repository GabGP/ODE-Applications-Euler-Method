
## 
# Ordinary Differential Equation
#
class ODE:
    fourDecimals = "{:.4f}"
    approx_xAxis = []
    approx_yAxis = []
    exact_xAxis = []
    exact_yAxis = []

    def eulerMethod(x0: float, y0: float, x: float, stepSize: float):

        # Resets the axis
        ODE.approx_xAxis.clear()
        ODE.approx_yAxis.clear()

        if ((x > 0) and (stepSize > 0)):

            while (x0 <= x): # Do while initial value of x is less or equal than the goal x
                y = y0 + stepSize * y0

                ODE.approx_xAxis.append(float(ODE.fourDecimals.format(x0)))
                ODE.approx_yAxis.append(float(ODE.fourDecimals.format(y)))

                y0 = y
                x0 = x0 + stepSize


    def improvedEulerMethod():
        1

    def exactSolution(selectedEquation, x0: float, x: float, stepSize: float):

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
            
            case _:
                return print("Select an Equation to Continue")
            