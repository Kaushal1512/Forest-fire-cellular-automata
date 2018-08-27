import numpy as np
import pylab as plt
n = 50
veg = np.zeros((n+2,n+2))
age = np.zeros((n+2,n+2))
age = age - 1
T = 300
GRS = 1
JP = 2
AP = 3
JH = 4
AH = 5
light_prob=0.02
fire_prob= [0.4,0.1,0.1,0.05,0.05]
sur_prob= [1,0.3,0.8,0.1,0.2]
for i in range(1,n+1):
    for j in range(1,n+1):
        veg[i][j] = np.random.randint(1,6)
        if veg[i][j] == JP or veg[i][j] == JH:
            age[i][j] = np.random.randint(0,10)

im_veg = None
im_age = None
for _ in range(T):   
    if not im_veg:
        plt.figure(1)
        im_veg = plt.imshow(veg[1:n+1,1:n+1], cmap = 'gist_earth', interpolation='none',vmin=1,vmax=5)    
        plt.colorbar(im_veg, orientation='horizontal')
        plt.figure(2)
        im_age = plt.imshow(age[1:n+1,1:n+1], cmap = 'gist_earth', interpolation='none',vmin=0,vmax=10)    
        plt.colorbar(im_age, orientation='horizontal')
    else:
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

        #veg = temp
        #age = temp_age

        for i in range(1,n+1):   #Update age
            for j in range(1,n+1):
                if veg[i][j] == 2 or veg[i][j] == 4:
                    veg[i][j] = veg[i][j] + int(age[i][j]+1)/10
                    age[i][j] = int(age[i][j] + 1)%10
                    
        
        """for i in range(1,n+1):   #Fire
            for j in range(1,n+1):
                if np.random.ranf(1) <= light_prob:
                    for kk in range(1,6):
                        if veg[i][j]==kk:
                            if np.random.ranf(1) <= fire_prob[kk]:
                                if np.random.ranf(1) <= sur_prob[kk]:
                                    veg[i][j]=1
                                    age[i][j]=0"""

        lightning = np.zeros((n+2,n+2))
        state = np.zeros((n+2,n+2))
        for i in range(1,n+1):
            for j in range(1,n+1):
                f = np.random.ranf()
                if f<=light_prob:
                    lightning[i][j] = 1
                    state[i][j] = 1
        
        R = 4
        
        t = 10
        im_fire = None
        """for _ in range(t):
            if not im_fire:
                plt.figure(3)
                im_fire = plt.imshow(veg[1:n+1,1:n+1], cmap = 'gist_earth', interpolation='none',vmin=1,vmax=5)    
                plt.colorbar(im_veg, orientation='horizontal')
            else:
                temp = np.array(state)
                for i in range(1,n+1):
                    for j in range(1,n+1):
                        x = 0
                        for mm in range(1,n+1): #count burning neighbours
                            for nn in range(1,n+1):
                                if mm != nn:
                                    x = x+temp[mm][nn]
                        if temp[i][j] == 0 and veg[i][j] == JP and veg[i][j] == JH and x >= R:
                            state[i][j] = 1
                        elif temp[i][j] == 0 and x>=1:
                            state[i][j] = 1
                        elif state[i][j]==1:
                            state[i][j] = 0
                            veg[i][j] = GRS
                flag = True
                for i in range(1,n+1):
                    for j in range(1,n+1):
                        if temp[i][j]!= state[i][j]:
                            flag=False
                    if not flag:
                        break
                if flag:
                    break
                im_fire.set_data(veg[1:n+1,1:n+1])
            plt.draw()
            plt.pause(0.05)   """

        

        im_veg.set_data(veg[1:n+1,1:n+1])
        im_age.set_data(age[1:n+1,1:n+1])
    plt.draw()
    plt.pause(0.05)
count = 0
for i in range(1,n+1):
    for j in range(1,n+1):
        if veg[i][j] == 3:
            count = count + 1
#print (count)