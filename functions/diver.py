from functions.Pascal import pascal

def diver(n_dice,dice,val_min,mem,tab):
    actual_face = dice
    dice -= 1
    if dice == 0:
        return { actual_face*n_dice : 1}
    else:
        output={}
        for k in range(n_dice+1):
            if (n_dice-k,dice) not in mem:
                mem[n_dice-k,dice]=diver(n_dice-k,dice,val_min,mem,tab)
            for value, weight in mem[n_dice-k,dice].items():
                value += actual_face *k
                weight *= pascal(n_dice,k,tab)
                if value in output:
                    output[value] += weight
                else:
                    output[value] = weight
        return  output