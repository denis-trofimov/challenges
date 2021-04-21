# 1. File OwnersDICTIONARY   Easy
# Implement a group_by_owners function that:

# Accepts a dictionary containing the file owner name for each file name.
# Returns a dictionary containing a list of file names for each owner name, in any order.
# For example, for dictionary {'Input.txt': 'Randy', 'Code.py': 'Stan', 'Output.txt': 'Randy'} the group_by_owners function should return {'Randy': ['Input.txt', 'Output.txt'], 'Stan': ['Code.py']}.
def group_by_owners(files):
    res = {}
    for k, v in files.items():
        l = res.get(v)
        if l is None:
            res[v] = [k]
        else:
            l.append(k)
            res[v] = l
    return res


if __name__ == "__main__":
    files = {"Input.txt": "Randy", "Code.py": "Stan", "Output.txt": "Randy"}
    print(group_by_owners(files))