def column(str_1,str_2,F):
    if F:
        num_1 = str_1
        num_2 = str_2
    else:
        num_1 = str_2
        num_2 = str_1
    if len(num_1) == 1 and len(num_2) == 1 and int(num_1[0]) == 0:
        return num_2
    else:
        return num_1
        
        
    for i in range(len(num_1)-1,len(num_1)-len(num_2)-1,-1):
        for j in range(len(num_2)-1,-1,-1):
            if  int(num_1[i]) - int(num_2[j]) == 0:
                num_1[i] = '0'
                del num_2[j]
                break
            elif int(num_1[i]) >= int(num_2[j]):
                num = int(num_1[i]) - int(num_2[j])
                num_1[i] = str(num)
                del num_2[j]
                break
            elif int(num_1[i]) < int(num_2[j]) and int(num_1[i-1]) > 0:
                num = (int(num_1[i]) + 10) - int(num_2[j])
                num_1[i-1] =int(num_1[i-1]) - 1
                num_1[i] = str(num)
                del num_2[j]
                break
            elif int(num_1[i]) < int(num_2[j]) and int(num_1[i-1]) == 0:
                for n in range(i-1,-1,-1):
                    if int(num_1[n]) !=0:
                        idx = n
                        break
                num = (int(num_1[i]) + 10) - int(num_2[j])
                num_1[idx] =str(int(num_1[idx]) - 1)
                num_1[i] = str(num)
                del num_2[j]
                for k in range(i,idx,-1):
                    if int(num_1[k]) == 0:
                        num_1[k] = '9'
                break
    return num_1
    




def BigMinus(s1, s2):
    n_1 = list(s1)
    n_2 = list(s2)
    result_list = []
    if len(n_1) > len(n_2):
        result = ''.join(column(n_1,n_2,True))
        return result
    else:
        result = ''.join(column(n_1,n_2,False))
        return result