def derivate(p):
    '''Derivate polynomials.'''
    sign = [i for i in p if i in "+-"]
    terms = [term.strip() for term in p.split("+")]
    powers = [term[term.rfind("*")+1:] for term in terms]
    #Normalize len of sign
    if len(sign) < len(powers):
        for i in range(len(powers)-len(sign)):
            sign.append(" ")
    new_p = ""
    for i in range(len(powers)):
        new_p += powers[i]+"*"+terms[i][:terms[i].rfind("*")+1]+str(int(powers[i])-1) + sign[i]
    return new_p
