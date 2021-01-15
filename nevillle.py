"""
    Finds an interpolated value using Neville's algorithm.
    Input
      x: input x's in a list of size n
      y: input y's in a list of size n
      x: the x value used for interpolation
    Output
      p[0]: the polynomial of degree n
    """

#Neville ALgorithm
def neville(Xdata, Ydata, x):
    n = len(Xdata)
    p = n*[0]
    for k in range(n):
        for i in range(n-k):
            if k == 0:
                p[i] = Ydata[i]
            else:
                p[i] = ((x-Xdata[i+k])*p[i]+ \
                        (Xdata[i]-x)*p[i+1])/ \
                        (Xdata[i]-Xdata[i+k])
    
    return p[0]

#UI part
X = [] 
Y = []
# number of elemetns as input 
ele_no = int(input("Enter number of elements : ")) 
  
# iterating till the range 
for i in range(0, ele_no): 
    fx = float(input("Enter value of x{} ".format(i+1)))   
    X.append(fx) # adding the element 
    fy = float(input("Enter value of y{} ".format(i+1)))   
    Y.append(fy) # adding the element 
      
print("X:{}\nY:{}".format(X,Y)) 
z = int(input("Enter the value of interpolation "))
print("Value of f({})=".format(z))
print(neville(X,Y,z))
