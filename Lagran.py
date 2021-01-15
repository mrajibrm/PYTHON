# Python3 program for implementation 
# of Lagrange's Interpolation 
  
# To represent a data point corresponding to x and y = f(x) 
class Data: 
    def __init__(self, x, y): 
        self.x = x 
        self.y = y 
  
# function to interpolate the given data points using Lagrange's formula 
# xi -> corresponds to the new data point, whose value is to be obtained 
# n -> represents the number of known data points 
def interpolate(f: list, xi: int, n: int) -> float: 
  
    # Initialize result 
    result = 0.0
    for i in range(n): 
  
        # Compute individual terms of above formula 
        term = f[i].y 
        for j in range(n): 
            if j != i: 
                term = term * (xi - f[j].x) / (f[i].x - f[j].x) 
  
        # Add current term to result 
        result += term 
  
    return result 
  
# Driver Code 
if __name__ == "__main__": 
  
    # creating an array of 3 known data points 
    f = [Data(-1.2, -5.76), Data(0.3, -5.61), Data(1.1, -3.69)] 
  
    # Using the interpolate function to obtain a data point 
    # corresponding to x=3 
    print("Value of f(0) is :", interpolate(f, 0, 3)) 
