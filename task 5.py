
org_tuples= [('VolleyBall',90), ('Chess',88), ('Football',93), ('Lawn Tennis', 85)] # The given list
org_tuples.sort(key=lambda lst: lst[1]) # sorting using sort predefined function with a key
print(org_tuples)

def sort_key(data):
    return data[1]

org_tuples.sort(key=sort_key)

print(org_tuples)