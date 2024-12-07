import math as math
import numpy as np
from scipy.integrate import odeint

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

    # Result of the exact solution (NumPy Arrays)
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
        ODE.exact_xAxis = []
        ODE.exact_yAxis = []

        if ((x >= 0.01) and (stepSize >= 0.01)):

            # Creating an array from x to x + stepSize with a stepsize "stepSize"
            t = np.arange(start=x0, stop=(x + stepSize), step=stepSize)

            match selectedEquation:
                case "e^(2y)":
                    ODE.exact_yAxis = odeint(ODE.equation1, y0, t)
                    print(ODE.exact_yAxis.tolist())
                
                case "(x + y - 5)²":
                    ODE.exact_yAxis = odeint(ODE.equation2, y0, t)
                
                case "0.9y - 1.8y²":
                    ODE.exact_yAxis = odeint(ODE.equation3, y0, t)
                
                case "2xy":
                    ODE.exact_yAxis = odeint(ODE.equation4, y0, t)
                
                case "1 + y²":
                    ODE.exact_yAxis = odeint(ODE.equation5, y0, t)
                
                case "xy + sqrt(y)":
                    ODE.exact_yAxis = odeint(ODE.equation6, y0, t)       
            
            
    def absoluteError():

        # Resets the columns
        ODE.absError.clear()
        ODE.improved_absError.clear()

        for rowNumber in range(len(ODE.approx_yAxis)):
            # absolute error = |approximate value - exact value|
            result = abs(ODE.approx_yAxis[rowNumber] - ODE.exact_yAxis[rowNumber, 0])
            ODE.absError.append(result)

            improvedResult = abs(ODE.improved_approx_yAxis[rowNumber] - ODE.exact_yAxis[rowNumber, 0])
            ODE.improved_absError.append(improvedResult)
    
    def relativeError():

        # Resets the columns
        ODE.relError.clear()
        ODE.improved_relError.clear()

        for rowNumber in range(len(ODE.approx_yAxis)):

            if (float(ODE.fourDecimals.format(ODE.exact_yAxis[rowNumber, 0])) != 0.000): # Avoids div by zero error
                # relative error = |absolute error / exact value| * 100%
                result = abs((ODE.approx_yAxis[rowNumber] - ODE.exact_yAxis[rowNumber, 0]) / ODE.exact_yAxis[rowNumber, 0]) * 100
                ODE.relError.append(result)

                improvedResult = abs((ODE.improved_approx_yAxis[rowNumber] - ODE.exact_yAxis[rowNumber, 0]) / ODE.exact_yAxis[rowNumber, 0]) * 100
                ODE.improved_relError.append(improvedResult)
            else: 
                ODE.relError.append(0)
                ODE.improved_relError.append(0)


    ##
    # Equations
    #
    
    def function(selectedEquation, x: float, y: float):

        match selectedEquation:
            case "e^(2y)":
                return math.exp(2 * y)
            
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
            
    def equation1(y, x):
        return math.exp(2 * y)
    
    def equation2(y, x):
        return math.pow((x + y - 5), 2)
    
    def equation3(y, x):
        return 0.9 * y - 1.8 * math.pow(y, 2)
    
    def equation4(y, x):
        return 2 * x * y
    
    def equation5(y, x):
        return 1 + math.pow(y, 2)
    
    def equation6(y, x):
        return x * y + math.sqrt(y) 
            