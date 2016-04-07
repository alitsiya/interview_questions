# Write a recursive function to compute the Fibonacci sequence. How does the 
# performance of the recursive function compare to that of an iterative version?

def fib_seq(n):
    """
    Non recursive solution
    >>> fib_seq(9)
    [2, 3, 5, 7, 11, 13, 17, 19, 23]
    """

    res = []
    num = 2

    while len(res) < n:
        found = True
        for i in range(2, num):
            if num%i == 0 and num != i:
                found = False

        if found:
            res.append(num)
        num += 1
    return res


def fib_seq_rec(n):
    """Recursive function
    >>> fib_seq_rec(10)
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

    """

    seq = []
    def _seq(seq, curr=2):
        if len(seq) == n:
            return seq
        for i in range(2, curr):
            if curr%i == 0:
                return _seq(seq, curr+1)
        seq.append(curr)
        return _seq(seq, curr+1)


    return _seq(seq)


if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print "\n*** ALL TEST PASSED. AWESOMESAUCE!\n"