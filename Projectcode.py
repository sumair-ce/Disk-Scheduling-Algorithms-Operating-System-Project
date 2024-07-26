import customtkinter as ctk # type: ignore
import turtle
import matplotlib.pyplot as plt # type: ignore
from copy import copy

# Disk Scheduling Algorithms
def FCFS(request, start):
    sum = 0
    position = start
    order = []
    order.append(start)
    for i in request:
        sum += abs(i - position)
        position = i
        order.append(i)
    return order, sum

def SSTF(Request, Start):
    templist = copy(Request)
    position = Start
    Order = [position]
    Sum = 0
    while templist:
        closest = min(templist, key=lambda x: abs(x - position))
        Sum += abs(closest - position)
        position = closest
        Order.append(position)
        templist.remove(position)
    return Order, Sum

def SCAN(Request, Start):
    n = len(Request)
    Order = []
    Request_tmp = copy(Request)
    Request_tmp.sort()
    if Start != 0 and Start < Request_tmp[n - 1]:
        Request_tmp.append(0)
    p = len(Request_tmp)

    i = Start - 1
    Order.append(Start)
    while i >= 0:
        for j in range(0, p):
            if (Request_tmp[j] == i):
                Order.append(i)
        i -= 1

    k = Start + 1
    while k < 200:
        for l in range(0, n):
            if (Request[l] == k):
                Order.append(k)
        k += 1

    Sum = 0
    for p in range(0, len(Order) - 1):
        Sum += abs(Order[p] - Order[p + 1])
    return Order, Sum

def CSCAN(Request, Start):
    n = len(Request)
    Order = []
    Request_tmp = copy(Request)
    Request_tmp.sort()
    if Start != 0 and Start < Request_tmp[n - 1]:
        Request_tmp.append(0)
    p = len(Request_tmp)

    i = Start - 1
    Order.append(Start)
    while i >= 0:
        for j in range(0, p):
            if (Request_tmp[j] == i):
                Order.append(i)
        i -= 1

    k = 199
    while k > Start:
        if (k == 199):
            Order.append(k)
        for l in range(0, n):
            if (Request[l] == k):
                Order.append(k)
        k -= 1

    Sum = 0
    SortedReq = copy(Order)
    SortedReq.sort()
    for p in range(0, len(Order) - 1):
        if (Order[p] != SortedReq[0]):
            Sum += abs(Order[p] - Order[p + 1])
    return Order, Sum

def LOOK(Request, Start):
    n = len(Request)
    Order = []
    i = Start - 1
    Order.append(Start)
    while i > 0:
        for j in range(0, n):
            if (Request[j] == i):
                Order.append(i)
        i -= 1

    k = Start + 1
    while k < 200:
        for l in range(0, n):
            if (Request[l] == k):
                Order.append(k)
        k += 1

    Sum = 0
    for p in range(0, len(Order) - 1):
        Sum += abs(Order[p] - Order[p + 1])
    return Order, Sum

def CLOOK(Request, Start):
    n = len(Request)
    Order = []
    i = Start - 1
    Order.append(Start)
    while i > 0:
        for j in range(0, n):
            if (Request[j] == i):
                Order.append(i)
        i -= 1

    k = 199
    while k > Start:
        for l in range(0, n):
            if (Request[l] == k):
                Order.append(k)
        k -= 1

    Sum = 0
    SortedReq = copy(Order)
    SortedReq.sort()
    for p in range(0, len(Order) - 1):
        if (Order[p] != SortedReq[0]):
            Sum += abs(Order[p] - Order[p + 1])
    return Order, Sum

def plotChart(request_arr, start):
    plot_list = []
    algos = ["FCFS", "SSTF", "SCAN", "CSCAN", "LOOK", "CLOOK"]
    request = list(request_arr.split(" "))
    request = [int(i) for i in request]
    
    fcfs_order, fcfs_sum = FCFS(request, start)
    sstf_order, sstf_sum = SSTF(request, start)
    scan_order, scan_sum = SCAN(request, start)
    cscan_order, cscan_sum = CSCAN(request, start)
    look_order, look_sum = LOOK(request, start)
    clook_order, clook_sum = CLOOK(request, start)
    
    plot_list.extend([fcfs_sum, sstf_sum, scan_sum, cscan_sum, look_sum, clook_sum])
    

    try:
        fig, ax = plt.subplots()
        fig.patch.set_facecolor('#2e2e2e')
        ax.set_facecolor('#2e2e2e')
        
        ax.set_title('Total Head Movement Comparison Chart', fontsize=14, color='white')
        ax.tick_params(axis='x', colors='white')
        ax.tick_params(axis='y', colors='white')
        ax.spines['bottom'].set_color('white')
        ax.spines['top'].set_color("#2e2e2e")
        ax.spines['left'].set_color('white')
        ax.spines['right'].set_color("#2e2e2e")
        
        bars = plt.bar(algos, plot_list, color='#4a90e2')
        
        plt.show()
    except Exception as e:
        print("Error plotting graph:", e)

# Visualizing the disk scheduling
def plotGraph(option, request_arr, start, utime):
    request = list(request_arr.split(" "))
    request = [int(i) for i in request]
    if option == "FCFS":
        Order, Sum = FCFS(request, start)
    elif option == "SSTF":
        Order, Sum = SSTF(request, start)
    elif option == "SCAN":
        Order, Sum = SCAN(request, start)
    elif option == "CSCAN":
        Order, Sum = CSCAN(request, start)
    elif option == "LOOK":
        Order, Sum = LOOK(request, start)
    elif option == "CLOOK":
        Order, Sum = CLOOK(request, start)

    import time
    turtle.clearscreen()
    Disk = turtle.Screen()
    Disk.title(option)
    Disk.bgcolor("#2e2e2e")
    Disk.setworldcoordinates(-5, -20, 210, 10)
    head = turtle.Turtle()
    head.shape("circle")
    head.color("#ffffff")
    head.turtlesize(.4, .4, .125)
    head.speed(1)
    head.pensize(0.5)
    head.pencolor("#ffffff")

    head2 = turtle.Turtle()
    head2.shape("square")
    head2.color("#1f6aa5")
    head2.turtlesize(.5, .5, 1)
    head2.speed(4)
    head2.pensize(2)
    head2.pencolor("#1f6aa5")

    n = len(Order)
    y = -1
    y2 = 0
    temp_order = [int(i * 10) for i in range(0, 21)]
    for i in range(0, len(temp_order)):
        head2.goto(temp_order[i], y2)
        head2.stamp()
        if(temp_order[i]==200): head2.write(temp_order[i]-1, False, align="right", font=("Arial", 10, "normal"))
        else: head2.write(temp_order[i], False, align="right", font=("Arial", 10, "normal"))

    for i in range(0, n):
        if i == 0:
            head.penup()
            head.goto(Order[i], y)
            head.pendown()
            head.stamp()
            head.write(Order[i], False, align="right", font=("Arial", 12, "normal"))
        else:
            head.goto(Order[i], y - 1)
            head.stamp()
            head.write(Order[i], False, align="right", font=("Arial", 12, "normal"))
            y -= 1
    head.hideturtle()
    head.speed(0)
    head.penup()
    head.goto(100, 2)
    message1 = f"Disk Scheduling Algorithm: {option}"
    message2 = f"Total Head Movement: {Sum}"
    message3 = f"Time taken: {round(utime * Sum, 2)} Seconds"

    head.write(message1, False, align="center", font=("Arial", 14, "normal"))
    head.goto(100, 4)
    head.write(message2, False, align="center", font=("Arial", 14, "normal"))
    head.goto(100, 3)
    head.write(message3, False, align="center", font=("Arial", 14, "normal"))

    Disk.exitonclick()

# Main GUI function
def Main():
    ctk.set_appearance_mode("Dark")
    ctk.set_default_color_theme("blue")

    app = ctk.CTk()
    app.title("Disk Scheduling")
    app.geometry("550x450")
    app.resizable(False, False)

    def on_plotGraph():
        try:
            start = int(start_pos.get())
            utime = float(time_val.get())
            if start < 0 or utime < 0:
                raise ValueError("Negative values are not allowed")
            plotGraph(
                option_var.get(),
                user_input.get("1.0", "end").strip(),
                start,
                utime
            )
        except ValueError as e:
            print(f"Error: {e}. Please enter positive values.")

    def on_plot_chart():
        try:
            start = int(start_pos.get())
            if start < 0:
                raise ValueError("Negative values are not allowed")
            plotChart(user_input.get("1.0", "end").strip(), start)
        except ValueError as e:
            print(f"Error: {e}. Please enter positive values.")

    # Title
    title = ctk.CTkLabel(app, text="Disk Scheduling Algorithms", font=ctk.CTkFont(size=30, weight="bold"))
    title.pack(pady=20)

    # Algorithm Selection
    algo_frame = ctk.CTkFrame(app)
    algo_frame.pack(pady=10)

    algo_label = ctk.CTkLabel(algo_frame, text="Choose Algorithm:", font=ctk.CTkFont(size=16))
    algo_label.pack(side="left", padx=10)

    option_var = ctk.StringVar(value="Select Algorithm")
    algo_menu = ctk.CTkOptionMenu(algo_frame, variable=option_var, values=["FCFS", "SSTF", "SCAN", "CSCAN", "LOOK", "CLOOK"])
    algo_menu.pack(side="left", padx=10)

    # Values Input
    input_frame = ctk.CTkFrame(app)
    input_frame.pack(pady=10)

    vals_label = ctk.CTkLabel(input_frame, text="Enter your values:", font=ctk.CTkFont(size=16))
    vals_label.pack(side="left", padx=10)

    user_input = ctk.CTkTextbox(input_frame, width=300, height=50, font=("Century Gothic", 16))
    user_input.pack(side="left", padx=10)

    note = ctk.CTkLabel(app, text="Note: Add space after every value", font=ctk.CTkFont(size=12))
    note.pack(padx=10)

    # Current Position
    pos_frame = ctk.CTkFrame(app)
    pos_frame.pack(pady=10)

    current_label = ctk.CTkLabel(pos_frame, text="Current position of R/W head:", font=ctk.CTkFont(size=16))
    current_label.pack(side="left", padx=10)

    start_pos = ctk.CTkEntry(pos_frame, width=50)
    start_pos.pack(side="left", padx=10)

    # Unit time
    time_frame = ctk.CTkFrame(app)
    time_frame.pack(pady=10)

    time_label = ctk.CTkLabel(time_frame, text="Enter unit time:", font=ctk.CTkFont(size=16))
    time_label.pack(side="left", padx=10)

    time_val = ctk.CTkEntry(time_frame, width=50)
    time_val.pack(side="left", padx=10)

    # Buttons
    button_frame = ctk.CTkFrame(app)
    button_frame.pack(pady=20)

    visualize_button = ctk.CTkButton(button_frame, text="Plot Graph", command=on_plotGraph)
    visualize_button.pack(side="left", padx=20)

    graph_button = ctk.CTkButton(button_frame, text="Bar Chart", command=on_plot_chart)
    graph_button.pack(side="left", padx=20)

    app.mainloop()

Main()
