# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 00:25:49 2019

@author: Hyun Seo
"""

import numpy as np


lat = [[8,0,0,0,0,0,0,0,0],
       [0,0,3,6,0,0,0,0,0],
       [0,7,0,0,9,0,2,0,0],
       [0,5,0,0,0,7,0,0,0],
       [0,0,0,0,4,5,7,0,0],
       [0,0,0,1,0,0,0,3,0],
       [0,0,1,0,0,0,0,6,8],
       [0,0,8,5,0,0,0,1,0],
       [0,9,0,0,0,0,4,0,0]]

temp = list(map(lambda i:int(i),input().split()))


lat = []
for i in range(9):
    lat.append(temp[9*i:9*(i+1)])

sol = [[[1]*9]*9]*9

lat = np.array(lat)
sol = np.array(sol)



for i in range(9):
    for j in range(9):
        if lat[i][j] != 0:
            sol[i][j] = [0]*9
            sol[i][j][lat[i][j]-1] = 3
            

def sol_to_lat(sol):
    temp = []
    a = []
    for i in sol:
        for j in list(i):
            if 3 in list(j):
                a.append(list(j).index(3)+1)
            else:
                a.append(0)
        temp.append(a)
        a = []
    return temp


def array_to_list(a):
    temp = []
    temp1 = []
    for i in a:
        for j in i:
            temp1.append(list(j))
        temp.append(temp1)
        temp1 = []
    return temp


def isdiff(new, sol):
    p = (new == sol)
    for i in p:
        for j in i:
            if False in j:
                return True
    return False


def garo_check(sol):   #3 있으면 그 행에 1을 없앰
    for i in range(9): #i가 행
        for j in range(9): #j가 숫자
            if 3 in sol[i][:,j]:
                a = np.where(sol[i][:,j] == 3)[0][0]
                for k in range(9):
                    sol[i][k][j] = 0
                sol[i][a][j] = 3
    return sol
                
                
def sero_check(sol):  #3 있으면 그 열에 1을 없앰
    for i in range(9): #i가 열
        for j in range(9): #j가 숫자
            if 3 in sol[:,i][:,j]:
                a = np.where(sol[:,i][:,j] == 3)[0][0]
                for k in range(9):
                    sol[k][i][j] = 0
                sol[a][i][j] = 3
    return sol


def nemo_check(sol):  #3 있으면 그 네모에 1을 없앰
    for i in range(3):
        for j in range(3):
            temp = []
            for k in sol[3*i:3*(i+1),3*j:3*(j+1)]:
                temp += [list(l) for l in list(k)]
            nemo = np.array(temp)
            for k in range(9):
                if 3 in nemo[k]:
                    a = np.where(nemo[k] == 3)[0][0] 
                    for l in range(9):
                        nemo[l][a] = 0
                    nemo[k][a] = 3
            for k in range(9):
                sol[3*i+k//3][3*j+k%3] = nemo[k]
    
    return sol
            

def single_check(sol):
    for i in range(3):
        for j in range(3):
            temp = []
            for k in sol[3*i:3*(i+1),3*j:3*(j+1)]:
                temp += [list(l) for l in list(k)]
            nemo = np.array(temp)
            for k in range(9):
                p = nemo[:,k]
                if len(np.where(p==1)[0]) == 2 and len(np.where(p==3)[0])==0:
                    asd = np.where(p==1)[0]
                    if asd[0]//3 == asd[1]//3:
                        sol[3*i+asd[0]//3][:,k] = np.array([0]*(3*j+asd[0]%3)+[1]+[0]*(asd[1]-asd[0]-1)+[1]+[0]*(8-3*j-asd[1]%3))
                    elif asd[0]%3 == asd[1]%3:
                        sol[:,3*j+asd[0]%3][:,k] = np.array([0]*(3*i+asd[0]//3)+[1]+[0]*(asd[1]//3-asd[0]//3-1)+[1]+[0]*(8-3*i-asd[1]//3))
                if len(np.where(p==1)[0]) == 3 and len(np.where(p==3)[0])==0:
                    asd = np.where(p==1)[0]
                    if asd[0]//3 == asd[1]//3 and asd[0]//3 == asd[2]//3:
                        sol[3*i+asd[0]//3][:,k] = np.array([0]*(3*j+asd[0]%3)+[1]*3+[0]*(8-3*j-asd[2]%3))
                    elif asd[0]%3 == asd[1]%3 and asd[0]%3 == asd[2]%3:
                        sol[:,3*j+asd[0]%3][:,k] = np.array([0]*(3*i+asd[0]//3)+[1]*3+[0]*(8-3*i-asd[2]//3))
            for k in range(9):
                sol[3*i+k//3][3*j+k%3] = nemo[k]
    sol = fillin(sol)                        
                
    for i in range(9):
        for j in range(9):
            p = sol[i][:,j]
            if len(np.where(p==1)[0]) == 2 and len(np.where(p==3)[0])==0:
                asd = np.where(p==1)[0]
                if asd[0]//3 == asd[1]//3:
                    sol[3*(i//3)][asd[0]-asd[0]%3:asd[0]-asd[0]%3+3][:,j] = np.array([0,0,0])
                    sol[3*(i//3)+1][asd[0]-asd[0]%3:asd[0]-asd[0]%3+3][:,j] = np.array([0,0,0])
                    sol[3*(i//3)+2][asd[0]-asd[0]%3:asd[0]-asd[0]%3+3][:,j] = np.array([0,0,0])
                    sol[i][asd[0]][j] = 1
                    sol[i][asd[1]][j] = 1
            if len(np.where(p==1)[0]) == 3 and len(np.where(p==3)[0])==0:
                asd = np.where(p==1)[0]
                if asd[0]//3 == asd[1]//3 and asd[0]//3 == asd[2]//3:
                    sol[3*(i//3)][asd[0]-asd[0]%3:asd[0]-asd[0]%3+3][:,j] = np.array([0,0,0])
                    sol[3*(i//3)+1][asd[0]-asd[0]%3:asd[0]-asd[0]%3+3][:,j] = np.array([0,0,0])
                    sol[3*(i//3)+2][asd[0]-asd[0]%3:asd[0]-asd[0]%3+3][:,j] = np.array([0,0,0])
                    sol[i][asd[0]][j] = 1
                    sol[i][asd[1]][j] = 1
                    sol[i][asd[2]][j] = 1
    sol = fillin(sol)
                    
    for i in range(9):
        for j in range(9):
            p = sol[:,i][:,j]
            if len(np.where(p==1)[0]) == 2 and len(np.where(p==3)[0])==0:
                asd = np.where(p==1)[0]
                if asd[0]//3 == asd[1]//3:
                    sol[asd[0]-asd[0]%3][i-i%3:i-i%3+3][:,j] = np.array([0,0,0])
                    sol[asd[0]-asd[0]%3+1][i-i%3:i-i%3+3][:,j] = np.array([0,0,0])
                    sol[asd[0]-asd[0]%3+2][i-i%3:i-i%3+3][:,j] = np.array([0,0,0])
                    sol[asd[0]][i][j] = 1
                    sol[asd[1]][i][j] = 1
            if len(np.where(p==1)[0]) == 3 and len(np.where(p==3)[0])==0:
                asd = np.where(p==1)[0]
                if asd[0]//3 == asd[1]//3 and asd[0]//3 == asd[2]//3:
                    sol[asd[0]-asd[0]%3][i-i%3:i-i%3+3][:,j] = np.array([0,0,0])
                    sol[asd[0]-asd[0]%3+1][i-i%3:i-i%3+3][:,j] = np.array([0,0,0])
                    sol[asd[0]-asd[0]%3+2][i-i%3:i-i%3+3][:,j] = np.array([0,0,0])
                    sol[asd[0]][i][j] = 1
                    sol[asd[1]][i][j] = 1
                    sol[asd[2]][i][j] = 1
    sol = fillin(sol)            
                
                
                
                
    return sol


def double_check(sol):
    for i in range(9):
        a = sol[i]
        num = []
        cnt = []
        for j in range(9):
            if len(np.where(a[:,j]==1)[0]) == 2:
                num.append((j,np.where(a[:,j]==1)[0]))
        for k in range(len(num)):
            for j in range(k+1,len(num)):
                if num[k][1][0] == num[j][1][0] and num[k][1][1] == num[j][1][1]:
                    sol[i][:,num[k][0]] = np.array([0]*9)
                    sol[i][:,num[j][0]] = np.array([0]*9)
                    sol[i][num[k][1][0]] = np.array([0]*num[k][0]+[1]+[0]*(num[j][0]-num[k][0]-1)+[1]+[0]*(8-num[j][0]))
                    sol[i][num[k][1][1]] = np.array([0]*num[k][0]+[1]+[0]*(num[j][0]-num[k][0]-1)+[1]+[0]*(8-num[j][0]))
        for j in range(9):
            if len(np.where(a[j] == 1)[0]) == 2:
                cnt.append((j,np.where(a[j] == 1)[0]))
        for k in range(len(cnt)):
            for j in range(k+1,len(cnt)):
                if cnt[k][1][0] == cnt[j][1][0] and cnt[k][1][1] == cnt[j][1][1]:
                    sol[i][:,cnt[k][1][0]] = np.array([0]*cnt[k][0]+[1]+[0]*(cnt[j][0]-cnt[k][0]-1)+[1]+[0]*(8-cnt[j][0]))
                    sol[i][:,cnt[k][1][1]] = np.array([0]*cnt[k][0]+[1]+[0]*(cnt[j][0]-cnt[k][0]-1)+[1]+[0]*(8-cnt[j][0]))
    sol = fillin(sol)
                    
    for i in range(9):
        a = sol[:,i]
        num = []
        cnt = []
        for j in range(9):
            if len(np.where(a[:,j]==1)[0]) == 2:
                num.append((j,np.where(a[:,j]==1)[0]))
        for k in range(len(num)):
            for j in range(k+1,len(num)):
                if num[k][1][0] == num[j][1][0] and num[k][1][1] == num[j][1][1]:
                    sol[:,i][:,num[k][0]] = np.array([0]*9)
                    sol[:,i][:,num[j][0]] = np.array([0]*9)
                    sol[:,i][num[k][1][0]] = np.array([0]*num[k][0]+[1]+[0]*(num[j][0]-num[k][0]-1)+[1]+[0]*(8-num[j][0]))
                    sol[:,i][num[k][1][1]] = np.array([0]*num[k][0]+[1]+[0]*(num[j][0]-num[k][0]-1)+[1]+[0]*(8-num[j][0]))
        for j in range(9):
            if len(np.where(a[j] == 1)[0]) == 2:
                cnt.append((j,np.where(a[j] == 1)[0]))
        for k in range(len(cnt)):
            for j in range(k+1,len(cnt)):
                if cnt[k][1][0] == cnt[j][1][0] and cnt[k][1][1] == cnt[j][1][1]:
                    sol[:,i][:,cnt[k][1][0]] = np.array([0]*cnt[k][0]+[1]+[0]*(cnt[j][0]-cnt[k][0]-1)+[1]+[0]*(8-cnt[j][0]))
                    sol[:,i][:,cnt[k][1][1]] = np.array([0]*cnt[k][0]+[1]+[0]*(cnt[j][0]-cnt[k][0]-1)+[1]+[0]*(8-cnt[j][0]))
    sol = fillin(sol)
                    
    for i in range(3):
        for m in range(3):
            temp = []
            for k in sol[3*i:3*(i+1),3*m:3*(m+1)]:
                temp += [list(l) for l in list(k)]
            a = np.array(temp)
            num = []
            cnt = []
            for j in range(9):
                if len(np.where(a[:,j]==1)[0]) == 2:
                    num.append((j,np.where(a[:,j]==1)[0]))
            for k in range(len(num)):
                for j in range(k+1,len(num)):
                    if num[k][1][0] == num[j][1][0] and num[k][1][1] == num[j][1][1]:
                        a[:,num[k][0]] = np.array([0]*9)
                        a[:,num[j][0]] = np.array([0]*9)
                        a[num[k][1][0]] = np.array([0]*num[k][0]+[1]+[0]*(num[j][0]-num[k][0]-1)+[1]+[0]*(8-num[j][0]))
                        a[num[k][1][1]] = np.array([0]*num[k][0]+[1]+[0]*(num[j][0]-num[k][0]-1)+[1]+[0]*(8-num[j][0]))
            for j in range(9):
                if len(np.where(a[j] == 1)[0]) == 2:
                    cnt.append((j,np.where(a[j] == 1)[0]))
            for k in range(len(cnt)):
                for j in range(k+1,len(cnt)):
                    if cnt[k][1][0] == cnt[j][1][0] and cnt[k][1][1] == cnt[j][1][1]:
                        a[:,cnt[k][1][0]] = np.array([0]*cnt[k][0]+[1]+[0]*(cnt[j][0]-cnt[k][0]-1)+[1]+[0]*(8-cnt[j][0]))
                        a[:,cnt[k][1][1]] = np.array([0]*cnt[k][0]+[1]+[0]*(cnt[j][0]-cnt[k][0]-1)+[1]+[0]*(8-cnt[j][0]))
            for k in range(9):
                sol[3*i+k//3][3*m+k%3] = a[k]
    sol = fillin(sol)
        

    return sol


def triple_check(sol):
    
    return sol


def great_check(sol,last):
    k = (0,0,0,0)

    for i in range(last+1,81):
        if k == (0,0,0,0):
            if len(np.where(sol[i//9][i%9] == 1)[0]) == 2:
                k = (i//9,i%9,np.where(sol[i//9][i%9] == 1)[0][0],np.where(sol[i//9][i%9] == 1)[0][1])
            else:
                continue
        else:
            continue
    
    copy = np.array(sol)
    flag = False
    if not k == (0,0,0,0):
        copy[k[0]][k[1]][k[2]] = 3
        copy[k[0]][k[1]][k[3]] = 0
        b = np.array([[[0]*9]*9]*9)
        copy = garo_check(copy)
        copy = sero_check(copy)
        copy = nemo_check(copy)
        while isdiff(copy,b):
            b = np.array(copy)
            copy = single_check(copy)
            copy = double_check(copy)
            copy = single_check(copy)
            copy = double_check(copy) 
            copy = fillin(copy)
            copy = garo_check(copy)
            copy = sero_check(copy)
            copy = nemo_check(copy)
        
        for i in range(9):
            for j in range(9):
                if len(np.where(copy[i][j]==0)[0])==9: 
                    flag = True
               
    if not k == (0,0,0,0):
        if flag == True:
            sol[k[0]][k[1]][k[2]] = 0
    
        else:
            sol = great_check(sol,k[0]*9+k[1])

        
    return sol
        

def fillin(sol):
    for i in sol:
        for j in i:
            if len(np.where(j==1)[0])+len(np.where(j==2)[0]) == 1 and len(np.where(j==3)[0])==0:
                a = 0
                if len(np.where(j==1)[0])==1:
                    a = np.where(j==1)[0][0]
                else:
                    a = np.where(j==2)[0][0]
                j[a] = 3
    sol = garo_check(sol)
    sol = sero_check(sol)
    sol = nemo_check(sol)
    
    for i in range(9):   #가로
        row = sol[i]
        for j in range(9): #j가 숫자, k가 열번호
            p = row[:,j]
            if len(np.where(p==1)[0])+len(np.where(p==2)[0]) == 1 and len(np.where(p==3)[0])==0:
                a = 0
                if len(np.where(p==1)[0])==1:
                    a = np.where(p==1)[0][0]
                else:
                    a = np.where(p==2)[0][0]
                sol[i][a] = np.array([0]*j+[3]+[0]*(8-j))
    sol = garo_check(sol)
    sol = sero_check(sol)
    sol = nemo_check(sol)
    
    for i in range(9):   #세로
        col = sol[:,i]
        for j in range(9): #j가 숫자, k가 행 번호
            p = col[:,j]
            if len(np.where(p==1)[0])+len(np.where(p==2)[0]) == 1 and len(np.where(p==3)[0])==0:
                a = 0
                if len(np.where(p==1)[0])==1:
                    a = np.where(p==1)[0][0]
                else:
                    a = np.where(p==2)[0][0]
                sol[a][i] = np.array([0]*j+[3]+[0]*(8-j))
    sol = garo_check(sol)
    sol = sero_check(sol)
    sol = nemo_check(sol)
    
    for i in range(3):
        for j in range(3):
            temp = []
            for k in sol[3*i:3*(i+1),3*j:3*(j+1)]:
                temp += [list(l) for l in list(k)]
            nemo = np.array(temp)
            for k in range(9):
                p = nemo[:,k]
                if len(np.where(p==1)[0])+len(np.where(p==2)[0]) == 1 and len(np.where(p==3)[0])==0:
                    a = 0
                    if len(np.where(p==1)[0])==1:
                        a = np.where(p==1)[0][0]
                    else:
                        a = np.where(p==2)[0][0]
                    sol[3*i+a//3][3*j+a%3] = np.array([0]*k+[3]+[0]*(8-k))
    sol = garo_check(sol)
    sol = sero_check(sol)
    sol = nemo_check(sol)
                    
    return sol




new = np.array(sol)
a = np.array([[[0]*9]*9]*9)
cnt = 0


while isdiff(new,a):
    print('solving...')
    cnt+=1
    a = np.array(new)
    new = single_check(new)
    new = double_check(new)   
    new = single_check(new)
    new = double_check(new)   
    new = fillin(new)
    new = garo_check(new)
    new = sero_check(new)
    new = nemo_check(new)
    
    if not isdiff(new,a):
        new = great_check(new,-1)

sol = np.array(new)

for i in sol:
    for j in i:
        print(j,end='')
    print('\n')
print()

print(cnt)



for i in sol_to_lat(sol):
    print(i)