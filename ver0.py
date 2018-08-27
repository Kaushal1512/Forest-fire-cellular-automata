import numpy as np
import pylab as plt
n = 50
veg = np.zeros((n+2,n+2))
age = np.zeros((n+2,n+2))
age = age - 1
T = 30
GRS = 1
JP = 2
AP = 3
JH = 4
AH = 5
for i in range(1,n+1):
    for j in range(1,n+1):
        veg[i][j] = np.random.randint(1,6)
        if veg[i][j] == JP or veg[i][j] == JH:
            age[i][j] = np.random.randint(0,10)

im_veg = None
im_age = None
for _ in xrange(T):   
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
                if temp[i][j] == JP or temp[i][j] == AP:
                    for mm in range(i-1,i+1+1):  #Pine to Juvenile Hardwood
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
                    
        

        im_veg.set_data(veg[1:n+1,1:n+1])
        im_age.set_data(age[1:n+1,1:n+1])
    plt.draw()
    plt.pause(0.1)
count = 0
for i in range(1,n+1):
    for j in range(1,n+1):
        if veg[i][j] == 3:
            count = count + 1
print count