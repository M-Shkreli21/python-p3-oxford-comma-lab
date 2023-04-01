def oxford_comma(items):
    if len(items) == 1:
        return ''.join(items)
    elif len(items) == 2:
        return ' and '.join(items)
    else:
        result = ', '.join(str(i) for i in items[:-1])
        result += f", and {items[-1]}"
        return result