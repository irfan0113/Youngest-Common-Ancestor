class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None


def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    depthOne = getDepth(descendantOne,topAncestor)
    depthTwo = getDepth(descendantTwo,topAncestor)

    if depthOne > depthTwo:
        return backtrackAncestralTree(descendantOne,descendantTwo,depthOne-depthTwo)

    else:
        return backtrackAncestralTree(descendantTwo,descendantOne,depthTwo-depthOne)
    pass

def getDepth(descendant, topAncestor):
    depth = 0
    while descendant!=topAncestor:
        depth += 1
        descendant = descendant.ancestor
    return depth

def backtrackAncestralTree(lowerDescendent,higherDescendant,diff):
    while diff>0:
        lowerDescendent = lowerDescendent.ancestor
        diff -= 1
    while lowerDescendent!=higherDescendant:
        lowerDescendent = lowerDescendent.ancestor
        higherDescendant = higherDescendant.ancestor
    return lowerDescendent

