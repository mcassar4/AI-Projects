def printCorConnections(locs, cors):
    for cor in cors:
        l1 = cor[:2]
        l2 = cor[2:]
        if l1 in locs and l2 in locs:
            s1 = "(cor-between loc-" + l1[0] + "-" + l1[1] + " loc-" + l2[0] + "-" + l2[1] + " c" + cor + ")"
            s2 = "(cor-between loc-" + l2[0] + "-" + l2[1] + " loc-" + l1[0] + "-" + l1[1] + " c" + cor + ")"
            s3 = "(cor-connected" + " c" + cor + " loc-" + l1[0] + "-" + l1[1] + ")"
            s4 = "(cor-connected" + " c" + cor + " loc-" + l2[0] + "-" + l2[1] + ")"
            print(s1 + "\n" + s2 + "\n" + s3 + "\n" + s4 + "\n")
    return
def printLocks(locks):
    for lock in locks:
        printLock(str(lock[0]), lock[1])
    return

def printLock(cor, col):
    s1 = "(cor-locked c" + cor + ")"
    s2 = "(cor-lock-colour c" + cor + " " + col + ")"
    print(s1 + "\n" + s2 + "\n")

def printKeys(keyList):
    for key in keyList:
        printKey(key[0], key[1], key[2], str(key[3]))
    return

def printKey(name, uses, colour, loc):
    if uses == 2:
        print("(key-two-use " + name + ")")
    elif uses == 1:
        print("(key-one-use " + name + ")")
    
    loc = str(loc)
    s2 = "(key-colour " + name + " " + colour + ")"
    s3 = "(key-at " + name + " loc-" + loc[0] + "-" + loc[1] + ")"

    print(s2 + "\n" + s3 + "\n")
    return

def stringify(locs, cors):
    for cor in range(len(cors)):
        cors[cor] = str(cors[cor])
    for loc in range(len(locs)):
        locs[loc] = str(locs[loc])
    return locs, cors


# Change these for each problem
heroStart = "loc-1-1"
locs = [11, 21, 31, 41, 51, 61, 71]
cors = [1121, 2131, 3141, 4151, 5161, 6171]
locs, cors = stringify(locs, cors)
lockedCors = [
    (1121, "yellow"),
    (2131, "yellow"),
    (3141, "purple"),
    (4151, "green"),
    (5161, "red"),
    (6171, "rainbow")
]
keys = [
    #(name, uses, colour, loc)
    ("key1", 0, "red", 11),
    ("key2", 2, "yellow", 11),
    ("key3", 1, "green", 11),
    ("key4", 1, "purple", 11),
    ("key5", 1, "rainbow", 11),
]


print("; hero starting location")
print("(hero-at "+ heroStart + ")")

print("\n; Corridor connections")
printCorConnections(locs, cors)

print("\n; Locks")
printLocks(lockedCors)

print("\n; Keys")
printKeys(keys)