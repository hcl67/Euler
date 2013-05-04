'''
This code is to solve the IBM Reasearch May 2012 Puzzle:

There are six sets of jobs. Each set is performed on a different server and each set contains jobs that take 1,2,3,...,10 minutes to run.
Obviously, all six sets would end up in 55 minutes.
Schedule all the sets such that if all six servers start together, on minute 0, a job would end on every minute from 1 to 54, and all six servers would end on minute 55 together.
Please supply the solution as six lines of ten numbers.
A solution for a smaller problem of four sets of six jobs ending every minute from 1 to 20 is:
2 1 5 4 6 3
1 3 6 4 5 2
5 2 4 6 3 1
6 3 4 2 1 5

Solution:

[[1, 2, 3, 5, 4, 6, 7, 8, 9, 10],
[2, 3, 7, 1, 9, 4, 5, 8, 10, 6],
[4, 3, 7, 2, 8, 1, 10, 6, 9, 5],
[8, 9, 3, 10, 2, 1, 5, 4, 6, 7],
[9, 10, 4, 6, 8, 7, 2, 5, 3, 1],
[10, 8, 9, 7, 6, 3, 4, 5, 1, 2]]

Auther: Djinn Lu
Date: 2012/5/6

Key Idea: use recurring method to testing the possible task line, which representing the task finished by which server at each minute,

Function Brief:

trans(tsk_ln,svr_n)

    To translate the task link of each servers into task assignment in each server, used in final print only

    tsk_ln: task line, the one to be recurring 
            eg. '010210234501120235430142215043133520431523540453124554' 
    svr_n: server number, in ibm's puzzle, is 6 (0-5)

check(tsk_ln,svr_n,tsk_lmt,tsk_tot)

    To check whether the task link is valid or not

    tsk_ln: task line
    svr_n: server number
    tsk_lmt: task limit, the number of tasks each server would handle
    tsk_tot: total task, the munites to finish all task -1, i.e. =sum (of 1-tsk_lmt) -1

find(tsk_ln,svr_n,tsk_lmt,cur_tsk,tsk_tot):

    The recurring function, simply assign the next server to current tsk_ln, and if valid, find the next server based on new tsk_ln;
    if all server assignment is invalid, roll back to previous tsk_ln

    tsk_ln: task line
    svr_n: server number
    tsk_lmt: task limit, the number of tasks each server would handle
    cur_tsk: current task, the prograss of recurring, once cur_tsk=tsk_tot, the tsk_ln would be the solution
    tsk_tot: total task, the munites to finish all task -1, i.e. =sum (of 1-tsk_lmt) -1


'''

def trans(tsk_ln,svr_n):
    k=1
    svr_tsk=[[] for i in range(svr_n)]
    svr_lst=[0 for i in range(svr_n)]
    for j in tsk_ln:
        svr_tsk[int(j)].append(k-svr_lst[int(j)])
        svr_lst[int(j)]=k
        k=k+1
    for j in range(svr_n):
        svr_tsk[j].append(k-svr_lst[j])
    return svr_tsk

def check(tsk_ln,svr_n,tsk_lmt,tsk_tot):
    k=1
    print(tsk_ln)
    svr_tsk=[[] for i in range(svr_n)]
    svr_lst=[0 for i in range(svr_n)]
    for j in tsk_ln:
        svr_tsk[int(j)].append(k-svr_lst[int(j)])
        svr_lst[int(j)]=k
        k=k+1
    if k>tsk_tot:    
        for j in range(svr_n):
            svr_tsk[j].append(k-svr_lst[j])
    svr_tsk_1=[sorted(i) for i in svr_tsk]
    for i in svr_tsk_1:
        if int(len(tsk_ln)/tsk_lmt)>len(i):
            return -1
        if len(i)>0:
            if i[-1]>tsk_lmt:
                return -1
            if len(i)>1:
                for j in range(1,len(i)):
                    if i[j-1]==i[j]:
                        return -1
    return 1
    
def find(tsk_ln,svr_n,tsk_lmt,cur_tsk,tsk_tot):
    if cur_tsk==tsk_tot:
        print(trans(tsk_ln,svr_n))
        return 1
    else:
        for i in range(svr_n):
            if check(tsk_ln+str(i),svr_n,tsk_lmt,tsk_tot)==1:
                if find(tsk_ln+str(i),svr_n,tsk_lmt,cur_tsk+1,tsk_tot)==1:
                    return 1
        if i==svr_n:
            return -1

find('0',6,10,1,54)
