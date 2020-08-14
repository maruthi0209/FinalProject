#### Defining the functions to be used in the program ####

import random
def fact(nmbr):
    f = 1
    for i in range(1,nmbr+1):
        f = f*i
    return f
def acomb(a,b):
    if a<b:
        print("combinations are not possible")
    elif a==b:
        print("there is one possibility")
    else:
        com = fact(a)/(fact(b)*fact(a-b))
        return com
def pol(lst):
    elements = []
    prod = 1
    for i in lst:
        elements.append(i)
        prod = prod*i
    return prod
def atkinsonindex(list, co):
    wealth = []
    inwe = []
    for i in list:
        if type(i) == int:
            wealth.append(i)
        else:
            wealth.append(sum(i))
    for i in range(len(wealth)):
        inwe.append(wealth[i]**(1-co))
    avg = (sum(wealth)/len(wealth))
    if co == 1:
        ind = 1- (((pol(wealth))**(1/len(wealth)/avg)))
    elif co <0:
        print("the parameter has to be a whole number")
    else:
        ind = 1 - (((sum(inwe)/len(wealth)**(1/(1-co)))/avg))
    return ind
    print(ind)

#### Defining batteries of each robots and tasks to be performed ####

task = []
taskset ={}
batterylimit = 10
availablebattery = {}
for a in range(4):
    availablebattery[a] = random.randint(80,100)
print(availablebattery)
for b in range(6):
    task.append(random.randint(15,30)) # giving random values to task requirements
task = list(set(task)) # removing duplicates while defining tasks
diff = 6-len(task)
while (diff != 0):
    for b in range(diff):
        task.append(random.randint(15,30))
        task = list(set(task))
        diff = 6-len(task)
print(task)

####
gross = []
feas = []
robotfeasibleset = {}
robotfeasibleset1 = {}
TaskAssignment = {}
s = []
t = []
r0 = []
L0 = []
r1 = []
r2 = []
r3 = []
r4 = []
for i in availablebattery.keys(): 
    p = [] # list because dictionary doesn't take duplicate values
    for j in range(len(task)):
        a = []
        b = []
        a.append(task[j]) #adding that task first to 'a' list
        for c in range(j+1,len(task)):
            if sum(a)+task[c]<=(availablebattery[i]-batterylimit): #checking for possible tasks in the list which fit the criterion 
                b.append(task[c]) #adding that task to another list
            else:
                continue #else just continuing
        p.append(a)
        p.append(b)
    TaskAssignment[availablebattery[i]] = p
##print(TaskAssignment)

##  printing the tasks in order.

##    print("Robot " + str(i) +" having battery level of " + str(availablebattery[i]) + " percent has possible task set as ")
##    for j in range(len((TaskAssignment[availablebattery[i]]))):
##        if j%2==0:
##            print(TaskAssignment[availablebattery[i]][j],TaskAssignment[availablebattery[i]][j+1])
##        else:
##            continue
##    print(1*"\n")

##    Printing all the tasks which the robots can do

    q = []
    robotfeasibleset[availablebattery[i]] = q
##    print('The available battery for the robot is '+str(availablebattery[i])) # printing them in a desired format 
    feasible = []
    length = []
    for j in range(len(TaskAssignment[availablebattery[i]])):
        # print(TaskAssignment[availablebattery[i]])
        if j%2==0:
            z=[]
            z.append(TaskAssignment[availablebattery[i]][j])
            z.append(TaskAssignment[availablebattery[i]][j+1])
##            print('Available combinations are ' + str(TaskAssignment[availablebattery[i]][j])+' '+str(TaskAssignment[availablebattery[i]][j+1]))
            c={}
            f=[]
            f1=[]
            f2=[]
            f3=[]
            f4=[]
            f5=[]
##            # For no combinations
            c0 = TaskAssignment[availablebattery[i]][j]
##            print('First task in each combintion = '+str(c0)+"\n")
            q.append(c0)
##            print("Number of feasible combinations is/are: 1" + "\n")

            # For 1 element in list b which is TaskAssignment[i][j+1]
            c1=[]
            for a in range(len(TaskAssignment[availablebattery[i]][j+1])):
                #print(a)
                c[a]=[]
                c[a].append(c0[0])
                c[a].append(TaskAssignment[availablebattery[i]][j+1][a])
                c1.append(c[a])
            totallength1 = len(c1)
            for p in c1:
                if sum(p) <= (availablebattery[i] - batterylimit) and (len(p) != 0):
                    f1.append(p)
                else:
                    continue
            q.append(f1)
            feasiblelength1 = len(f1)
##            print('1st combination is ' + str(c1))
##            print("Total number of solutions possible is/are: " + str(totallength1))
##            print("Number of feasible solutions is/are: " + str(feasiblelength1))
##            print("Feasible solutions in 1st combination is/are: " + str(f1))
##            print("\n")

            # for 2 elements in list b which is now TasAssignment[availablebattery[i]][j+1]
            c2=[]
            for a in range(len(TaskAssignment[availablebattery[i]][j+1])-1):
                #print(a)
                c[a]=[]
                c[a].append(c0[0])
                c[a].append(TaskAssignment[availablebattery[i]][j+1][a])
                c[a].append(TaskAssignment[availablebattery[i]][j+1][a+1])
                c2.append(c[a])
            totallength2 = len(c2)    
            for p in c2:
                if sum(p) <= (availablebattery[i] - batterylimit) and (len(p) != 0):
                    f2.append(p)
                else:
                    continue
            q.append(f2)
            feasiblelength2 = len(f2)
##            print('2nd combination is ' + str(c2))
##            print("Total number of solutions possible is/are: " + str(totallength2))
##            print("Number of feasible solutions is/are: " + str(feasiblelength2))
##            print("Feasible solutions in 2nd combination is/are: " + str(f2))
##            print("\n")
            
            # for 3 elements in list b which is now TasAssignment[availablebattery[i]][j+1]
            c3=[]
            for a in range(len(TaskAssignment[availablebattery[i]][j+1])-2):
                #print(a)
                c[a]=[]
                c[a].append(c0[0])
                c[a].append(TaskAssignment[availablebattery[i]][j+1][a])
                c[a].append(TaskAssignment[availablebattery[i]][j+1][a+1])
                c[a].append(TaskAssignment[availablebattery[i]][j+1][a+2])
                if len(c[a]) == 4:
                    c3.append(c[a])
                else:
                    continue
            totallength3 = len(c3)
            for p in c3:
                if sum(p) <= (availablebattery[i] - batterylimit) and (len(p) != 0):
                    f3.append(p)
                else:
                    continue
            q.append(f3)
            feasiblelength3 = len(f3)
##            print('3rd combination is ' + str(c3))
##            print("Total number of solutions possible is/are: " + str(totallength3))
##            print("Number of feasible solutions is/are: " + str(feasiblelength3))
##            print("Feasible solutions in 3rd combination is/are: " + str(f3))
##            print("\n")

            # for 4 elements in list b which is now TasAssignment[availablebattery[i]][j+1]
            c4=[]
            for a in range(len(TaskAssignment[availablebattery[i]][j+1])-3):
                #print(a)
                c[a]=[]
                c[a].append(c0[0])
                c[a].append(TaskAssignment[availablebattery[i]][j+1][a])
                c[a].append(TaskAssignment[availablebattery[i]][j+1][a+1])
                c[a].append(TaskAssignment[availablebattery[i]][j+1][a+2])
                c[a].append(TaskAssignment[availablebattery[i]][j+1][a+3])
                if len(c[a]) == 5:
                    c4.append(c[a])
                else:
                    continue
            totallength4 = len(c4)
            for p in c4:
                if sum(p) <= (availablebattery[i] - batterylimit) and (len(p) != 0):
                    f4.append(p)
                else:
                    continue
            q.append(f4)
            feasiblelength4 = len(f4)
##            print('4th combination is ' + str(c4))
##            print("Total number of solutions possible is/are: " + str(totallength4))
##            print("Number of feasible solutions is/are: " + str(feasiblelength4))
##            print("Feasible solutions in 4th combination is/are: " + str(f4))
##            print("\n")

            # for 5 elements in list b which is now TasAssignment[availablebattery[i]][j+1]
            c5=[]
            for a in range(len(TaskAssignment[availablebattery[i]][j+1])-4):
                #print(a)
                c[a]=[]
                c[a].append(c0[0])
                c[a].append(TaskAssignment[availablebattery[i]][j+1][a])
                c[a].append(TaskAssignment[availablebattery[i]][j+1][a+1])
                c[a].append(TaskAssignment[availablebattery[i]][j+1][a+2])
                c[a].append(TaskAssignment[availablebattery[i]][j+1][a+3])
                c[a].append(TaskAssignment[availablebattery[i]][j+1][a+4])
                if len(c[a]) == 6:
                    c5.append(c[a])
                else:
                    continue
            totallength5 = len(c5)
            for p in c5:
                if sum(p) <= (availablebattery[i] - batterylimit) and (len(p) != 0):
                    f5.append(p)
                else:
                    continue
            q.append(f5)
            feasiblelength5 = len(f5)
##            print('5th combination is ' + str(c3))
##            print("Total number of solutions possible is/are: " + str(totallength5))
##            print("Number of feasible solutions is/are: " + str(feasiblelength5))
##            print("Feasible solutions in 5th combination is/are: " + str(f5))
##            print(1*"\n")
        else:
            continue
        totalfeasible = feasiblelength1 + feasiblelength2 + feasiblelength3 + feasiblelength4 + feasiblelength5 
        # print(totalfeasible)
        feasible.append(totalfeasible)
        totallength = totallength1 + totallength2 + totallength3 + totallength4 + totallength5 + len(task)
        # print(totallength)
        length.append(totallength)
##    print(feasible)
##    print(length)
    gross.append(sum(length))
    feas.append(sum(feasible))
    taskset = {}
    for i in task:
        taskset[i] = []
##    print(taskset)
    for i in robotfeasibleset.keys():
        p = []
        q = []
        r = []
        u = []
        v = []
##        print("Robot with battery level: " + str(i) + "\n")
        for j in range(len(robotfeasibleset[i])):
            if len(robotfeasibleset[i][j]) != 0:
                p.append(robotfeasibleset[i][j])
            else:
                continue
        for k in p:
            if type(k[0]) == int:
                q.append(k)
            elif len(k[0]) == 2:
                r.append(k)
            elif len(k[0]) == 3:
                u.append(k)
            else:
                v.append(k)
    for i in range(len(r)):
        if r[i][0][0] == task[0]:
            taskset[task[0]].append(r[i])
        elif r[i][0][0] == task[1]:
            taskset[task[1]].append(r[i])
        elif r[i][0][0] == task[2]:
            taskset[task[2]].append(r[i])
        elif r[i][0][0] == task[3]:
            taskset[task[3]].append(r[i])
        elif r[i][0][0] == task[4]:
            taskset[task[4]].append(r[i])
        elif r[i][0][0] == task[5]:
            taskset[task[5]].append(r[i])
        elif r[i][0][0] == task[6]:
            taskset[task[5]].append(r[i])
        elif r[i][0][0] == task[7]:
            taskset[task[5]].append(r[i])
        elif r[i][0][0] == task[8]:
            taskset[task[5]].append(r[i])
        elif r[i][0][0] == task[9]:
            taskset[task[5]].append(r[i])
        else:
            continue
##    print(taskset,"\n")
##    print(p,"\n")
##    print(q,"\n")
##    print(r,"\n")
##    print(u,"\n")
##    print(v,"\n")
##    s.append(taskset)
    s.append(p)
    r0.append(r)
    l0 = len(r0)
    l = len(r)
    w = len(q)
    x = len(r)
    y = len(u)
    z = len(v)
    L = [w,x,y,z]
    r1.append(q)
    r2.append(r)
    r3.append(u)
    r4.append(v)
    L0.append(L)
##print(r1)
##print(r2)
##print(r3)
##print(r4)
##print(s[0],"\n")
##print(s[1],"\n")
##print(s[2],"\n")
##print(s[3],"\n")    
##print(r0,"\n") # just the combinations of different task for the particular robot.
##print(L,"\n") # each element gives the length of r of each robot.
##print(q,"\n") # just the task requirements in terms of list.
##print(s,"\n") # this list has all the possible task combinations for each robot in a single matrix
##print("The total number of possible sets for the above task assignment are: " + str(sum(gross)))
##print("Out of these, the number of feasible sets are: " + str(sum(feas))+"\n")

r11 = r1[0]
t11 = []
for i in range(len(r11)):
    t11.append(r11[i][0])
r12 = r2[0]
t12 = []
for i in range(len(r12)):
    for j in range(len(r12[i])):
        t12.append(r12[i][j])
r13 = r3[0]
t13 = []
for i in range(len(r13)):
    for j in range(len(r13[i])):
        t13.append(r13[i][j])
##print(t13)
r14 = r4[0]
t14 = []
for i in range(len(r14)):
    for j in range(len(r14[i])):
        t14.append(r14[i][j])
r21 = r1[1]
t21 = []
for i in range(len(r21)):
    for j in range(len(r21[i])):
        t21.append(r21[i][j])
r22 = r2[1]
t22 = []
for i in range(len(r22)):
    for j in range(len(r22[i])):
        t22.append(r22[i][j])
r23 = r3[1]
t23 = []
for i in range(len(r23)):
    for j in range(len(r23[i])):
        t23.append(r23[i][j])
##print(t23)
r24 = r4[1]
t24 = []
for i in range(len(r24)):
    for j in range(len(r24[i])):
        t24.append(r24[i][j])
r31 = r1[2]
t31 = []
for i in range(len(r31)):
    for j in range(len(r31[i])):
        t31.append(r31[i][j])
r32 = r2[2]
t32 = []
for i in range(len(r32)):
    for j in range(len(r32[i])):
        t32.append(r32[i][j])
##print(t32)
r33 = r3[2]
t33 = []
for i in range(len(r33)):
    for j in range(len(r33[i])):
        t33.append(r33[i][j])
##print(t33)
r34 = r4[2]
t34 = []
for i in range(len(r34)):
    for j in range(len(r34[i])):
        t34.append(r34[i][j])
r41 = r1[3]
t41 = []
for i in range(len(r41)):
    for j in range(len(r41[i])):
        t41.append(r41[i][j])
r42 = r2[3]
t42 = []
for i in range(len(r42)):
    for j in range(len(r42[i])):
        t42.append(r42[i][j])
##print(t42)
r43 = r3[3]
t43 = []
for i in range(len(r43)):
    for j in range(len(r43[i])):
        t43.append(r43[i][j])
##print(t43)
r44 = r4[3]
t44 = []
for i in range(len(r44)):
    for j in range(len(r44[i])):
        t44.append(r44[i][j])

##print(t11,"\n")
##print(t12,"\n")
##print(t13,"\n")
##print(t14,"\n")
##print(t21,"\n")
##print(t22,"\n")
##print(t23,"\n")
##print(t24,"\n")
##print(t31,"\n")
##print(t32,"\n")
##print(t33,"\n")
##print(t34,"\n")
##print(t41,"\n")
##print(t42,"\n")
##print(t43,"\n")
##print(t44,"\n")

####################################################################################################
iteration1 = []

for i in t11:

    # Value of j is in t21
    for j in t21:
        if j != i:
            for k in t31:
                if k != i and k != j:
                    for l in t41:
                        if l != i and l != j and l != k:
                            m = [i,j,k,l]
                            iteration1.append(m)
                        else:
                            continue
                    for l in t42:
                        if (i not in l) and (j not in l) and (k not in l):
                            m = [i,j,k,l]
                            iteration1.append(m)
                        else:
                            continue
                    for l in t43:
                        if (i not in l) and (j not in l) and (k not in l):
                            m = [i,j,k,l]
                            iteration1.append(m)
                        else:
                            continue
                    if len(t44)!= 0:
                        for l in t44:
                            if (i not in l) and (j not in l) and (k not in l):
                                m = [i,j,k,l]
                                iteration1.append(m)
                            else:
                                continue
                    else:
                        continue
                else:
                    continue
            for k in t32:
                if (i not in k) and (j not in k):
                    for l in t41:
                        if l != i and l != j and (l not in k):
                            m = [i,j,k,l]
                            iteration1.append(m)
                        else:
                            continue
                    for l in t42:
                        if (i not in l) and (j not in l) and (k[0] not in l) and (k[1] not in l):
                            m = [i,j,k,l]
                            iteration1.append(m)
                        else:
                            continue
                    for l in t43:
                        if (i not in l) and (j not in l) and (k[0] not in l) and (k[1] not in l):
                            m = [i,j,k,l]
                            iteration1.append(m)
                        else:
                            continue
                    if len(t44)!= 0:
                        for l in t44:
                            if (i not in l) and (j not in l) and (k[0] not in l) and (k[1] not in l):
                                m = [i,j,k,l]
                                iteration1.append(m)
                            else:
                                continue
                    else:
                        continue
                else:
                    continue
            for k in t33:
                if (i not in k) and (j not in k):
                    for l in t41:
                        if l != i and l != j and (l not in k):
                            m = [i,j,k,l]
                            iteration1.append(m)
                        else:
                            continue
                    for l in t42:
                        if (i not in l) and (j not in l) and (k[0] not in l) and (k[1] not in l) and (k[2] not in l):
                            m = [i,j,k,l]
                            iteration1.append(m)
                        else:
                            continue
                    for l in t43:
                        if (i not in l) and (j not in l) and (k[0] not in l) and (k[1] not in l) and (k[2] not in l):
                            m = [i,j,k,l]
                            iteration1.append(m)
                        else:
                            continue
                    if len(t44)!= 0:
                        for l in t44:
                            if (i not in l) and (j not in l) and (k[0] not in l) and (k[1] not in l) and (k[2] not in l):
                                m = [i,j,k,l]
                                iteration1.append(m)
                            else:
                                continue
                    else:
                        continue
                else:
                    continue
            if len(t34)!= 0:
                for k in t33:
                    if (i not in k) and (j not in k):
                        for l in t41:
                            if l != i and l != j and (l not in k):
                                m = [i,j,k,l]
                                iteration1.append(m)
                            else:
                                continue
                        for l in t42:
                            if (i not in l) and (j not in l) and (l[0] not in k) and (l[1] not in k):
                                m = [i,j,k,l]
                                iteration1.append(m)
                            else:
                                continue
                        for l in t43:
                            if (i not in l) and (j not in l) and (k[0] not in l) and (k[1] not in l) and (k[2] not in l) and (k[3] not in l):
                                m = [i,j,k,l]
                                iteration1.append(m)
                            else:
                                continue
                        if len(t44)!= 0:
                            for l in t44:
                                if (i not in l) and (j not in l) and (k[0] not in l) and (k[1] not in l) and (k[2] not in l) and (k[3] not in l):
                                    m = [i,j,k,l]
                                    iteration1.append(m)
                                else:
                                    continue
                        else:
                            continue
                    else:
                        continue
            else:
                continue
        else:
            continue

    # Now the value of j is in t22
    for j in t22:
        if (i not in j):
            for k in t31:
                if k != i and (k not in j):
                    for l in t41:
                        if l != i and (l not in j) and l != k:
                            m = [i,j,k,l]
                            iteration1.append(m)
                        else:
                            continue
                    for l in t42:
                        if (i not in l) and (j[0] not in l) and (j[1] not in l) and (k not in l):
                            m = [i,j,k,l]
                            iteration1.append(m)
                        else:
                            continue
                    for l in t43:
                        if (i not in l) and (j[0] not in l) and (j[1] not in l) and (k not in l):
                            m = [i,j,k,l]
                            iteration1.append(m)
                        else:
                            continue
                    if len(t44)!= 0:
                        for l in t44:
                            if (i not in l) and (j[0] not in l) and (j[1] not in l) and (k not in l):
                                m = [i,j,k,l]
                                iteration1.append(m)
                            else:
                                continue
                    else:
                        continue
                else:
                    continue
            for k in t32:
                if (i not in k) and (j[0] not in k) and (j[1] not in k):
                    for l in t41:
                        if l != i and (l not in j) and (l not in k):
                            m = [i,j,k,l]
                            iteration1.append(m)
                        else:
                            continue
                    for l in t42:
                        if (i not in l) and (j[0] not in l) and (j[1] not in l) and (k[0] not in l) and (k[1] not in l):
                            m = [i,j,k,l]
                            iteration1.append(m)
                        else:
                            continue
                    for l in t43:
                        if (i not in l) and (j[0] not in l) and (j[1] not in l) and (k[0] not in l) and (k[1] not in l):
                            m = [i,j,k,l]
                            iteration1.append(m)
                        else:
                            continue
                    if len(t44)!= 0:
                        for l in t44:
                            if (i not in l) and (j[0] not in l) and (j[1] not in l) and (k[0] not in l) and (k[1] not in l):
                                m = [i,j,k,l]
                                iteration1.append(m)
                            else:
                                continue
                    else:
                        continue
                else:
                    continue
            for k in t33:
                if (i not in k) and (j[0] not in k) and (j[1] not in k):
                    for l in t41:
                        if l != i and (l not in j) and (l not in k):
                            m = [i,j,k,l]
                            iteration1.append(m)
                        else:
                            continue
                    for l in t42:
                        if (i not in l) and (j[0] not in l) and (j[1] not in l) and (k[0] not in l) and (k[1] not in l) and (k[2] not in l):
                            m = [i,j,k,l]
                            iteration1.append(m)
                        else:
                            continue
                    for l in t43:
                        if (i not in l) and (j[0] not in l) and (j[1] not in l) and (k[0] not in l) and (k[1] not in l) and (k[2] not in l):
                            m = [i,j,k,l]
                            iteration1.append(m)
                        else:
                            continue
                    if len(t44)!= 0:
                        for l in t44:
                            if (i not in l) and (j[0] not in l) and (j[1] not in l) and (k[0] not in l) and (k[1] not in l) and (k[2] not in l):
                                m = [i,j,k,l]
                                iteration1.append(m)
                            else:
                                continue
                    else:
                        continue
                else:
                    continue
            if len(t34)!= 0:
                for k in t34:
                    if (i not in k) and (j[0] not in k) and (j[1] not in k):
                        for l in t41:
                            if l != i and (l not in j) and (l not in k):
                                m = [i,j,k,l]
                                iteration1.append(m)
                            else:
                                continue
                        for l in t42:
                            if (i not in l) and (j[0] not in l) and (j[1] not in l) and (l[0] not in k) and (l[1] not in k):
                                m = [i,j,k,l]
                                iteration1.append(m)
                            else:
                                continue
                        for l in t43:
                            if (i not in l) and (j[0] not in l) and (j[1] not in l) and (k[0] not in l) and (k[1] not in l) and (k[2] not in l) and (k[3] not in l):
                                m = [i,j,k,l]
                                iteration1.append(m)
                            else:
                                continue
                        if len(t44)!= 0:
                            for l in t44:
                                if (i not in l) and (j[0] not in l) and (j[1] not in l) and (k[0] not in l) and (k[1] not in l) and (k[2] not in l) and (k[3] not in l):
                                    m = [i,j,k,l]
                                    iteration1.append(m)
                                else:
                                    continue
                        else:
                            continue
                    else:
                        continue
            else:
                continue
        else:
            continue        

    # Now the value of j is in t23
    for j in t23:
        if (i not in j):
            for k in t31:
                if k != i and (k not in j):
                    for l in t41:
                        if l != i and (l not in j) and l != k:
                            m = [i,j,k,l]
                            iteration1.append(m)
                        else:
                            continue
                    for l in t42:
                        if (i not in l) and (l[0] not in j) and (l[1] not in j) and (k not in l):
                            m = [i,j,k,l]
                            iteration1.append(m)
                        else:
                            continue
                    for l in t43:
                        if (i not in l) and (j[0] not in l) and (j[1] not in l) and (j[2] not in l) and (k not in l):
                            m = [i,j,k,l]
                            iteration1.append(m)
                        else:
                            continue
                    if len(t44)!= 0:
                        for l in t44:
                            if (i not in l) and (j[0] not in l) and (j[1] not in l) and (j[2] not in l) and (k not in l):
                                m = [i,j,k,l]
                                iteration1.append(m)
                            else:
                                continue
                    else:
                        continue
                else:
                    continue
            for k in t32:
                if (i not in k) and (k[0] not in j) and (k[1] not in j):
                    for l in t41:
                        if l != i and (l not in j) and (l not in k):
                            m = [i,j,k,l]
                            iteration1.append(m)
                        else:
                            continue
                    for l in t42:
                        if (i not in l) and (l[0] not in j) and (l[1] not in j) and (k[0] not in l) and (k[1] not in l):
                            m = [i,j,k,l]
                            iteration1.append(m)
                        else:
                            continue
                    for l in t43:
                        if (i not in l) and (j[0] not in l) and (j[1] not in l) and (j[2] not in l) and (k[0] not in l) and (k[1] not in l):
                            m = [i,j,k,l]
                            iteration1.append(m)
                        else:
                            continue
                    if len(t44)!= 0:
                        for l in t44:
                            if (i not in l) and (j[0] not in l) and (j[1] not in l) and (j[2] not in l) and (k[0] not in l) and (k[1] not in l):
                                m = [i,j,k,l]
                                iteration1.append(m)
                            else:
                                continue
                    else:
                        continue
                else:
                    continue
            for k in t33:
                if (i not in k) and (j[0] not in k) and (j[1] not in k) and (j[2] not in k):
                    for l in t41:
                        if l != i and (l not in j) and (l not in k):
                            m = [i,j,k,l]
                            iteration1.append(m)
                        else:
                            continue
                    for l in t42:
                        if (i not in l) and (l[0] not in j) and (l[1] not in j) and (k[0] not in l) and (k[1] not in l) and (k[2] not in l):
                            m = [i,j,k,l]
                            iteration1.append(m)
                        else:
                            continue
                    for l in t43:
                        if (i not in l) and (j[0] not in l) and (j[1] not in l) and (j[2] not in l) and (k[0] not in l) and (k[1] not in l) and (k[2] not in l):
                            m = [i,j,k,l]
                            iteration1.append(m)
                        else:
                            continue
                    if len(t44)!= 0:
                        for l in t44:
                            if (i not in l) and (j[0] not in l) and (j[1] not in l) and (j[2] not in l) and (k[0] not in l) and (k[1] not in l) and (k[2] not in l):
                                m = [i,j,k,l]
                                iteration1.append(m)
                            else:
                                continue
                    else:
                        continue
                else:
                    continue
            if len(t34)!= 0:
                for k in t34:
                    if (i not in k) and (j[0] not in k) and (j[1] not in k) and (j[2] not in k):
                        for l in t41:
                            if l != i and (l not in j) and (l not in k):
                                m = [i,j,k,l]
                                iteration1.append(m)
                            else:
                                continue
                        for l in t42:
                            if (i not in l) and (l[0] not in j) and (l[1] not in j) and (l[0] not in k) and (l[1] not in k):
                                m = [i,j,k,l]
                                iteration1.append(m)
                            else:
                                continue
                        for l in t43:
                            if (i not in l) and (j[0] not in l) and (j[1] not in l) and (j[2] not in l) and (k[0] not in l) and (k[1] not in l) and (k[2] not in l) and (k[3] not in l):
                                m = [i,j,k,l]
                                iteration1.append(m)
                            else:
                                continue
                        if len(t44)!= 0:
                            for l in t44:
                                if (i not in l) and (j[0] not in l) and (j[1] not in l) and (j[2] not in l) and (k[0] not in l) and (k[1] not in l) and (k[2] not in l) and (k[3] not in l):
                                    m = [i,j,k,l]
                                    iteration1.append(m)
                                else:
                                    continue
                        else:
                            continue
                    else:
                        continue
            else:
                continue
        else:
            continue

    # Now the value of j is in t24
    if len(t24) != 0:
        for j in t24:
            if (i not in j):
                for k in t31:
                    if k != i and (k not in j):
                        for l in t41:
                            if l != i and (l not in j) and l != k:
                                m = [i,j,k,l]
                                iteration1.append(m)
                            else:
                                continue
                        for l in t42:
                            if (i not in l) and (l[0] not in j) and (l[1] not in j) and (k not in l):
                                m = [i,j,k,l]
                                iteration1.append(m)
                            else:
                                continue
                        for l in t43:
                            if (i not in l) and (l[0] not in j) and (l[1] not in j) and (l[2] not in j) and (k not in l):
                                m = [i,j,k,l]
                                iteration1.append(m)
                            else:
                                continue
                        if len(t44)!= 0:
                            for l in t44:
                                if (i not in l) and (j[0] not in l) and (j[1] not in l) and (j[2] not in l) and (j[3] not in l) and (k not in l):
                                    m = [i,j,k,l]
                                    iteration1.append(m)
                                else:
                                    continue
                        else:
                            continue
                    else:
                        continue
                for k in t32:
                    if (i not in k) and (k[0] not in j) and (k[1] not in j):
                        for l in t41:
                            if l != i and (l not in j) and (l not in k):
                                m = [i,j,k,l]
                                iteration1.append(m)
                            else:
                                continue
                        for l in t42:
                            if (i not in l) and (l[0] not in j) and (l[1] not in j) and (k[0] not in l) and (k[1] not in l):
                                m = [i,j,k,l]
                                iteration1.append(m)
                            else:
                                continue
                        for l in t43:
                            if (i not in l) and (l[0] not in j) and (l[1] not in j) and (l[2] not in j) and (k[0] not in l) and (k[1] not in l):
                                m = [i,j,k,l]
                                iteration1.append(m)
                            else:
                                continue
                        if len(t44)!= 0:
                            for l in t44:
                                if (i not in l) and (j[0] not in l) and (j[1] not in l) and (j[2] not in l) and (j[3] not in l) and (k[0] not in l) and (k[1] not in l):
                                    m = [i,j,k,l]
                                    iteration1.append(m)
                                else:
                                    continue
                        else:
                            continue
                    else:
                        continue
                for k in t33:
                    if (i not in k) and (k[0] not in j) and (k[1] not in j) and (k[2] not in j):
                        for l in t41:
                            if l != i and (l not in j) and (l not in k):
                                m = [i,j,k,l]
                                iteration1.append(m)
                            else:
                                continue
                        for l in t42:
                            if (i not in l) and (l[0] not in j) and (l[1] not in j) and (k[0] not in l) and (k[1] not in l) and (k[2] not in l):
                                m = [i,j,k,l]
                                iteration1.append(m)
                            else:
                                continue
                        for l in t43:
                            if (i not in l) and (j[0] not in l) and (j[1] not in l) and (j[2] not in l) and (k[0] not in l) and (k[1] not in l) and (k[2] not in l):
                                m = [i,j,k,l]
                                iteration1.append(m)
                            else:
                                continue
                        if len(t44)!= 0:
                            for l in t44:
                                if (i not in l) and (j[0] not in l) and (j[1] not in l) and (j[2] not in l) and (k[0] not in l) and (k[1] not in l) and (k[2] not in l):
                                    m = [i,j,k,l]
                                    iteration1.append(m)
                                else:
                                    continue
                        else:
                            continue
                    else:
                        continue
                if len(t34)!= 0:
                    for k in t34:
                        if (i not in k) and (j[0] not in k) and (j[1] not in k) and (j[2] not in k):
                            for l in t41:
                                if l != i and (l not in j) and (l not in k):
                                    m = [i,j,k,l]
                                    iteration1.append(m)
                                else:
                                    continue
                            for l in t42:
                                if (i not in l) and (l[0] not in j) and (l[1] not in j) and (l[0] not in k) and (l[1] not in k):
                                    m = [i,j,k,l]
                                    iteration1.append(m)
                                else:
                                    continue
                            for l in t43:
                                if (i not in l) and (j[0] not in l) and (j[1] not in l) and (j[2] not in l) and (k[0] not in l) and (k[1] not in l) and (k[2] not in l) and (k[3] not in l):
                                    m = [i,j,k,l]
                                    iteration1.append(m)
                                else:
                                    continue
                            if len(t44)!= 0:
                                for l in t44:
                                    if (i not in l) and (j[0] not in l) and (j[1] not in l) and (j[2] not in l) and (k[0] not in l) and (k[1] not in l) and (k[2] not in l) and (k[3] not in l):
                                        m = [i,j,k,l]
                                        iteration1.append(m)
                                    else:
                                        continue
                            else:
                                continue
                        else:
                            continue
                else:
                    continue
            else:
                continue
    else:
        continue

# i is in t12
for i in t12:

    # Value of j is in t21
    for j in t21:
        if (j not in i):
            for k in t31:
                if (k not in i) and k != j:
                    for l in t41:
                        if (l not in i) and l != j and l != k:
                            m = [i,j,k,l]
                            iteration1.append(m)
                        else:
                            continue
                    for l in t42:
                        if (i[0] not in l) and (i[1] not in l) and (j not in l) and (k not in l):
                            m = [i,j,k,l]
                            iteration1.append(m)
                        else:
                            continue
                    for l in t43:
                        if (i[0] not in l) and (i[1] not in l) and (j not in l) and (k not in l):
                            m = [i,j,k,l]
                            iteration1.append(m)
                        else:
                            continue
                    if len(t44)!= 0:
                        for l in t44:
                            if (i[0] not in l) and (i[1] not in l) and (j not in l) and (k not in l):
                                m = [i,j,k,l]
                                iteration1.append(m)
                            else:
                                continue
                    else:
                        continue
                else:
                    continue
            for k in t32:
                if (i[0] not in k) and (i[1] not in k) and (j not in k):
                    for l in t41:
                        if (l not in i) and l != j and (l not in k):
                            m = [i,j,k,l]
                            iteration1.append(m)
                        else:
                            continue
                    for l in t42:
                        if (i[0] not in l) and (i[1] not in l) and (j not in l) and (k[0] not in l) and (k[1] not in l):
                            m = [i,j,k,l]
                            iteration1.append(m)
                        else:
                            continue
                    for l in t43:
                        if (i[0] not in l) and (i[1] not in l) and (j not in l) and (k[0] not in l) and (k[1] not in l):
                            m = [i,j,k,l]
                            iteration1.append(m)
                        else:
                            continue
                    if len(t44)!= 0:
                        for l in t44:
                            if (i[0] not in l) and (i[1] not in l) and (j not in l) and (k[0] not in l) and (k[1] not in l):
                                m = [i,j,k,l]
                                iteration1.append(m)
                            else:
                                continue
                    else:
                        continue
                else:
                    continue
            for k in t33:
                if (i[0] not in k) and (i[1] not in k) and (j not in k):
                    for l in t41:
                        if (l not in i) and l != j and (l not in k):
                            m = [i,j,k,l]
                            iteration1.append(m)
                        else:
                            continue
                    for l in t42:
                        if (i[0] not in l) and (i[1] not in l) and (j not in l) and (k[0] not in l) and (k[1] not in l) and (k[2] not in l):
                            m = [i,j,k,l]
                            iteration1.append(m)
                        else:
                            continue
                    for l in t43:
                        if (i[0] not in l) and (i[1] not in l) and (j not in l) and (k[0] not in l) and (k[1] not in l) and (k[2] not in l):
                            m = [i,j,k,l]
                            iteration1.append(m)
                        else:
                            continue
                    if len(t44)!= 0:
                        for l in t44:
                            if (i[0] not in l) and (i[1] not in l) and (j not in l) and (k[0] not in l) and (k[1] not in l) and (k[2] not in l):
                                m = [i,j,k,l]
                                iteration1.append(m)
                            else:
                                continue
                    else:
                        continue
                else:
                    continue
            if len(t34)!= 0:
                for k in t33:
                    if (i[0] not in k) and (i[1] not in k) and (j not in k):
                        for l in t41:
                            if (l not in i) and l != j and (l not in k):
                                m = [i,j,k,l]
                                iteration1.append(m)
                            else:
                                continue
                        for l in t42:
                            if (i[0] not in l) and (i[1] not in l) and (j not in l) and (l[0] not in k) and (l[1] not in k):
                                m = [i,j,k,l]
                                iteration1.append(m)
                            else:
                                continue
                        for l in t43:
                            if (i[0] not in l) and (i[1] not in l) and (j not in l) and (k[0] not in l) and (k[1] not in l) and (k[2] not in l) and (k[3] not in l):
                                m = [i,j,k,l]
                                iteration1.append(m)
                            else:
                                continue
                        if len(t44)!= 0:
                            for l in t44:
                                if (i[0] not in l) and (i[1] not in l) and (j not in l) and (k[0] not in l) and (k[1] not in l) and (k[2] not in l) and (k[3] not in l):
                                    m = [i,j,k,l]
                                    iteration1.append(m)
                                else:
                                    continue
                        else:
                            continue
                    else:
                        continue
            else:
                continue
        else:
            continue

    # Now the value of j is in t22
    for j in t22:
        if (i[0] not in j) and (i[1] not in j):
            for k in t31:
                if (k not in i) and (k not in j):
                    for l in t41:
                        if (l not in i) and (l not in j) and l != k:
                            m = [i,j,k,l]
                            iteration1.append(m)
                        else:
                            continue
                    for l in t42:
                        if (i[0] not in l) and (i[1] not in l) and (j[0] not in l) and (j[1] not in l) and (k not in l):
                            m = [i,j,k,l]
                            iteration1.append(m)
                        else:
                            continue
                    for l in t43:
                        if (i[0] not in l) and (i[1] not in l) and (j[0] not in l) and (j[1] not in l) and (k not in l):
                            m = [i,j,k,l]
                            iteration1.append(m)
                        else:
                            continue
                    if len(t44)!= 0:
                        for l in t44:
                            if (i[0] not in l) and (i[1] not in l) and (j[0] not in l) and (j[1] not in l) and (k not in l):
                                m = [i,j,k,l]
                                iteration1.append(m)
                            else:
                                continue
                    else:
                        continue
                else:
                    continue
            for k in t32:
                if (i[0] not in k) and (i[1] not in k) and (j[0] not in k) and (j[1] not in k):
                    for l in t41:
                        if (l not in i) and (l not in j) and (l not in k):
                            m = [i,j,k,l]
                            iteration1.append(m)
                        else:
                            continue
                    for l in t42:
                        if (i[0] not in l) and (i[1] not in l) and (j[0] not in l) and (j[1] not in l) and (k[0] not in l) and (k[1] not in l):
                            m = [i,j,k,l]
                            iteration1.append(m)
                        else:
                            continue
                    for l in t43:
                        if (i[0] not in l) and (i[1] not in l) and (j[0] not in l) and (j[1] not in l) and (k[0] not in l) and (k[1] not in l):
                            m = [i,j,k,l]
                            iteration1.append(m)
                        else:
                            continue
                    if len(t44)!= 0:
                        for l in t44:
                            if (i[0] not in l) and (i[1] not in l) and (j[0] not in l) and (j[1] not in l) and (k[0] not in l) and (k[1] not in l):
                                m = [i,j,k,l]
                                iteration1.append(m)
                            else:
                                continue
                    else:
                        continue
                else:
                    continue
            for k in t33:
                if (i[0] not in k) and (i[1] not in k) and (j[0] not in k) and (j[1] not in k):
                    for l in t41:
                        if (l not in i) and (l not in j) and (l not in k):
                            m = [i,j,k,l]
                            iteration1.append(m)
                        else:
                            continue
                    for l in t42:
                        if (i[0] not in l) and (i[1] not in l) and (j[0] not in l) and (j[1] not in l) and (k[0] not in l) and (k[1] not in l) and (k[2] not in l):
                            m = [i,j,k,l]
                            iteration1.append(m)
                        else:
                            continue
                    for l in t43:
                        if (i[0] not in l) and (i[1] not in l) and (j[0] not in l) and (j[1] not in l) and (k[0] not in l) and (k[1] not in l) and (k[2] not in l):
                            m = [i,j,k,l]
                            iteration1.append(m)
                        else:
                            continue
                    if len(t44)!= 0:
                        for l in t44:
                            if (i[0] not in l) and (i[1] not in l) and (j[0] not in l) and (j[1] not in l) and (k[0] not in l) and (k[1] not in l) and (k[2] not in l):
                                m = [i,j,k,l]
                                iteration1.append(m)
                            else:
                                continue
                    else:
                        continue
                else:
                    continue
            if len(t34)!= 0:
                for k in t34:
                    if (i[0] not in k) and (i[1] not in k) and (j[0] not in k) and (j[1] not in k):
                        for l in t41:
                            if l != i and (l not in j) and (l not in k):
                                m = [i,j,k,l]
                                iteration1.append(m)
                            else:
                                continue
                        for l in t42:
                            if (i not in l) and (j[0] not in l) and (j[1] not in l) and (l[0] not in k) and (l[1] not in k):
                                m = [i,j,k,l]
                                iteration1.append(m)
                            else:
                                continue
                        for l in t43:
                            if (i not in l) and (j[0] not in l) and (j[1] not in l) and (k[0] not in l) and (k[1] not in l) and (k[2] not in l) and (k[3] not in l):
                                m = [i,j,k,l]
                                iteration1.append(m)
                            else:
                                continue
                        if len(t44)!= 0:
                            for l in t44:
                                if (i not in l) and (j[0] not in l) and (j[1] not in l) and (k[0] not in l) and (k[1] not in l) and (k[2] not in l) and (k[3] not in l):
                                    m = [i,j,k,l]
                                    iteration1.append(m)
                                else:
                                    continue
                        else:
                            continue
                    else:
                        continue
            else:
                continue
        else:
            continue        

    # Now the value of j is in t23
    for j in t23:
        if (i[0] not in j) and (i[1] not in j):
            for k in t31:
                if (k not in i) and (k not in j):
                    for l in t41:
                        if (l not in i) and (l not in j) and l != k:
                            m = [i,j,k,l]
                            iteration1.append(m)
                        else:
                            continue
                    for l in t42:
                        if (i[0] not in l) and (i[1] not in l) and (l[0] not in j) and (l[1] not in j) and (k not in l):
                            m = [i,j,k,l]
                            iteration1.append(m)
                        else:
                            continue
                    for l in t43:
                        if (i[0] not in l) and (i[1] not in l) and (j[0] not in l) and (j[1] not in l) and (j[2] not in l) and (k not in l):
                            m = [i,j,k,l]
                            iteration1.append(m)
                        else:
                            continue
                    if len(t44)!= 0:
                        for l in t44:
                            if (i[0] not in l) and (i[1] not in l) and (j[0] not in l) and (j[1] not in l) and (j[2] not in l) and (k not in l):
                                m = [i,j,k,l]
                                iteration1.append(m)
                            else:
                                continue
                    else:
                        continue
                else:
                    continue
            for k in t32:
                if (i[0] not in k) and (i[1] not in k) and (k[0] not in j) and (k[1] not in j):
                    for l in t41:
                        if (l not in i) and (l not in j) and (l not in k):
                            m = [i,j,k,l]
                            iteration1.append(m)
                        else:
                            continue
                    for l in t42:
                        if (i[0] not in l) and (i[1] not in l) and (l[0] not in j) and (l[1] not in j) and (k[0] not in l) and (k[1] not in l):
                            m = [i,j,k,l]
                            iteration1.append(m)
                        else:
                            continue
                    for l in t43:
                        if (i[0] not in l) and (i[1] not in l) and (j[0] not in l) and (j[1] not in l) and (j[2] not in l) and (k[0] not in l) and (k[1] not in l):
                            m = [i,j,k,l]
                            iteration1.append(m)
                        else:
                            continue
                    if len(t44)!= 0:
                        for l in t44:
                            if (i[0] not in l) and (i[1] not in l) and (j[0] not in l) and (j[1] not in l) and (j[2] not in l) and (k[0] not in l) and (k[1] not in l):
                                m = [i,j,k,l]
                                iteration1.append(m)
                            else:
                                continue
                    else:
                        continue
                else:
                    continue
            for k in t33:
                if (i[0] not in l) and (i[1] not in l) and (j[0] not in k) and (j[1] not in k) and (j[2] not in k):
                    for l in t41:
                        if (l not in i) and (l not in j) and (l not in k):
                            m = [i,j,k,l]
                            iteration1.append(m)
                        else:
                            continue
                    for l in t42:
                        if (i[0] not in l) and (i[1] not in l) and (l[0] not in j) and (l[1] not in j) and (k[0] not in l) and (k[1] not in l) and (k[2] not in l):
                            m = [i,j,k,l]
                            iteration1.append(m)
                        else:
                            continue
                    for l in t43:
                        if (i[0] not in l) and (i[1] not in l) and (j[0] not in l) and (j[1] not in l) and (j[2] not in l) and (k[0] not in l) and (k[1] not in l) and (k[2] not in l):
                            m = [i,j,k,l]
                            iteration1.append(m)
                        else:
                            continue
                    if len(t44)!= 0:
                        for l in t44:
                            if (i[0] not in l) and (i[1] not in l) and (j[0] not in l) and (j[1] not in l) and (j[2] not in l) and (k[0] not in l) and (k[1] not in l) and (k[2] not in l):
                                m = [i,j,k,l]
                                iteration1.append(m)
                            else:
                                continue
                    else:
                        continue
                else:
                    continue
            if len(t34)!= 0:
                for k in t34:
                    if (i[0] not in l) and (i[1] not in l) and (j[0] not in k) and (j[1] not in k) and (j[2] not in k):
                        for l in t41:
                            if (l not in i) and (l not in j) and (l not in k):
                                m = [i,j,k,l]
                                iteration1.append(m)
                            else:
                                continue
                        for l in t42:
                            if (i[0] not in l) and (i[1] not in l) and (l[0] not in j) and (l[1] not in j) and (l[0] not in k) and (l[1] not in k):
                                m = [i,j,k,l]
                                iteration1.append(m)
                            else:
                                continue
                        for l in t43:
                            if (i[0] not in l) and (i[1] not in l) and (j[0] not in l) and (j[1] not in l) and (j[2] not in l) and (k[0] not in l) and (k[1] not in l) and (k[2] not in l) and (k[3] not in l):
                                m = [i,j,k,l]
                                iteration1.append(m)
                            else:
                                continue
                        if len(t44)!= 0:
                            for l in t44:
                                if (i[0] not in l) and (i[1] not in l) and (j[0] not in l) and (j[1] not in l) and (j[2] not in l) and (k[0] not in l) and (k[1] not in l) and (k[2] not in l) and (k[3] not in l):
                                    m = [i,j,k,l]
                                    iteration1.append(m)
                                else:
                                    continue
                        else:
                            continue
                    else:
                        continue
            else:
                continue
        else:
            continue

    # Now the value of j is in t24
    if len(t24) != 0:
        for j in t24:
            if (i[0] not in j) and (i[1] not in j):
                for k in t31:
                    if (k not in i) and (k not in j):
                        for l in t41:
                            if (l not in i) and (l not in j) and l != k:
                                m = [i,j,k,l]
                                iteration1.append(m)
                            else:
                                continue
                        for l in t42:
                            if (i[0] not in l) and (i[1] not in l) and (l[0] not in j) and (l[1] not in j) and (k not in l):
                                m = [i,j,k,l]
                                iteration1.append(m)
                            else:
                                continue
                        for l in t43:
                            if (i[0] not in l) and (i[1] not in l) and (l[0] not in j) and (l[1] not in j) and (l[2] not in j) and (k not in l):
                                m = [i,j,k,l]
                                iteration1.append(m)
                            else:
                                continue
                        if len(t44)!= 0:
                            for l in t44:
                                if (i[0] not in l) and (i[1] not in l) and (j[0] not in l) and (j[1] not in l) and (j[2] not in l) and (j[3] not in l) and (k not in l):
                                    m = [i,j,k,l]
                                    iteration1.append(m)
                                else:
                                    continue
                        else:
                            continue
                    else:
                        continue
                for k in t32:
                    if (i[0] not in k) and (i[1] not in k) and (k[0] not in j) and (k[1] not in j):
                        for l in t41:
                            if (l not in i) and (l not in j) and (l not in k):
                                m = [i,j,k,l]
                                iteration1.append(m)
                            else:
                                continue
                        for l in t42:
                            if (i[0] not in l) and (i[1] not in l) and (l[0] not in j) and (l[1] not in j) and (k[0] not in l) and (k[1] not in l):
                                m = [i,j,k,l]
                                iteration1.append(m)
                            else:
                                continue
                        for l in t43:
                            if (i[0] not in l) and (i[1] not in l) and (l[0] not in j) and (l[1] not in j) and (l[2] not in j) and (k[0] not in l) and (k[1] not in l):
                                m = [i,j,k,l]
                                iteration1.append(m)
                            else:
                                continue
                        if len(t44)!= 0:
                            for l in t44:
                                if (i[0] not in l) and (i[1] not in l) and (j[0] not in l) and (j[1] not in l) and (j[2] not in l) and (j[3] not in l) and (k[0] not in l) and (k[1] not in l):
                                    m = [i,j,k,l]
                                    iteration1.append(m)
                                else:
                                    continue
                        else:
                            continue
                    else:
                        continue
                for k in t33:
                    if (i[0] not in k) and (i[1] not in k) and (k[0] not in j) and (k[1] not in j) and (k[2] not in j):
                        for l in t41:
                            if (l not in i) and (l not in j) and (l not in k):
                                m = [i,j,k,l]
                                iteration1.append(m)
                            else:
                                continue
                        for l in t42:
                            if (i[0] not in l) and (i[1] not in l) and (l[0] not in j) and (l[1] not in j) and (k[0] not in l) and (k[1] not in l) and (k[2] not in l):
                                m = [i,j,k,l]
                                iteration1.append(m)
                            else:
                                continue
                        for l in t43:
                            if (i[0] not in l) and (i[1] not in l) and (j[0] not in l) and (j[1] not in l) and (j[2] not in l) and (k[0] not in l) and (k[1] not in l) and (k[2] not in l):
                                m = [i,j,k,l]
                                iteration1.append(m)
                            else:
                                continue
                        if len(t44)!= 0:
                            for l in t44:
                                if (i[0] not in l) and (i[1] not in l) and (j[0] not in l) and (j[1] not in l) and (j[2] not in l) and (k[0] not in l) and (k[1] not in l) and (k[2] not in l):
                                    m = [i,j,k,l]
                                    iteration1.append(m)
                                else:
                                    continue
                        else:
                            continue
                    else:
                        continue
                if len(t34)!= 0:
                    for k in t34:
                        if (i[0] not in k) and (i[1] not in k) and (j[0] not in k) and (j[1] not in k) and (j[2] not in k):
                            for l in t41:
                                if (l not in i) and (l not in j) and (l not in k):
                                    m = [i,j,k,l]
                                    iteration1.append(m)
                                else:
                                    continue
                            for l in t42:
                                if (i[0] not in l) and (i[1] not in l) and (l[0] not in j) and (l[1] not in j) and (l[0] not in k) and (l[1] not in k):
                                    m = [i,j,k,l]
                                    iteration1.append(m)
                                else:
                                    continue
                            for l in t43:
                                if (i[0] not in l) and (i[1] not in l) and (j[0] not in l) and (j[1] not in l) and (j[2] not in l) and (k[0] not in l) and (k[1] not in l) and (k[2] not in l) and (k[3] not in l):
                                    m = [i,j,k,l]
                                    iteration1.append(m)
                                else:
                                    continue
                            if len(t44)!= 0:
                                for l in t44:
                                    if (i[0] not in l) and (i[1] not in l) and (j[0] not in l) and (j[1] not in l) and (j[2] not in l) and (k[0] not in l) and (k[1] not in l) and (k[2] not in l) and (k[3] not in l):
                                        m = [i,j,k,l]
                                        iteration1.append(m)
                                    else:
                                        continue
                            else:
                                continue
                        else:
                            continue
                else:
                    continue
            else:
                continue
    else:
        continue

# i is in t13
for i in t13:

    # Value of j is in t21
    for j in t21:
        if (j not in i):
            for k in t31:
                if (k not in i) and k != j:
                    for l in t41:
                        if (l not in i) and l != j and l != k:
                            m = [i,j,k,l]
                            iteration1.append(m)
                        else:
                            continue
                    for l in t42:
                        if (l[0] not in i) and (l[1] not in i) and (j not in l) and (k not in l):
                            m = [i,j,k,l]
                            iteration1.append(m)
                        else:
                            continue
                    for l in t43:
                        if (i[0] not in l) and (i[1] not in l) and (i[2] not in l) and (j not in l) and (k not in l):
                            m = [i,j,k,l]
                            iteration1.append(m)
                        else:
                            continue
                    if len(t44)!= 0:
                        for l in t44:
                            if (i[0] not in l) and (i[1] not in l) and (i[2] not in l) and (j not in l) and (k not in l):
                                m = [i,j,k,l]
                                iteration1.append(m)
                            else:
                                continue
                    else:
                        continue
                else:
                    continue
            for k in t32:
                if (k[0] not in i) and (k[1] not in i) and (j not in k):
                    for l in t41:
                        if (l not in i) and l != j and (l not in k):
                            m = [i,j,k,l]
                            iteration1.append(m)
                        else:
                            continue
                    for l in t42:
                        if (l[0] not in i) and (l[1] not in i) and (j not in l) and (k[0] not in l) and (k[1] not in l):
                            m = [i,j,k,l]
                            iteration1.append(m)
                        else:
                            continue
                    for l in t43:
                        if (i[0] not in l) and (i[1] not in l) and (i[2] not in l) and (j not in l) and (k[0] not in l) and (k[1] not in l):
                            m = [i,j,k,l]
                            iteration1.append(m)
                        else:
                            continue
                    if len(t44)!= 0:
                        for l in t44:
                            if (i[0] not in l) and (i[1] not in l) and (i[2] not in l) and (j not in l) and (k[0] not in l) and (k[1] not in l):
                                m = [i,j,k,l]
                                iteration1.append(m)
                            else:
                                continue
                    else:
                        continue
                else:
                    continue
            for k in t33:
                if (i[0] not in k) and (i[1] not in k) and (i[2] not in k) and (j not in k):
                    for l in t41:
                        if (l not in i) and l != j and (l not in k):
                            m = [i,j,k,l]
                            iteration1.append(m)
                        else:
                            continue
                    for l in t42:
                        if (l[0] not in i) and (l[1] not in i) and (j not in l) and (k[0] not in l) and (k[1] not in l) and (k[2] not in l):
                            m = [i,j,k,l]
                            iteration1.append(m)
                        else:
                            continue
                    for l in t43:
                        if (i[0] not in l) and (i[1] not in l) and (i[2] not in l) and (j not in l) and (k[0] not in l) and (k[1] not in l) and (k[2] not in l):
                            m = [i,j,k,l]
                            iteration1.append(m)
                        else:
                            continue
                    if len(t44)!= 0:
                        for l in t44:
                            if (i[0] not in l) and (i[1] not in l) and (i[2] not in l) and (j not in l) and (k[0] not in l) and (k[1] not in l) and (k[2] not in l):
                                m = [i,j,k,l]
                                iteration1.append(m)
                            else:
                                continue
                    else:
                        continue
                else:
                    continue
            if len(t34)!= 0:
                for k in t33:
                    if (k[0] not in i) and (k[1] not in i) and (i[2] not in k) and (j not in k):
                        for l in t41:
                            if (l not in i) and l != j and (l not in k):
                                m = [i,j,k,l]
                                iteration1.append(m)
                            else:
                                continue
                        for l in t42:
                            if (l[0] not in i) and (l[1] not in i) and (j not in l) and (l[0] not in k) and (l[1] not in k):
                                m = [i,j,k,l]
                                iteration1.append(m)
                            else:
                                continue
                        for l in t43:
                            if (i[0] not in l) and (i[1] not in l) and (i[2] not in l) and (j not in l) and (k[0] not in l) and (k[1] not in l) and (k[2] not in l) and (k[3] not in l):
                                m = [i,j,k,l]
                                iteration1.append(m)
                            else:
                                continue
                        if len(t44)!= 0:
                            for l in t44:
                                if (i[0] not in l) and (i[1] not in l) and (i[2] not in l) and (j not in l) and (k[0] not in l) and (k[1] not in l) and (k[2] not in l) and (k[3] not in l):
                                    m = [i,j,k,l]
                                    iteration1.append(m)
                                else:
                                    continue
                        else:
                            continue
                    else:
                        continue
            else:
                continue
        else:
            continue

    # Now the value of j is in t22
    for j in t22:
        if (j[0] not in i) and (j[1] not in i):
            for k in t31:
                if (k not in i) and (k not in j):
                    for l in t41:
                        if (l not in i) and (l not in j) and l != k:
                            m = [i,j,k,l]
                            iteration1.append(m)
                        else:
                            continue
                    for l in t42:
                        if (l[0] not in i) and (l[1] not in i) and (j[0] not in l) and (j[1] not in l) and (k not in l):
                            m = [i,j,k,l]
                            iteration1.append(m)
                        else:
                            continue
                    for l in t43:
                        if (i[0] not in l) and (i[1] not in l) and (i[2] not in l) and (j[0] not in l) and (j[1] not in l) and (k not in l):
                            m = [i,j,k,l]
                            iteration1.append(m)
                        else:
                            continue
                    if len(t44)!= 0:
                        for l in t44:
                            if (i[0] not in l) and (i[1] not in l) and (i[2] not in l) and (j[0] not in l) and (j[1] not in l) and (k not in l):
                                m = [i,j,k,l]
                                iteration1.append(m)
                            else:
                                continue
                    else:
                        continue
                else:
                    continue
            for k in t32:
                if (k[0] not in i) and (k[1] not in i) and (j[0] not in k) and (j[1] not in k):
                    for l in t41:
                        if (l not in i) and (l not in j) and (l not in k):
                            m = [i,j,k,l]
                            iteration1.append(m)
                        else:
                            continue
                    for l in t42:
                        if (l[0] not in i) and (l[1] not in i) and (j[0] not in l) and (j[1] not in l) and (k[0] not in l) and (k[1] not in l):
                            m = [i,j,k,l]
                            iteration1.append(m)
                        else:
                            continue
                    for l in t43:
                        if (i[0] not in l) and (i[1] not in l) and (i[2] not in l) and (j[0] not in l) and (j[1] not in l) and (k[0] not in l) and (k[1] not in l):
                            m = [i,j,k,l]
                            iteration1.append(m)
                        else:
                            continue
                    if len(t44)!= 0:
                        for l in t44:
                            if (i[0] not in l) and (i[1] not in l) and (i[2] not in l) and (j[0] not in l) and (j[1] not in l) and (k[0] not in l) and (k[1] not in l):
                                m = [i,j,k,l]
                                iteration1.append(m)
                            else:
                                continue
                    else:
                        continue
                else:
                    continue
            for k in t33:
                if (i[0] not in k) and (i[1] not in k) and (i[2] not in k) and (j[0] not in k) and (j[1] not in k):
                    for l in t41:
                        if (l not in i) and (l not in j) and (l not in k):
                            m = [i,j,k,l]
                            iteration1.append(m)
                        else:
                            continue
                    for l in t42:
                        if (l[0] not in i) and (l[1] not in i) and (j[0] not in l) and (j[1] not in l) and (k[0] not in l) and (k[1] not in l) and (k[2] not in l):
                            m = [i,j,k,l]
                            iteration1.append(m)
                        else:
                            continue
                    for l in t43:
                        if (i[0] not in l) and (i[1] not in l) and (i[2] not in l) and (j[0] not in l) and (j[1] not in l) and (k[0] not in l) and (k[1] not in l) and (k[2] not in l):
                            m = [i,j,k,l]
                            iteration1.append(m)
                        else:
                            continue
                    if len(t44)!= 0:
                        for l in t44:
                            if (i[0] not in l) and (i[1] not in l) and (i[2] not in l) and (j[0] not in l) and (j[1] not in l) and (k[0] not in l) and (k[1] not in l) and (k[2] not in l):
                                m = [i,j,k,l]
                                iteration1.append(m)
                            else:
                                continue
                    else:
                        continue
                else:
                    continue
            if len(t34)!= 0:
                for k in t34:
                    if (i[0] not in k) and (i[1] not in k) and (i[2] not in k) and (j[0] not in k) and (j[1] not in k):
                        for l in t41:
                            if (l not in i) and (l not in j) and (l not in k):
                                m = [i,j,k,l]
                                iteration1.append(m)
                            else:
                                continue
                        for l in t42:
                            if (l[0] not in i) and (l[1] not in i) and (j[0] not in l) and (j[1] not in l) and (l[0] not in k) and (l[1] not in k):
                                m = [i,j,k,l]
                                iteration1.append(m)
                            else:
                                continue
                        for l in t43:
                            if (i[0] not in l) and (i[1] not in l) and (i[2] not in l) and (j[0] not in l) and (j[1] not in l) and (k[0] not in l) and (k[1] not in l) and (k[2] not in l) and (k[3] not in l):
                                m = [i,j,k,l]
                                iteration1.append(m)
                            else:
                                continue
                        if len(t44)!= 0:
                            for l in t44:
                                if (i[0] not in l) and (i[1] not in l) and (i[2] not in l) and (j[0] not in l) and (j[1] not in l) and (k[0] not in l) and (k[1] not in l) and (k[2] not in l) and (k[3] not in l):
                                    m = [i,j,k,l]
                                    iteration1.append(m)
                                else:
                                    continue
                        else:
                            continue
                    else:
                        continue
            else:
                continue
        else:
            continue        

    # Now the value of j is in t23
    for j in t23:
        if (i[0] not in j) and (i[1] not in j) and (i[2] not in j):
            for k in t31:
                if (k not in i) and (k not in j):
                    for l in t41:
                        if (l not in i) and (l not in j) and l != k:
                            m = [i,j,k,l]
                            iteration1.append(m)
                        else:
                            continue
                    for l in t42:
                        if (l[0] not in i) and (l[1] not in i) and (l[0] not in j) and (l[1] not in j) and (k not in l):
                            m = [i,j,k,l]
                            iteration1.append(m)
                        else:
                            continue
                    for l in t43:
                        if (i[0] not in l) and (i[1] not in l) and (i[2] not in l) and (j[0] not in l) and (j[1] not in l) and (j[2] not in l) and (k not in l):
                            m = [i,j,k,l]
                            iteration1.append(m)
                        else:
                            continue
                    if len(t44)!= 0:
                        for l in t44:
                            if (i[0] not in l) and (i[1] not in l) and (i[2] not in l) and (j[0] not in l) and (j[1] not in l) and (j[2] not in l) and (k not in l):
                                m = [i,j,k,l]
                                iteration1.append(m)
                            else:
                                continue
                    else:
                        continue
                else:
                    continue
            for k in t32:
                if (k[0] not in i) and (k[1] not in i) and (k[0] not in j) and (k[1] not in j):
                    for l in t41:
                        if (l not in i) and (l not in j) and (l not in k):
                            m = [i,j,k,l]
                            iteration1.append(m)
                        else:
                            continue
                    for l in t42:
                        if (l[0] not in i) and (l[1] not in i) and (l[0] not in j) and (l[1] not in j) and (k[0] not in l) and (k[1] not in l):
                            m = [i,j,k,l]
                            iteration1.append(m)
                        else:
                            continue
                    for l in t43:
                        if (i[0] not in l) and (i[1] not in l) and (i[2] not in l) and (j[0] not in l) and (j[1] not in l) and (j[2] not in l) and (k[0] not in l) and (k[1] not in l):
                            m = [i,j,k,l]
                            iteration1.append(m)
                        else:
                            continue
                    if len(t44)!= 0:
                        for l in t44:
                            if (i[0] not in l) and (i[1] not in l) and (i[2] not in l) and (j[0] not in l) and (j[1] not in l) and (j[2] not in l) and (k[0] not in l) and (k[1] not in l):
                                m = [i,j,k,l]
                                iteration1.append(m)
                            else:
                                continue
                    else:
                        continue
                else:
                    continue
            for k in t33:
                if (i[0] not in k) and (i[1] not in k) and (i[2] not in k) and (j[0] not in k) and (j[1] not in k) and (j[2] not in k):
                    for l in t41:
                        if (l not in i) and (l not in j) and (l not in k):
                            m = [i,j,k,l]
                            iteration1.append(m)
                        else:
                            continue
                    for l in t42:
                        if (l[0] not in i) and (l[1] not in i) and (l[0] not in j) and (l[1] not in j) and (k[0] not in l) and (k[1] not in l) and (k[2] not in l):
                            m = [i,j,k,l]
                            iteration1.append(m)
                        else:
                            continue
                    for l in t43:
                        if (i[0] not in l) and (i[1] not in l) and (i[2] not in l) and (j[0] not in l) and (j[1] not in l) and (j[2] not in l) and (k[0] not in l) and (k[1] not in l) and (k[2] not in l):
                            m = [i,j,k,l]
                            iteration1.append(m)
                        else:
                            continue
                    if len(t44)!= 0:
                        for l in t44:
                            if (i[0] not in l) and (i[1] not in l) and (i[2] not in l) and (j[0] not in l) and (j[1] not in l) and (j[2] not in l) and (k[0] not in l) and (k[1] not in l) and (k[2] not in l):
                                m = [i,j,k,l]
                                iteration1.append(m)
                            else:
                                continue
                    else:
                        continue
                else:
                    continue
            if len(t34)!= 0:
                for k in t34:
                    if (i[0] not in k) and (i[1] not in k) and (i[2] not in k) and (j[0] not in k) and (j[1] not in k) and (j[2] not in k):
                        for l in t41:
                            if (l not in i) and (l not in j) and (l not in k):
                                m = [i,j,k,l]
                                iteration1.append(m)
                            else:
                                continue
                        for l in t42:
                            if (l[0] not in i) and (l[1] not in i) and (l[0] not in j) and (l[1] not in j) and (l[0] not in k) and (l[1] not in k):
                                m = [i,j,k,l]
                                iteration1.append(m)
                            else:
                                continue
                        for l in t43:
                            if (i[0] not in l) and (i[1] not in l) and (i[2] not in l) and (j[0] not in l) and (j[1] not in l) and (j[2] not in l) and (k[0] not in l) and (k[1] not in l) and (k[2] not in l) and (k[3] not in l):
                                m = [i,j,k,l]
                                iteration1.append(m)
                            else:
                                continue
                        if len(t44)!= 0:
                            for l in t44:
                                if (i[0] not in l) and (i[1] not in l) and (i[2] not in l) and (j[0] not in l) and (j[1] not in l) and (j[2] not in l) and (k[0] not in l) and (k[1] not in l) and (k[2] not in l) and (k[3] not in l):
                                    m = [i,j,k,l]
                                    iteration1.append(m)
                                else:
                                    continue
                        else:
                            continue
                    else:
                        continue
            else:
                continue
        else:
            continue

    # Now the value of j is in t24
    if len(t24) != 0:
        for j in t24:
            if (i[0] not in j) and (i[1] not in j) and (i[2] not in j):
                for k in t31:
                    if (k not in i) and (k not in j):
                        for l in t41:
                            if (l not in i) and (l not in j) and l != k:
                                m = [i,j,k,l]
                                iteration1.append(m)
                            else:
                                continue
                        for l in t42:
                            if (l[0] not in i) and (l[1] not in i) and (l[0] not in j) and (l[1] not in j) and (k not in l):
                                m = [i,j,k,l]
                                iteration1.append(m)
                            else:
                                continue
                        for l in t43:
                            if (i[0] not in l) and (i[1] not in l) and (i[2] not in l) and (l[0] not in j) and (l[1] not in j) and (l[2] not in j) and (k not in l):
                                m = [i,j,k,l]
                                iteration1.append(m)
                            else:
                                continue
                        if len(t44)!= 0:
                            for l in t44:
                                if (i[0] not in l) and (i[1] not in l) and (i[2] not in l) and (j[0] not in l) and (j[1] not in l) and (j[2] not in l) and (j[3] not in l) and (k not in l):
                                    m = [i,j,k,l]
                                    iteration1.append(m)
                                else:
                                    continue
                        else:
                            continue
                    else:
                        continue
                for k in t32:
                    if (k[0] not in i) and (k[1] not in i) and (k[0] not in j) and (k[1] not in j):
                        for l in t41:
                            if (l not in i) and (l not in j) and (l not in k):
                                m = [i,j,k,l]
                                iteration1.append(m)
                            else:
                                continue
                        for l in t42:
                            if (l[0] not in i) and (l[1] not in i) and (l[0] not in j) and (l[1] not in j) and (k[0] not in l) and (k[1] not in l):
                                m = [i,j,k,l]
                                iteration1.append(m)
                            else:
                                continue
                        for l in t43:
                            if (i[0] not in l) and (i[1] not in l) and (i[2] not in l) and (l[0] not in j) and (l[1] not in j) and (l[2] not in j) and (k[0] not in l) and (k[1] not in l):
                                m = [i,j,k,l]
                                iteration1.append(m)
                            else:
                                continue
                        if len(t44)!= 0:
                            for l in t44:
                                if (i[0] not in l) and (i[1] not in l) and (i[2] not in l) and (j[0] not in l) and (j[1] not in l) and (j[2] not in l) and (j[3] not in l) and (k[0] not in l) and (k[1] not in l):
                                    m = [i,j,k,l]
                                    iteration1.append(m)
                                else:
                                    continue
                        else:
                            continue
                    else:
                        continue
                for k in t33:
                    if (i[0] not in k) and (i[1] not in k) and (i[2] not in k) and (k[0] not in j) and (k[1] not in j) and (k[2] not in j):
                        for l in t41:
                            if (l not in i) and (l not in j) and (l not in k):
                                m = [i,j,k,l]
                                iteration1.append(m)
                            else:
                                continue
                        for l in t42:
                            if (l[0] not in i) and (l[1] not in i) and (l[0] not in j) and (l[1] not in j) and (k[0] not in l) and (k[1] not in l) and (k[2] not in l):
                                m = [i,j,k,l]
                                iteration1.append(m)
                            else:
                                continue
                        for l in t43:
                            if (i[0] not in l) and (i[1] not in l) and (i[2] not in l) and (j[0] not in l) and (j[1] not in l) and (j[2] not in l) and (k[0] not in l) and (k[1] not in l) and (k[2] not in l):
                                m = [i,j,k,l]
                                iteration1.append(m)
                            else:
                                continue
                        if len(t44)!= 0:
                            for l in t44:
                                if (i[0] not in l) and (i[1] not in l) and (i[2] not in l) and (j[0] not in l) and (j[1] not in l) and (j[2] not in l) and (k[0] not in l) and (k[1] not in l) and (k[2] not in l):
                                    m = [i,j,k,l]
                                    iteration1.append(m)
                                else:
                                    continue
                        else:
                            continue
                    else:
                        continue
                if len(t34)!= 0:
                    for k in t34:
                        if (i[0] not in k) and (i[1] not in k) and (i[2] not in k) and (j[0] not in k) and (j[1] not in k) and (j[2] not in k):
                            for l in t41:
                                if (l not in i) and (l not in j) and (l not in k):
                                    m = [i,j,k,l]
                                    iteration1.append(m)
                                else:
                                    continue
                            for l in t42:
                                if (l[0] not in i) and (l[1] not in i) and (l[0] not in j) and (l[1] not in j) and (l[0] not in k) and (l[1] not in k):
                                    m = [i,j,k,l]
                                    iteration1.append(m)
                                else:
                                    continue
                            for l in t43:
                                if (i[0] not in l) and (i[1] not in l) and (i[2] not in l) and (j[0] not in l) and (j[1] not in l) and (j[2] not in l) and (k[0] not in l) and (k[1] not in l) and (k[2] not in l) and (k[3] not in l):
                                    m = [i,j,k,l]
                                    iteration1.append(m)
                                else:
                                    continue
                            if len(t44)!= 0:
                                for l in t44:
                                    if (i[0] not in l) and (i[1] not in l) and (i[2] not in l) and (j[0] not in l) and (j[1] not in l) and (j[2] not in l) and (k[0] not in l) and (k[1] not in l) and (k[2] not in l) and (k[3] not in l):
                                        m = [i,j,k,l]
                                        iteration1.append(m)
                                    else:
                                        continue
                            else:
                                continue
                        else:
                            continue
                else:
                    continue
            else:
                continue
    else:
        continue

##print(len(iteration1))
##for i in iteration1:
##    print(i)

####################################################################################################

coefficient = float(input("Enter Inequality aversion parameter "))
a = []
for i in availablebattery.values():
    a.append(i)
print(atkinsonindex(a,coefficient))
b = []
for i in range(len(iteration1)):
    b.append(atkinsonindex(iteration1[i],coefficient))
c = b.index(max(b))
print(iteration1[c])

####################################################################################################
