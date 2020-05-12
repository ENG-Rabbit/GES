def Quest(Role = "",*args):
    try:
        item = args[0]
    except:
        item = None
    if Role == "sub":
        qu = input("چه کسی باید {}؟".format(item))
    elif Role == "place":
        qu = input("کجا باید {}؟".format(item))
    return qu
print(Quest("place"))
