
## 
# Ordinary Differential Equation
#
class ODE:
    fourDecimals = "{:.4f}"
    
    def eulerMethod(y0: float, x: float, stepSize: float):

        if ((x > 0) and (stepSize > 0)):

            n = stepSize
            while (n < x + stepSize):
                y = y0 + stepSize * y0
                print(ODE.fourDecimals.format(y))

                y0 = y
                n = n + stepSize


    def improvedEulerMethod():
        1