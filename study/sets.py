set1 = set(['White', 'Black', 'Red'])
set2 = set(['Red', 'Green'])

def det(let):
    if let in set2:
        return False
    else:
        return True

print(list(filter(det, set1)))


# Simply:
# print(set1-set2)