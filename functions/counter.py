def diver(depth,max_depth, node, dices_list):
    if depth==max_depth:
        yield(node)
    else:
        for i in dices_list[depth]:
            yield from diver(depth + 1,max_depth,node + i,dices_list)


    