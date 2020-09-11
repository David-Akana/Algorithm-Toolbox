def max_pairwise_product(numbers):
    len_arr = len(numbers)
    if len_arr == 1:
        return numbers[0]
    else:
        max_pos_num = 0
        s_max_pos_num = 0
        max_neg_num = 0
        s_max_neg_num = 0
        for i in range(len_arr):
            if numbers[i] >= 0:
                if numbers[i] >= max_pos_num:
                    s_max_pos_num = max_pos_num
                    max_pos_num = numbers[i]
                elif numbers[i] > s_max_pos_num and numbers[i] < max_pos_num:
                    s_max_pos_num = numbers[i]
                else:
                    pass
            else:
                if numbers[i] <= max_neg_num:
                    s_max_neg_num = max_neg_num
                    max_neg_num = numbers[i]
                elif numbers[i] < s_max_neg_num and numbers[i] > max_neg_num:
                    s_max_neg_num = numbers[i]
        
        pos_prod = max_pos_num * s_max_pos_num
        neg_prod = max_neg_num * s_max_neg_num
        if pos_prod > neg_prod:
            return pos_prod
        else:
            return neg_prod


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))

