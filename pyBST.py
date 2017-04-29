#=======================================================================================================#
#=04/10/2017                                                                            Alexander Alava=#
#=pyBST.py                                                                                    U35432961=#
#=                                                                                                     =#
#=      This file provides basic operations for Binary Search Trees using a tuple representation.      =#
#=======================================================================================================#

# Declaring and defining the function that determines if the parameter is a binary tree
def is_bintree(T):
    # Checking the type of the structure is a tuple
    if type(T) is not tuple:
        return False

    # Checking if the structure is empty 
    if T == ():
        return True

    # Checking if the length of the tuple is less than three
    if len(T) != 3:
        return False

    # Checking if the children of the root are binary trees
    if is_bintree(T[1]) and is_bintree(T[2]):
        return True
    
    return False

# Declaring and defining the function that returns the minimum value in the binary search tree 
def bst_min(T):
    # Checking if the tree is empty
    if T == ():
        return None

    # Checking if the left subtree is empty
    if not T[1]:        
        return T[0]
    
    return bst_min(T[1])

# Declaring and defining the function that returns the maximum value in the binary search tree    
def bst_max(T):
    # Checking if the tree is empty
    if T == ():
        return None

    # Checking if the right subtree is empty
    if not T[2]:        
        return T[0]
    
    return bst_max(T[2])

# Declaring and defining the function that determines if the tree is a binary search tree        
def is_bst(T):
    # Checking if the parameter is not a binary tree at all
    if not is_bintree(T):
        return False

    # Checking if the tree is empty
    if T == ():
        return True

    # Checking if the subtrees are binary search trees
    if not is_bst(T[1]) or not is_bst(T[2]):
        return False

    # Checking if both children are empty trees
    if T[1] == () and T[2] == ():
        return True

    # Checking if the right subtree is empty
    if T[2] == ():
        return bst_max(T[1]) < T[0]

     # Checking if the left subtree is empty
    if T[1] == ():
        return T[0] < bst_min(T[2])
    
    return bst_max(T[1]) < T[0] < bst_min(T[2])

# Declaring the function that isearches for a specific node in the tree               
def bst_search(T,x):
    # Checking if the tree is empty
    if T == ():
        return T
    # Checking if the current root is the value being searched for
    if T[0] == x:
        return T
    # Checking if the current root is greater than the value being searched for
    if x < T[0]:
        return bst_search(T[1],x)
    return bst_search(T[2],x)

# Declaring the function that inserts a specific node into the tree
def bst_insert(T,x):
    # Checking if the tree is empty
    if T == ():
        return (x,(),())
    
    # Checking if the value to be inserted is less than the current root 
    elif x < T[0]:
        return (T[0],bst_insert(T[1],x),T[2])
    
    else:
        return (T[0],T[1],bst_insert(T[2],x))

# Declaring the function that deletes the smallest node in the tree
def delete_min(T):
    # Checking if the tree is empty
    if T == ():
        return T
    
    # Checking if the left subtree is empty
    if not T[1]:        
        return T[2]
    
    else:
        return (T[0],delete_min(T[1]),T[2])

# Declaring the function that deletes a specific node in the tree
def bst_delete(T,x):
    assert T, "Deleting value not in tree"

    # Checking if the value to be deleted is less than the current root              
    if x < T[0]:
        return (T[0],bst_delete(T[1],x),T[2])
    
    # Checking if the value to be deleted is greater than the current root 
    elif x > T[0]:
        return (T[0],T[1],bst_delete(T[2],x))
    
    else:
        # Checking if the left child is empty
        if not T[1]:
            return T[2]
        
        # Checking if the right child is empty
        elif not T[2]:
            return T[1]
         
        else:
            return (bst_min(T[2]),T[1],delete_min(T[2]))

# Declaring and defining an overloaded print function for the binary search tree
def print_bintree(T,indent=0):
    # Checking if the current tree or subtree is empty and printing
    if not T:
        print('*')
        return
    
    else:
        # Printing the values of the root and leaves in a special format
        print(T[0])
        print(' '*(indent + len(T[0])-1)+'---', end = '')
        print_bintree(T[1],indent+3)
        print(' '*(indent + len(T[0])-1)+'---', end = '')
        print_bintree(T[2],indent+3)      

# Declaring and defining a specific print space function    
def print_func_space(x):
    print(x,end=' ')

# Declaring and defining the inorder traversal
def inorder(T,f):
    
    # Checking if the tree is a binary search tree
    if not is_bst(T):
        return
    
    # Checking if the tree is empty
    if not T:
        return
    
    # Establishing the respective order of the nodes
    inorder(T[1],f)
    f(T[0])
    inorder(T[2],f)

# Declaring and defining the preorder traversal    
def preorder(T,f):
    
    # Checking if the tree is a binary search tree
    if not is_bst(T):
        return
    
    # Checking if the tree is empty
    if not T:
        return
    
    # Establishing the respective order of the nodes
    f(T[0])
    preorder(T[1],f)
    preorder(T[2],f)	

# Declaring and defining the postorder traversal
def postorder(T,f):
    
    # Checking if the tree is a binary search tree
    if not is_bst(T):
        return
    
    # Checking if the tree is empty
    if not T:
        return
    
    # Establishing the respective order of the nodes
    postorder(T[1],f)
    postorder(T[2],f)
    f(T[0])

# Declaring and defining the function that returns the height of any tree or subtree
def tree_height(T):
    # Checking if the tree is a binary search tree
    if not is_bst(T):
        return
    
    # Checking if the tree is empty
    if T == ():
        return -1
    return 1 + max(tree_height(T[1]), tree_height(T[2]))

# Declaring and defining the function that returns the balance of any tree or subtree
def balance(T):
    # Checking if the tree is a binary search tree 
    if not is_bst(T):
        return
    
    # Checking if the tree is empty
    if T == ():
        return 0
    
    return tree_height(T[1]) - tree_height(T[2])

# Declaring and defining the function that returns the minimum balance of all the subtrees of a tree 
def minBalance(T):
    # Checking if the tree is empty
    if T == ():
        return 0
    
    return min(balance(T), minBalance(T[1]), minBalance(T[2]))

# Declaring and defining the function that returns the maximum balance of all the subtrees of a tree
def maxBalance(T):
    # Checking if the tree is empty
    if T == ():
        return 0
    
    return max(balance(T), maxBalance(T[1]), maxBalance(T[2]))

# Declaring and defining the function that determines if the tree inputted is avl or not
def is_avl(T):
    # Checking if the maximum and minimum balance are within the avl bounds
    if -1 <= maxBalance(T) <= 1 and -1 <= minBalance(T) <= 1:
        return True
    
    return False

# Tests for all the functions above
if __name__ == '__main__':
    
    # Tests for K
    K = ()   
    for x in ['Joe','Bob', 'Phil', 'Paul', 'Marc', 'Jean', 'Jerry', 'Alice', 'Anne']:
        K = bst_insert(K,x)

    print('\nPrint full tree\n')
    print_bintree(K)

    print('\nTree elements in inorder:')
    inorder(K,print_func_space)
    print()

    print("\nDelete Bob and print tree\n")
    K = bst_delete(K,'Bob')
    print_bintree(K)
    print()

    print("\nPrint subtree at 'Phil'\n")
    print_bintree(bst_search(K,'Phil'))
    print()

    print("\nTree elements in preorder: ")
    preorder(K,print_func_space)
    print()

    print("\nTree elements in postorder:" )
    postorder(K,print_func_space)
    print()

    print("\nTree height: ")
    print(tree_height(K))

    print("\nBalance of the tree: ")
    print(balance(K))

    print("\nMinimum balance of the tree: ")
    print(minBalance(K))

    print("\nMaximum balance of the tree: ")
    print(maxBalance(K))

    print("\nIs it an AVL tree?: ")
    print(is_avl(K))

    # Tests for num
    num = ()
    for x in ['0','1', '2', '3', '4', '5', '6', '7', '8']:
        num = bst_insert(num,x)

    print('\nPrint full tree\n')
    print_bintree(num)

    print('\nTree elements in inorder: ')
    inorder(num,print_func_space)
    print()

    print("\nTree elements in preorder: ")
    preorder(num,print_func_space)
    print()
    
    print("\nTree elements in preorder: ")
    preorder(num,print_func_space)
    print()

    print("\nTree elements in postorder:" )
    postorder(num,print_func_space)
    print()

    print("\nTree height: ")
    print(tree_height(num))

    print("\nBalance of the tree: ")
    print(balance(num))

    print("\nMinimum balance of the tree: ")
    print(minBalance(num))

    print("\nMaximum balance of the tree: ")
    print(maxBalance(num))

    print("\nIs it  an AVL tree?: ")
    print(is_avl(num))

    # Tests for small
    small = ()
    for x in ['1','0', '2', '3']:
        small = bst_insert(small,x)

    print('\nTree elements in sorted order\n')
    inorder(small,print_func_space)
    print()

    print('\nPrint full tree\n')
    print_bintree(small)
    
    print("\nTree elements in preorder: ")
    preorder(small,print_func_space)
    print()

    print("\nTree elements in postorder:" )
    postorder(small,print_func_space)
    print()

    print("\nTree height: ")
    print(tree_height(small))

    print("\nBalance of the tree: ")
    print(balance(small))

    print("\nMinimum balance of the tree: ")
    print(minBalance(small))

    print("\nMaximum balance of the tree: ")
    print(maxBalance(small))

    print("\nIs it an AVL tree?: ")
    print(is_avl(small))
