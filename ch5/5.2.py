def convert_fraction_binary(fraction):
    if fraction >= 1 or fraction <= 0:
        return 'ERROR; cannot have >= 1 or <= 0'
    result = '0.'
    fraction_adj = fraction * 2
    while fraction_adj != 0:
        if fraction_adj >= 1:
            result += '1'
        else:
            result += '0'
        fraction_adj = (fraction_adj % 1) * 2
    return result
