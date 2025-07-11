import string
'''
Helps with sucessfully resolving the effect of the Yu-Gi-Oh card: Simultaneous Equation Cannons
https://www.db.yugioh-card.com/yugiohdb/card_search.action?ope=2&cid=19921
'''
def main():
    
    XYZ = [3, 4, 5]
    Fusion = [1, 2, 3, 4, 5, 6]

    running = True
    while running:
        A = input("Total Cards: ")
        B = input("Levels: ").split()

        if A.lower() == "quit":
            break

        if_possible = False

        if not (7 <= int(A) <= 17):
            print("Can't Resolve")
            continue
        
        tmp = False
        for i in B:
            if (4 <= int(i) <= 11):
                tmp = True
                break
        
        if not tmp:
            print("Can't Resolve")
            continue

        for i in Fusion:
            for j in XYZ:
                if (i + (2*j)) == int(A):
                    for k in B:
                        if i + j == int(k):
                            print("Fusion: " + str(i) + " XYZ: " + str(j))
                            if_possible = True
    
        if not if_possible:
            print("Can't Resolve")
    
        print()    
    return

main()