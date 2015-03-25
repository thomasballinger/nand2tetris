def is_label(line):
    """Returns whether a line is a label

    line must be already whitespace-stripped"""
    return line.startswith('(')


def label_from_line(line):
    return line.strip('()')


def is_symbol(symbol):
    return not symbol.isdigit()
