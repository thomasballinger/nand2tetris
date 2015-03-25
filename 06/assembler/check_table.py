def check_table(table, line, line_number):
    """Preliminary check through assembly to find user-defined symbols.

    Any symbols found can then be added to SymbolTable for future use.
    """

    if is_label(line):
        symbol = line.strip('()')

        if not table.contains(symbol) and not symbol.isdigit():
            table.add_entry(symbol, line_number)


def is_label(line):
    """Returns whether a line is a label

    line must be already whitespace-stripped"""
    return line.startswith('(')
