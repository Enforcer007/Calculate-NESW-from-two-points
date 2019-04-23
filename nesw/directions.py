_mapping = { 1:'NE',2:'NW',3:'SW',4:'SE'}


def NESW(cord, ref):
    # print(cord,ref)
    diff = cord[0] - ref[0], cord[1] - ref[1]
    # print(diff)
    if diff[0] >= 0 and diff[1] >= 0:
        return _mapping[1]
    elif diff[0] >= 0 and diff[1] < 0:
        return _mapping[2]
    elif diff[0] <= 0 and diff[1] < 0:
        return _mapping[3]
    else:
        return _mapping[4]