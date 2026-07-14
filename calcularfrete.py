def frete(estado):
    if(estado == "AL" or estado == "BA" or estado == "CE"):
        frete = 25
        return frete
    elif(estado == "MA" or estado == "PB" or estado == "PE"):
        frete = 40
        return frete
    elif(estado == "PI" or estado == "RN" or estado == "SE"):
        frete = 70
        return frete
    else:
        frete = 150
        return frete