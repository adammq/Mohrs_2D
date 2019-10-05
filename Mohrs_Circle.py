import numpy as np
from numpy import pi as pi
from numpy import cos as cos
from numpy import sin as sin
from numpy import linalg
from matplotlib import pyplot as plt

# input units and values
units = input('units: ')

sigX = float(input("sigma-x: "))
sigY = float(input("sigma-y: "))
tauXY = float(input("tau-XY: "))

#calculate principal normal stresses and absolute maximum shear stress
Cauchy = np.matrix([[sigX,tauXY],[tauXY,sigY]])

sig_prncpl = linalg.eigvals(Cauchy)
sig_prncpl = sorted(sig_prncpl,reverse=True)
tau_abs = abs(sig_prncpl[0]-sig_prncpl[1])/2

#print value outputs
print("\nPrincipal normal stresses:\n" +
	str(round(sig_prncpl[0],2)) + units + "\n" +
	str(round(sig_prncpl[1],2)) + units + "\n")
print("Absolute maximum shear stress:\n" +
	str(round(tau_abs,2))  + units + "\n")

#calculations for plot of Mohr's circle
#center of circle, corresponding to average in-plane normal stresses
sig_avg = (sig_prncpl[0] + sig_prncpl[1])/2

#initialize theta
theta = np.linspace(0,2*pi,256)

#create plot
plt.figure(figsize=(10,10),dpi=80)
plt.subplot(1,1,1)

#plot Mohr's circle
X = tau_abs*cos(theta)+sig_avg
Y = tau_abs*sin(theta)
plt.plot(X,Y,color="blue")

#notable points on graph
#absolute maximum shear stress
plt.plot(sig_avg,tau_abs,marker='o',markersize=6,color="black",
	label="Absolute maximum shear stress\n" + "(" + str(round(tau_abs,2)) + units + ")")
#principal normal stresses
#maximum
plt.plot(sig_prncpl[0],0,marker='o',markersize=6,color="black",
	label="Principal normal stresses\n" + "(" + str(round(sig_prncpl[0],2)) + units +
	", " + str(round(sig_prncpl[1],2)) + units + ")")
#minimum
plt.plot(sig_prncpl[1],0,marker='o',markersize=6,color="black")
#current stress state
#X-axis
plt.plot(sigX,tauXY,marker='o',markersize=4,color="red",
	label="Current stress state\n" + "(" + str(round(sigX,2)) + units +
	", " + str(round(sigY,2)) + units + ")")
#Y-axis
plt.plot(sigY,-tauXY,marker='o',markersize=6,color="red")
plt.grid(True)

#format axes and grid
ax = plt.gca()  # gca stands for 'get current axis'
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',sig_avg))
plt.gca().invert_yaxis()
plt.title("Mohr's Circles")
plt.legend(loc='upper left')
plt.show()