def check_table(table, line, line_number):
    """Preliminary check through assembly to find user-defined symbols.

    Any symbols found can then be added to SymbolTable for future use.
    """

    if is_label(line):
        label = label_from_line(line)

        if is_symbol(label):
            table.add_entry(label, line_number)


def is_label(line):
    """Returns whether a line is a label

    line must be already whitespace-stripped"""
    return line.startswith('(')


def label_from_line(line):
    return line.strip('()')


def is_symbol(symbol):
    return not symbol.isdigit()
