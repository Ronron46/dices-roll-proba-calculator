from functions.Pascal import pascal

def diver(n_dice,dice,mem,tab,dice_list):
    aux_list=dice_list.copy()
    actual_face = dice 
    if len(aux_list) >=2:
        if int(aux_list[1][1]) == actual_face:
            n_dice += int(aux_list[1][0])
            aux_list.pop(1)   
    dice -= 1
    if dice == 0:
        return { actual_face*n_dice : 1}
    else:
        output={}
        for k in range(n_dice+1):
            if (n_dice-k,dice) not in mem:
                mem[n_dice-k,dice]=diver(n_dice-k,dice,mem,tab,aux_list)
            for value, weight in mem[n_dice-k,dice].items():
                value += actual_face *k
                weight *= pascal(n_dice,k,tab)
                if value in output:
                    output[value] += weight
                else:
                    output[value] = weight
        return  output