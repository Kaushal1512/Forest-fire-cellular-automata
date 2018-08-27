import numpy as np
import pylab as plt

n=50
T = 100
R = 4
GRS = 1 ; p_grs = 0.2
JP = 2 ; p_jp = 0.3
AP = 3 ; p_ap = 0.1
JH = 4 ; p_jh = 0.3
AH = 5 ; p_ah = 0.1
pveg = np.array([p_grs, p_jp, p_ap, p_jh, p_ah])
veg = np.zeros((n+2,n+2))
p_light = 0.001
for i in range(1,n+1): #initialization with given probabilities
    for j in range(1,n+1):
        temp = 0
        f = np.random.ranf()
        for k in range(1,6):
            temp = temp + p_grs
            if(f<temp):
                veg[i][j] = k
                break
light = np.zeros((n+2,n+2))
for i in range(1,n+1): #random lightning
    for j in range(1,n+1):
        if np.random.ranf()<p_light:
            if veg[i][j] !=GRS:
                light[i][j] = 1
state = np.array(light)
im_veg = None
for _ in xrange(T):
    if not im_veg:
        im_veg = plt.imshow(state[1:n+1,1:n+1], cmap = 'gist_earth', interpolation='none',vmin=0,vmax=2)    
        plt.colorbar(im_veg, orientation='horizontal')
    else:
        temp = np.array(veg)
        tempstate = np.array(state)
        for i in range(1,n+1):
            for j in range(1,n+1):
                count = 0
                """if state[i][j]==1:
                    veg[i][j] = GRS"""

                if tempstate[i][j] != 1:
                    for mm in range(i-1,i+2):
                        for nn in range(j-1,j+2):
                            if mm != nn:
                                count = count + state[mm][nn]
                    if veg[i][j] == AH or veg[i][j] == JH:
                        if count > R:
                            if veg[i][j] != GRS:
                                state[i][j] = 1
                    else:
                        if count>0:
                            if veg[i][j] != GRS:
                                state[i][j] = 1
                else:
                    state[i][j] = 2
                    veg[i][j] = GRS
    
        im_veg.set_data(state[1:n+1,1:n+1])
        #im_age.set_data(age[1:n+1,1:n+1])
    plt.draw()
    plt.pause(0.5)