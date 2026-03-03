# CHUNKER:
def chunker(l, n):
    # looping till length l
    for i in range(0, len(l), n): 
        yield l[i:i + n]

# NON-ROUTE FUNCTIONS:
def reverse_me(lst):
    new_lst = lst[::-1]
    return new_lst