# generate all combinations of N items
def powerSet(items):
    N = len(items)
    # enumerate the 2**N possible combinations
    for i in range(2**N):
        combo = []
        for j in range(N):
            # test bit jth of integer i
            if (i >> j) % 2 == 1:
                combo.append(items[j])
        yield combo

def yieldAllCombos(items):
    """
        Generates all combinations of N items into two bags, whereby each
        item is in one or zero bags.

        Yields a tuple, (bag1, bag2), where each bag is represented as a list
        of which item(s) are in each bag.
    """
    """
    How many possible combinations exist for N items into two bags?

    With two bags, there are 3^n  possible combinations available.

    With one bag we determined there were 2^n possible combinations available by
    representing the bag as a list of binary bits, 0 or 1. Since there are N bits,
    and they can be one of two possibilities, there must be  possibilities.

    With two bags there thus must be 3^n possible combinations.
    You can imagine this by representing the two bags as a list of "trinary" bits,
    0, 1, or 2 (a 0 if an item is in neither bag; 1 if it is in bag1; 2 if it is in bag2).
    With the "trinary" bits, there are N trits that can each be one of three possibilities
     - thus there must be 3^n possible combinations.
    """
    N=len(items)
    for i in range(3**N):
        bag1=[]
        bag2=[]
        for j in range(N):
            # test bit jth of integer i
            if (i//(3**j)) % 3 == 1:
                bag1.append(items[j])
            elif (i//(3**j)) % 3 == 2:
                bag2.append(items[j])
        yield (bag1,bag2)
