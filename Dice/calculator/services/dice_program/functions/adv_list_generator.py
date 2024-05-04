def adv_list_generator(dice_list):
    l_adv=[]
    for i in range(len(dice_list)):
                if dice_list[i][0][0] == 'A' :
                    temp=dice_list[i][0].split('A')
                    temp1=[]
                    temp2=[]
                    temp1.append(int(temp[1]))
                    for face in range(int(dice_list[i][1])):
                        temp2.append(2*face+1)
                    temp1.append(temp2)
                    l_adv.append(temp1)
                else:
                    temp=dice_list[i][0].split('D')
                    temp1=[]
                    temp2=[]
                    temp1.append(int(temp[1]))
                    for face in range(int(dice_list[i][1])):
                        temp2.append(2*(int(dice_list[i][1])-face-1)+1)
                    temp1.append(temp2)
                    l_adv.append(temp1)
    return l_adv