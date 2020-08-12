def apend_next_phi(collect, a=0, b=1, counter=0, maxcount=20):
    """
    :param collect: list of numbers phi
    :param a: first phi number
    :param b: second phi number
    :param counter: counting calculated numbers
    :param maxcount: contains maximum iterations
    :return: collect - list with appended phi number
    """

    c = a + b
    collect.append(c)
    counter += 1
    if counter == maxcount:
        return collect
    else:
        apend_next_phi(collect, b, c, counter, maxcount)
    return collect


coll = [0, 1]
res_phi = apend_next_phi(coll)
for i in res_phi:
    print(i)