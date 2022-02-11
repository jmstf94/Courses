

def helpLaceStrings(s1, s2, out):
    if s1 == '':
        return out+s2
    if s2 == '':
        return out+s1
    else:
        return helpLaceStrings(s1[1:], s2[1:], out+s1[0]+s2[0])





def laceStringsRecur(s1, s2):
    return helpLaceStrings(s1, s2, '')




print(laceStringsRecur('abc','def'))