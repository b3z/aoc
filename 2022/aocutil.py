import subprocess


def cp(s):
    subprocess.Popen(["pbcopy"], stdin=subprocess.PIPE).communicate(
        bytes(str(s), encoding="ascii")
    )


def inp(s="input"):
    return open(s).readlines()


def toCharArray(xs):
    for c in range(len(xs)):
        xs[c] = [char for char in xs[c]]
    return xs
