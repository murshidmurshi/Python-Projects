def num_to_word(num):

    under_20=['Zero','One','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Eleven','Twelve','Thirteen','Fourteen','Fifteen','Sixteen','Seventeen','Eighteen','Ninteen']
    tens=['Twenty','Thirty','Fourty','Fifty','Sixty','Seventy','Eighty','Ninty']
    above_100={100:'hundred',1000:'Thousand',100000:'Million',10000000:'Billion'}
    
    if num<20:
        return under_20[num]
    if num<100:
        return tens[(int)(num/10)-2]+(''if num%10==0 else ' '+under_20[num%10])
    pivot=max(key for key in above_100.keys() if key<=num)
    return num_to_word((int)(num/pivot))+' '+above_100[pivot]+(''if num%pivot==0 else ' '+num_to_word(num%pivot))
print(num_to_word(332))


