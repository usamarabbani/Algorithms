def symmetricTree(p,q):
    if not p and not q:
        return True
    if not p or not q:
        return False
    return (p.value==q.value) && symmetricTree(p.right,q.left) && symmetricTree(p.left,q.right)
