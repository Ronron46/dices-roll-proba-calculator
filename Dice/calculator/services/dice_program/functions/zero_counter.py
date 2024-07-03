def zero_counter(number):
    number=str(number)
    count=0
    pow=str(len(number)-1)
    if len(number) > 4:
        number=number[:4]
    for i in range(len(number)):
        if number[len(number)-i-1] == '0':
            count +=1
        else:
            break
    if count == len(number)-1:
        point='.0'
    else:
        point='.'
    res=number[:1] + point + number[1:len(number)-count]+'x' + '10^' + pow 
    return res
    

