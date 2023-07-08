from mapp import mapp


def init():
    for x in range(0, 599):
        mapp.append([])
        for y in range(0, 999):
            mapp[x].append([0, 0, 0])
