import math as math

## 
# Ordinary Differential Equation
#
class ODE:
    fourDecimals = "{:.4f}"

    # Result of the euler method
    approx_xAxis = []
    approx_yAxis = []

    # Result of the improved euler method
    improved_approx_xAxis = []
    improved_approx_yAxis = []

    # Result of the exact solution
    exact_xAxis = []
    exact_yAxis = []

    # Result of the absolute error
    absError = []
    improved_absError = []

    # Result of the relative error
    relError = []
    improved_relError = []

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


    def improvedEulerMethod(selectedEquation, x0: float, y0: float, x: float, stepSize: float):
        # formats the arguments to 4 decimals before using them
        x0 = float(ODE.fourDecimals.format(x0))
        y0 = float(ODE.fourDecimals.format(y0))
        x = float(ODE.fourDecimals.format(x))
        stepSize = float(ODE.fourDecimals.format(stepSize))

        # Resets the axis
        ODE.improved_approx_xAxis.clear()
        ODE.improved_approx_yAxis.clear()

        if ((x >= 0.01) and (stepSize >= 0.01)):

            # Initial Values (Step 0)
            ODE.improved_approx_xAxis.append(x0)
            ODE.improved_approx_yAxis.append(y0)
            x0 = float(ODE.fourDecimals.format(x0 + stepSize)) # Next step

            while (x0 <= x): # Do while initial value of x is less or equal than the goal x
                k1 = ODE.function(selectedEquation, x0, y0)
                k2 = ODE.function(selectedEquation, x0 + stepSize, y0 + stepSize * k1)
                y = y0 + (stepSize / 2) * (k1 + k2)

                ODE.improved_approx_xAxis.append(x0)
                ODE.improved_approx_yAxis.append(y)

                y0 = y
                x0 = float(ODE.fourDecimals.format(x0 + stepSize)) # Always format to 4 decimals


    def exactSolution(selectedEquation, x0: float, y0: float, x: float, stepSize: float):
        # formats the arguments to 4 decimals before using them
        x0 = float(ODE.fourDecimals.format(x0))
        y0 = float(ODE.fourDecimals.format(y0))
        x = float(ODE.fourDecimals.format(x))
        stepSize = float(ODE.fourDecimals.format(stepSize))
        
        # Resets the axis
        ODE.exact_xAxis.clear()
        ODE.exact_yAxis.clear()

        if ((x >= 0.01) and (stepSize >= 0.01)):

            x_n = x0
            while (x_n <= x): # Do while initial value of x is less or equal than the goal x
                y = ODE.exactFunction(selectedEquation, x0, y0, x_n)

                ODE.exact_xAxis.append(x_n)
                ODE.exact_yAxis.append(y)

                x_n = float(ODE.fourDecimals.format(x_n + stepSize)) # Always format to 4 decimals
            

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
            
            
    def exactFunction(selectedEquation, x0: float, y0: float, x: float): # TODO:

        match selectedEquation:
            case "e^(2y)":
                c = - x0 - 1 / (2 * math.exp(2 * y0))
                return -1/2 * math.log( abs(2 * (c - x)) )
            
            case "(x + y - 5)²":
                c = math.atan(y0 + x0 - 5) - x0
                return math.tan(x + c)
            
            case "0.9y - 1.8y²":
                c = (math.log(abs(y0 / (2 * y0 - 1))) / 9) - (x0 / 10)
                print(c)
                return (1 / (2 * c * math.exp(0.9 * x) - 2)) + 1/2
            
            case "2xy":
                c = y0 / math.exp( math.pow(x0, 2) )
                return c * math.exp( math.pow(x, 2) )
            
            case "1 + y²":
                c = math.atan(y0) - x0
                return math.tan(x + c)
            
            case "xy + sqrt(y)":
                u = (-x0 * math.pow(y0, 1/2))
                c = u / math.exp((1/4) * x0 * x0)
                return math.pow((c * math.exp((1/4) * x * x))/x, 2)     
            
    def absoluteError():

        # Resets the columns
        ODE.absError.clear()
        ODE.improved_absError.clear()

        for rowNumber in range(len(ODE.approx_yAxis)):
            # absolute error = |approximate value - exact value|
            result = abs(ODE.approx_yAxis[rowNumber] - ODE.exact_yAxis[rowNumber])
            ODE.absError.append(result)

            improvedResult = abs(ODE.improved_approx_yAxis[rowNumber] - ODE.exact_yAxis[rowNumber])
            ODE.improved_absError.append(improvedResult)
    
    def relativeError():

        # Resets the columns
        ODE.relError.clear()
        ODE.improved_relError.clear()

        for rowNumber in range(len(ODE.approx_yAxis)):

            if (float(ODE.fourDecimals.format(ODE.exact_yAxis[rowNumber])) != 0.000): # Avoids div by zero error
                # relative error = |absolute error / exact value| * 100%
                result = abs(ODE.approx_yAxis[rowNumber] - ODE.exact_yAxis[rowNumber] / ODE.exact_yAxis[rowNumber]) * 100
                ODE.relError.append(result)

                improvedResult = abs((ODE.improved_approx_yAxis[rowNumber] - ODE.exact_yAxis[rowNumber]) / ODE.exact_yAxis[rowNumber]) * 100
                ODE.improved_relError.append(improvedResult)
            else: 
                ODE.relError.append(0)
                ODE.improved_relError.append(0)
            