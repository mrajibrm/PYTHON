import random
import matplotlib.pyplot as plt
import math
import numpy as np
import matplotlib.patches as mpatches

# Problem 1.4
# In Exercise 1.4, we use an artificial data set to study the perceptron
# learning algorithm. This problem leads you to explore the algorithm further
# with data sets of different sizes and dimensions.


def generate_dataset(n):

  
# split the points randomly to either the +1 class or the -1 class

    pos1 = n - random.randrange(1, n)
    neg1 = n - pos1
  
# randomly generate slope and y-intercept for line
    m = round(random.uniform(-1,1), 1)
    b = round(random.uniform(-5,5), 1)
  
# set min and max x and y values for the points
    min_val = -20
    max_val = 20
  
# generate x values above and below f(x)
    x1 = [random.randrange(min_val, max_val) for i in range(pos1)]
    x2 = [random.randrange(min_val, max_val) for i in range(neg1)]
  
# generate y values above and below f(x)
    y1 = [random.randrange(math.floor(m*x+b)+min_val, math.floor(m*x+b)) for \
    x in x1]
    y2 = [random.randrange(math.ceil(m*x+b), max_val+math.floor(m*x+b)) for x \
        in x2]
  
    return min_val, max_val, m, b, x1, x2, y1, y2, pos1, neg1

def plot_fx(min_val, max_val, m, b):

    """ Plots the f(x) line and axes labels.
"""
# plot f(x) line
    plt.plot(np.arange(min_val, max_val), m*np.arange(min_val, max_val) + \
    b, color='green')
  
# axes labels
    plt.xlabel('X axis')
    plt.ylabel('Y axis')

def plot_points(x1, x2, y1, y2):
    """ Plots the generated points, sorted into the +1 and -1 classes.
"""
    plt.scatter(x1, y1, c='red') # +1 points
    plt.scatter(x2, y2, c='blue') # -1 points

def combine_data(pos1, neg1, x1, x2, y1, y2):
    """ Combines the dummy point (x[0]), x and y values, and group value into
an array.
"""
    d = [] # create empty set to put datapoint values
    for i in range(0, pos1):
        d.append([1, x1[i], y1[i], 1]) # append all +1 datapoints
    for j in range(0, neg1):
        d.append([1, x2[j], y2[j], -1]) # append all -1 datapoints
    return d;

def perceptron_calc(w, x):
    """ Calculates the cross product of the x-values and the corresponding
weights.
"""
    return w[0]*x[0] + w[1]*x[1] + w[2]*x[2]

def sign(x):
    """ Gives sign of value
"""
    return 1 if x>=0 else -1
def update_rule(w, d):
    """ Updates the weights according to the perceptron linear algorithm.
"""
    w[0] += d[0] * d[3] # update dummy weight
    w[1] += d[1] * d[3] # update x value weight
    w[2] += d[2] * d[3] # update y value weight
    return [w[0], w[1], w[2]]
  
def plot_gx(weights, min_val, max_val):
  
    m_g = -weights[1]/weights[2] # calculate g(x) slope
    b_g = -weights[0]/weights[2] # calculate g(x) y-intercept
# plot h(x)
    plt.plot(np.arange(min_val, max_val), m_g*np.arange(min_val, max_val) + \
    b_g, color='yellow')

def perceptron_learning_algorithm(pos1, neg1, x1, x2, y1, y2, n, min_val, \
max_val, m, b):
  
    dataset = combine_data(pos1, neg1, x1, x2, y1, y2)
  
# set starting weight values and iteration count   
    weights = [0.0, 0.0, 0.0]
    count = 0
  
# classified is false until all points have been accurately classified
    classified = False
    while not classified:
        count += 1 # increment count every iteration
        data_count = 0 # increment count every datapoint
        random.shuffle(dataset) # shuffle to access different points
        for datapoint in dataset:
# check if sign of calculated classification is equal to actual
            if(sign(perceptron_calc(weights, datapoint)) != datapoint[3]):
# if not, update weights
                weights = update_rule(weights, datapoint)
            else:
                data_count += 1 # correct sign adds to total correct count
        if(data_count == n):
            classified = True # once all points are classified, set to True
  
# plot points, f(x), and g(x), and add legend
    plot_fx(minimum_val, maximum_val, slope, y_intercept)
    plot_points(x1, x2, y1, y2)
    plot_gx(weights, minimum_val, maximum_val)
    fx = mpatches.Patch(color='green', label='f(x)')
    gx = mpatches.Patch(color='yellow', label='g(x)')
    plt.legend(handles=[fx, gx])

    plt.show()
  
    return count

# a
minimum_val, maximum_val, slope, y_intercept, x1, x2, y1, y2, \
num_positive_points, num_negative_points = \
generate_dataset(20)
plot_fx(minimum_val, maximum_val, slope, y_intercept)
plot_points(x1, x2, y1, y2)
plt.show()

# b
count = perceptron_learning_algorithm(num_positive_points, \
num_negative_points, x1, x2, y1, y2, 20, \
minimum_val, maximum_val, slope, y_intercept)

print("Number of updates until convergence:", count)

# f is fairly close to g.

# c
minimum_val, maximum_val, slope, y_intercept, x1, x2, y1, y2, \
num_positive_points, num_negative_points = \
generate_dataset(20)
perceptron_learning_algorithm(num_positive_points, num_negative_points, x1, \
x2, y1, y2, 20, minimum_val, maximum_val, \
slope, y_intercept)

# d
minimum_val, maximum_val, slope, y_intercept, x1, x2, y1, y2, \
num_positive_points, num_negative_points = \
generate_dataset(100)
perceptron_learning_algorithm(num_positive_points, num_negative_points, x1, \
x2, y1, y2, 100, minimum_val, maximum_val, \
slope, y_intercept)

#e.
minimum_val, maximum_val, slope, y_intercept, x1, x2, y1, y2, \
num_positive_points, num_negative_points = \
generate_dataset(1000)
perceptron_learning_algorithm(num_positive_points, num_negative_points, x1, \
x2, y1, y2, 1000, minimum_val, maximum_val, \
slope, y_intercept)

# f is almost inseperable from g, and it look quite a bit longer in terms of
# updates for the algorithm to converge.