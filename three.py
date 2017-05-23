import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(0,2*np.pi,101)
s=np.sin(x)
c=np.cos(x)

plt.close('all')
plt.subplot(2,2,1)
plt.plot(x,s,'b+',x,c,'r+')
plt.axis('tight')

plt.subplot(2,2,2)
plt.plot(x,s)
plt.grid()
plt.xlabel('radians')
plt.ylabel('amplitudes')
plt.title('sin(x)')
plt.axis('tight')
plt.savefig('myplot.png')

