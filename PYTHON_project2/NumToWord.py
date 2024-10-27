def num2word(num):

    under_20=['Zero','One','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Eleven','Twevel','Thirteen','Fourteen','Fifteen','Sixteen','Seventeen','Eighteen','Ninteen']
    tens=['Twenty','Thirty','Fourty','Fifty','Sixty','Seventy','Eighty','Ninty']
    above_100={100:'Hundred',1000:'Thousand',100000:'Million',10000000:'Billion'}

    if num<20:
        return under_20[num]
    if num<100:
        return tens[(int)(num/10)-2]+(''if num%10==0 else ' '+under_20[num%10])
    pivate=max([key for key in above_100.keys() if key<=num])
    return num2word((int)(num/pivate))+' '+above_100[pivate]+('' if num%pivate==0 else ' '+num2word(num%pivate))
print(num2word(1409303))
