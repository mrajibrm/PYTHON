import tkinter as tk

check = tk.Tk()
check.geometry("400x200")  # Size of the window
check.title("Check Inventory")  # Adding a title

l3 = tk.Label(check,  text='Make', width=15 )
l3.grid(row=2,column=1)
l3 = tk.Label(check,  text='Model', width=15 )
l3.grid(row=4,column=1)
l3 = tk.Label(check,  text='Year', width=15 )
l3.grid(row=6,column=1)

make_list = ["Ford", "Mercedes-Benz", "Nissan", "BMW", "Honda"]
car_makes = tk.StringVar(check)
car_makes.set(make_list[1])  # default value
om1 = tk.OptionMenu(check, car_makes, *make_list)
om1.grid(row=2, column=2)

str_out=tk.StringVar(check)
str_out.set("Model")
l2 = tk.Label(check,  textvariable=str_out, width=10 )
l2.grid(row=2,column=4)

def my_show(*args):
    str_out.set(car_makes.get())
    if car_makes.get() in 'Ford':
        my_list1 = ["Explorer----------", "Escape", "F150", "F250", "F350", "F450", "F550", "Focus", "Fusion", "Mustang"]
        options1 = tk.StringVar(check)
        options1.set(my_list1[1])  # default value
        om2 = tk.OptionMenu(check, options1, *my_list1)
        om2.grid(row=4, column=2)
    elif car_makes.get() in 'BMW':
        my_list2 = ["1 Series", "2 Series", "3 Series", "4 Series", "5 Series", "6 Series", "7 Series", "8 Series"]
        options2 = tk.StringVar(check)
        options2.set(my_list2[1])  # default value
        om2 = tk.OptionMenu(check, options2, *my_list2)
        om2.grid(row=4, column=2)
car_makes.trace('w',my_show)

check.mainloop()