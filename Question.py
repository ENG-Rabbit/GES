def Quest(Role = "",*args):
    try:
        item = args[0]
    except:
        item = ""
    if Role == "sub":
        qu = "چه کسی باید {}؟".format(item)
    elif Role == "place":
        qu = "کجا باید {}؟".format(item)
    return input(qu)
#print(Quest("place"))
