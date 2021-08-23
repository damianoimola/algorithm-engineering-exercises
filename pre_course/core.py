

def max_sum_subvector(vec):
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
