
## 
# Ordinary Differential Equation
#
class ODE:
    
    def eulerMethod(x0: int, y0: int, x: int, stepSize: int):

        for n in range(stepSize, x + stepSize):
            y = y0 + stepSize * y0
            print(y)
            y0 = y


    def improvedEulerMethod():
        1