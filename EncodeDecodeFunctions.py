def encoder(password)
    result = ''
    for char in password:
        if int(char) >=7:
            char = str(int(char) - 7)
        else:
            char = str(3 + int(char))
        result += char

    return result

def decoder(password):
    result = ''
    for char in password:
        if int(char) <= 2:
            char = str(int(char) + 7)
        else:
            char = str(int(char) - 3)
        result += char

    return result



