def rec_pop(li,adv):
    for i in range(len(li)):
        if li[i][0][0] == 'A' or li[i][0][0] == 'D':
            adv.append(li.pop(i))
            rec_pop(li,adv)
            break