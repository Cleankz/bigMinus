def BigMinus(s1, s2):
    num_1 = list(s1)
    num_2 = list(s2)
    result_list = []
    
    
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
            elif int(num_1[i]) < int(num_2[j]) and int(num_1[i-1]) == 0:
                for n in range(i-1,-1,-1):
                    if int(num_1[n]) !=0:
                        idx = n
                        break
                num = (int(num_1[i]) + 10) - int(num_2[j])
                num_1[idx] =int(num_1[idx]) - 1
                num_1[i] = str(num)
                for k in range(i,idx,-1):
                    if int(num_1[k]) == 0:
                        num_1[k] = '9'
                


            
                
            
    return num_1
print(BigMinus('12345678910110000006','123456'))