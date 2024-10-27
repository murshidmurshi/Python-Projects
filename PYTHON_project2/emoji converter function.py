def emoji_converter(message):
    words=message.split()
    emoji={
        ':)':'😊',
        ':(':'☹'
    }
    output=''
    for word in words:
        output+=emoji.get(word,word)+' '
    return output


message=input('>')
result=emoji_converter(message)
print(result)
