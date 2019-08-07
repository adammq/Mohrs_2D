import numpy as np
from numpy import pi as pi
from numpy import cos as cos
from numpy import sin as sin
from matplotlib import pyplot as plt

# input units and values
units = input('units: ')
sigX = float(input("sigma-x: "))
sigY = float(input("sigma-y: "))
tauXY = float(input("tau-XY: "))

# calculate average stress and radius
sig_avg = (sigX + sigY)/2
R = np.sqrt(((sigX-sigY)/2)**2+tauXY**2)

# calculate max and min normal stress and max shear stress
sig1 = sig_avg + R
sig2 = sig_avg - R
tauS = R

# plot Mohr's circle
a = np.linspace(0,2*pi,256)
plt.figure(figsize=(10,10),dpi=80)
plt.subplot(1,1,1)
plt.plot(R*cos(a)+sig_avg,R*sin(a),color="blue",label="X-Y")

# plot initial points
plt.plot(sigX,tauXY,marker='x',markersize=5,color='black')
plt.annotate("X "+"("+str(round(sigX,2))+", "+str(round(tauXY,2))+") "+units,
	xy=(sigX, tauXY), xycoords='data',xytext=(+10, +30),
	textcoords='offset points', fontsize=8, arrowprops=dict(arrowstyle="->",
		connectionstyle="arc3,rad=.2"))
plt.plot(sigY,-tauXY,marker='x',markersize=5,color='black')
plt.annotate("Y "+"("+str(round(sigY,2))+", "+str(round(-tauXY,2))+") "+units,
	xy=(sigY, -tauXY), xycoords='data',xytext=(+10, +30),
	textcoords='offset points', fontsize=8, arrowprops=dict(arrowstyle="->",
		connectionstyle="arc3,rad=.2"))

#plot important points
plt.plot(sig_avg,0,marker='x',markersize=5,color='black')
plt.annotate("C "+"("+str(round(sig_avg,2))+", "+str(round(0.0,2))+") "+units,
	xy=(sig_avg, 0), xycoords='data',xytext=(+10, +30),
	textcoords='offset points', fontsize=8, arrowprops=dict(arrowstyle="->",
		connectionstyle="arc3,rad=.2"))
plt.plot(sig1,0,marker='x',markersize=5,color='black')
plt.annotate(r'$\sigma_1 = $'+str(round(sig1,2))+" "+units,xy=(sig1, 0), xycoords='data',xytext=(+10, +30),
	textcoords='offset points', fontsize=8, arrowprops=dict(arrowstyle="->",
		connectionstyle="arc3,rad=.2"))
plt.plot(sig2,0,marker='x',markersize=5,color='black')
plt.annotate(r'$\sigma_2 = $' + str(round(sig2,2))+" "+units,xy=(sig2, 0), xycoords='data',xytext=(+10, +30),
	textcoords='offset points', fontsize=8, arrowprops=dict(arrowstyle="->",
		connectionstyle="arc3,rad=.2"))
plt.plot(sig_avg,tauS,marker='x',markersize=5,color='black')
plt.annotate(r'$\tau_S = $' + str(round(tauS,2))+" "+units,xy=(sig_avg, tauS), xycoords='data',xytext=(+10, +30),
	textcoords='offset points', fontsize=8, arrowprops=dict(arrowstyle="->",
		connectionstyle="arc3,rad=.2"))

# add reference lines
plt.plot([sigX,sigY],[tauXY,-tauXY],'r:')
plt.plot([sig_avg,sig_avg],[0,tauS],'r:')

# add legend
plt.title("Mohr's Circle")
#plt.xlabel(r'$\sigma$')
#plt.ylabel(r'$\tau$')
plt.legend(loc='upper left')

# modify axes
ax = plt.gca()  # gca stands for 'get current axis'
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))
plt.gca().invert_yaxis()

# display graph
plt.show()