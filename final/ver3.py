import numpy as np
import pylab as plt
import matplotlib.colors as mcolors


def make_colormap(seq):
    """Return a LinearSegmentedColormap
    seq: a sequence of floats and RGB-tuples. The floats should be increasing
    and in the interval (0,1).
    """
    seq = [(None,) * 3, 0.0] + list(seq) + [1.0, (None,) * 3]
    cdict = {'red': [], 'green': [], 'blue': []}
    for i, item in enumerate(seq):
        if isinstance(item, float):
            r1, g1, b1 = seq[i - 1]
            r2, g2, b2 = seq[i + 1]
            cdict['red'].append([item, r1, r2])
            cdict['green'].append([item, g1, g2])
            cdict['blue'].append([item, b1, b2])
    return mcolors.LinearSegmentedColormap('CustomMap', cdict)


c = mcolors.ColorConverter().to_rgb
rvb = make_colormap(
    [c('black'),  0.33,  c('red'), 0.66, c('green')])

n=50
T = 10
R = 4
GRS = 1 ; p_grs = 0.2
JP = 2 ; p_jp = 0.3
AP = 3 ; p_ap = 0.1
JH = 4 ; p_jh = 0.3
AH = 5 ; p_ah = 0.1
pveg = np.array([p_grs, p_jp, p_ap, p_jh, p_ah])
veg = np.zeros((n+2,n+2),dtype=int)
age = np.zeros((n+2,n+2),dtype=int)
p_light = 0.1
fireprob = [0.1,0.6,0.7,0.1,0.1]#[ 0.4, 0.1, 0.1, 0.05, 0.05]
survivalprob = [ 1.0, 0.3, 0.8, 0.1, 0.2]

for i in range(1,n+1): #initialization with given probabilities
    for j in range(1,n+1):
        temp = 0
        f = np.random.ranf()
        for k in range(1,6):
            temp = temp + p_grs
            if(f<temp):
                veg[i][j] = k
                break
        if veg[i][j] == JP or veg[i][j] == JH:
            age[i][j] = np.random.randint(1,10)


im_veg = None
im_age = None
im_fire = None
state = np.zeros((n+2,n+2))+2
for _ in range(T):   
    if not im_veg:
        plt.figure(1)
        im_veg = plt.imshow(veg[1:n+1,1:n+1], cmap = 'gist_earth', interpolation='none',vmin=1,vmax=5)    
        plt.colorbar(im_veg, orientation='horizontal')
        plt.figure(2)
        im_age = plt.imshow(age[1:n+1,1:n+1], cmap = 'gist_earth', interpolation='none',vmin=0,vmax=10)    
        plt.colorbar(im_age, orientation='horizontal')
        plt.figure(3)
        im_fire = plt.imshow(state[1:n+1,1:n+1], cmap = rvb, interpolation='none',vmin=0,vmax=2)
        plt.colorbar(im_fire, orientation='horizontal')
    else:
        state = np.zeros((n+2,n+2))+2
        x = np.random.randint(1,n+1)
        y = np.random.randint(1,n+1)
        
        ran = np.random.ranf()
        flag = False
        if ran <= p_light:
            print veg[x][y]
            if np.random.ranf()<fireprob[veg[x][y]-1]:
                state[x][y] = 1
                flag = True
        #if flag:
            print "hi"
        for day in range(100):  #spreading fire
            #print day
            if not im_fire:
                plt.figure(3)
                im_fire = plt.imshow(state[1:n+1,1:n+1], cmap = 'gist_gray', interpolation='none',vmin=0,vmax=2)
                plt.colorbar(im_fire, orientation='horizontal')
            else:
                tempstate = np.array(state)
                for i in range(1,n+1): #change state
                    for j in range(1,n+1):
                        #burn = False
                        if tempstate[i][j] == 2:
                            count = 0
                            for mm in range(i-1,i+2): #count burning neighbours
                                for nn in range(j-1,j+2):

                                    if tempstate[mm][nn] == 1 and mm!=nn:
                                        count = count + 1
                            if count>0:
                                if np.random.ranf()<= fireprob[veg[i][j]-1]:
                                    state[i][j] = 1
                        elif tempstate[i][j] == 1:
                            state[i][j] = 0
                """f = False
                for i in range(1,n+1):   # check convergence
                    for j in range(1,n+1):
                        if tempstate[i][j] != state[i][j]:
                            f = True
                            break
                    if f:
                        break
                if not f:
                    break"""

                x = np.random.randint(1,n+1)
                y = np.random.randint(1,n+1)
                ran = np.random.ranf()
                if ran <= p_light:
                    if np.random.ranf()<fireprob[veg[x][y]-1] and state[x][y]==2:
                        state[x][y] = 1
                im_fire.set_data(state[1:n+1,1:n+1])
            plt.draw()
            plt.pause(0.05)
            for i in range(1,n+1):   #survival
                for j in range(1,n+1):
                    if state[i][j] == 0:
                        if np.random.ranf()>survivalprob[veg[i][j]-1]:
                            veg[i][j] = 1
                            age[i][j] = 0
                




        temp = np.array(veg)
        temp_age = np.array(age)

        for i in range(1,n+1):
            for j in range(1,n+1):
                
                flag = False
                if temp[i][j] == GRS:  #if Grass
                    for l in range(1,5):    #Grass to Juvenile pine
                        for mm in range(i-l,i+l+1):
                            for nn in range(j-l,j+l+1):
                                if mm>=0 and mm<n+2 and nn>=0 and nn<n+2 and mm!=nn:
                                    if temp[mm][nn] == JP:
                                        flag = True
                                        break
                            if flag:
                                break
                        if flag:
                            break
                    if flag:
                        p = np.random.ranf(1)
                        if p < 0.03:
                            veg[i][j] = 2
                            age[i][j] = 1
                    flag = False
                    for mm in range(i-1,i+1+1):  #Grass to Juvenile Hardwood
                        for nn in range(j-1,j+1+1):
                            if mm>=0 and mm<n+2 and nn>=0 and nn<n+2 and mm != nn:
                                if temp[mm][nn] == 5:
                                    if np.random.ranf(1) <= 0.01:
                                        veg[i][j] = 4
                                        age[i][j] = 1
                                        flag = True
                                    break
                        if flag:
                            break
                flag = False
                if temp[i][j] == JP or temp[i][j] == AP: #Pine to Juvenile Hardwood
                    for mm in range(i-1,i+1+1):  
                        for nn in range(j-1,j+1+1):
                            if mm>=0 and mm<n+2 and nn>=0 and nn<n+2 and mm != nn:
                                if temp[mm][nn] == AH:
                                    if np.random.ranf(1) <= 0.02:
                                        veg[i][j] = JH
                                        age[i][j] = 1
                                        flag = True
                                    break
                        if flag:
                            break


        for i in range(1,n+1):   #Update age
            for j in range(1,n+1):
                if veg[i][j] == 2 or veg[i][j] == 4:
                    veg[i][j] = veg[i][j] + int(age[i][j]+1)/10
                    age[i][j] = int(age[i][j] + 1)%10

        im_veg.set_data(veg[1:n+1,1:n+1])
        im_age.set_data(age[1:n+1,1:n+1])
    plt.draw()
    plt.pause(0.05)