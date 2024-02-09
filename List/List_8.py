# Initialize lists L and M
L = [int(x) for x in input("Enter elements of list L separated by space: ").split()]
M = [int(x) for x in input("Enter elements of list M separated by space: ").split()]

# Check if the lists are of the same size
if len(L) != len(M):
    print("Lists must be of the same size.")
else:
    # Create a new list N with sums of corresponding elements in L and M
    N = []
    for i in range(len(L)):
        N.append(L[i] + M[i])

    # Display the lists and the resulting sum list
    print("\nList L:", L)
    print("List M:", M)
    print("Sum List N:", N)
