def second_largest(li):
    max_num = 0
    sec_max = 0
    
    for ele in li:
        if(ele > max_num):
            sec_max = max_num - 1 
            max_num = ele
        elif(ele > sec_max):
            sec_max = ele

    return max_num , sec_max

li =  [20,40,10,100,60]
max_num, sec_max = second_largest(li)
print("Max Number is :",max_num)
print("Second Max Number is:", sec_max)