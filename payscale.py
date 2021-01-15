def work_hour():
    work_hour = int(input("Please enter the time(in) hour you have worked:"))
    if 0 <= work_hour <= 40:
        print("You have worked for {} hour".format(work_hour))
    return work_hour

def Calculate_sal(work_hour):
    rate = float(input("Enter your pay rate(in dollar) : $"))
    if 7.50 <= rate <=18.25 and round(rate,2) == rate:
       print("Your pay rate is ${} /hour".format(rate)) 
    else:
        print("Invalid Input")
        quit()  
    gross_pay = work_hour * rate

    print("Your Gross Pay: ${:.2f}".format(gross_pay))

