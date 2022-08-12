def reverse_str(strs):
    strs_reverse = ''

    for char in strs:
        strs_reverse = char + strs_reverse
    return strs_reverse

strs = 'Reverse this strings'

print(reverse_str(strs))
