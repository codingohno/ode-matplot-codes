import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from scipy.integrate import solve_ivp
from math import sqrt
from matplotlib.animation import PillowWriter
from matplotlib.animation import FuncAnimation



#modification
fig, ax = plt.subplots()

#getting inputs from user
A_input=input("what values of A:(ex:1,3,5)").split(',')
A_input=[int(x) for x in A_input]
k_input=input("v value:(ex:1,2,3)").split(',')
k_input=[int(x) for x in k_input]


#global
V=1 #v resolution
t = np.linspace(0,5,100)#time resolution
dog_dot=[]#references for moving dots
dog_result_x=[]
dog_result_y=[]


#ultility functions
#we have a system of first order of ode
#let us define that s=(x,y) 
#    | x |        | dx/dt |
# s= |   | ,ds/dt=|       |
#    | y |        | dy/dt |
def solve_and_plot_single(chosen_A,k):
    #inner function
    def dsdt(t,s):
        #unpack the s into x and y
        x,y=s
        vt_y=V*t-y
        dxdt=(x/sqrt(x**2+vt_y**2))*-k*V
        dydt=(vt_y/sqrt(x**2+vt_y**2))*k*V

        #return the differentiation of the column vector
        return [dxdt,dydt]

    # picking init conditions
    y0=0
    x0=chosen_A

    #there are a two types of solver given in the vid
    # odeint (old solving function:not recommended)
    # solve_ivp(with inti cond)
    solution_s=solve_ivp(dsdt,t_span=(0,max(t)),y0=(x0,y0),t_eval=t)

    #extract the x and y values and store globally
    x_arr=solution_s.y[0]
    y_arr=solution_s.y[1]
    dog_result_x.append(x_arr)
    dog_result_y.append(y_arr)

    #plot the line and the dot
    plt.plot(x_arr,y_arr,label=f"A={chosen_A} k={k}")
    temp,=plt.plot([x_arr[0]],[y_arr[0]],'o')
    dog_dot.append(temp)
    
# #plot the dog multiple
#different A
for a_val in A_input:
    for k_val in k_input:
        solve_and_plot_single(a_val,k_val)


#comparision for the moving human
#human always go with 1V
def dhumandt(t,human_pos):
    return V
solution_human=solve_ivp(dhumandt,t_span=(0,max(t)),y0=[0],t_eval=t)
human_arr_y=solution_human.y[0]
human_arr_x=len(human_arr_y)*[0]
human_plot=plt.plot(human_arr_x,human_arr_y)
human_dot,=plt.plot([human_arr_x[0]],[human_arr_y[0]],'o')

def my_update(frame):
    human_dot.set_data([human_arr_x[frame]],[human_arr_y[frame]])
    for i in range (len(dog_dot)):
        plot_dot=dog_dot[i]
        plot_dot.set_data([dog_result_x[i][frame]],[dog_result_y[i][frame]])
    return (human_dot,)+tuple(dog_dot) #unpacked tuple

_animation = FuncAnimation(fig, my_update, frames=list(range(len(t))), interval=20, repeat=True)








#setting the label for axes
plt.ylabel('y',fontsize=22)
plt.xlabel("x",fontsize=22)

#show the plot
plt.legend()
plt.show()

####################################
