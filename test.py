def testing(num):
    if (num > 50):
        return(num - 2)
    return testing(testing(num + 10))
print(testing(30))