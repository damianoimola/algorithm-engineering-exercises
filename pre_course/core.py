

def max_sum_subvector(vec):
    """
        Get the sub-vector of @vec that has the biggest sum of their numbers
    :param vec: integer array
    :return: array
    """
    l = len(vec)
    assert l != 0, "Empty vector"
    tmp_vec = []
    max_vec = [vec[0]]
    for i in range(0, l):
        tmp_vec = []
        for j in range(i, l):
            tmp_vec = vec[i:j+1]
            if sum(tmp_vec) > sum(max_vec):
                max_vec = tmp_vec

    return max_vec, sum(max_vec)

def fibonacci(n):
    """
        Computes recursively the Fibonacci's Sequence
    :param n: Number
    :return: Integer
    """
    assert  n > 0, "Fibonacci starts from n=1"
    if n <= 2:
        return [1]
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def sum_1(n):
    """
        Computes recursively the sum of th first @n numbers
    :param n: Number
    :return: Integer
    """
    if n == 0:
        return 0
    elif n > 0:
        return n + sum_1(n-1)
    elif n < 0:
        return n + sum_1(n+1)

def sum_2(n):
    """
        Computes the sum of th first @n numbers
    :param n: Number
    :return: Integer
    """
    return n(n+1) / 2

def hanoi_towers(n):
    """
        Compute recursively the number of steps to solve the Hanoi Tower Puzzele
    :param n: Number of plates
    :return: Integer (it should be a power of 2)
    """
    print("TODO")

