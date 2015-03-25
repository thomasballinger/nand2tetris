from check_table import is_label, label_from_line, is_symbol
from symboltable import SymbolTable


def strip_whitespace(line):
    line = line.strip('\n\r')
    line = line.replace(' ', '')
    line = line.replace('\t', '')
    return line


def stripped(lines):
    for line in lines:
        yield strip_whitespace(line)


def comments_stripped(lines):
    # Remove comments
    for line in lines:
        split_comments = line.split('//')
        yield split_comments[0]


def without_blanks(lines):
    for line in lines:
        if line:
            yield line


def parse(assembly_file, symbol_table):
    with open(assembly_file, 'r') as raw_code:
        code = []
        addr = 0

        for line in without_blanks(comments_stripped(stripped(raw_code))):

            # Check for and store user-defined symbols
            if is_label(line):
                label = label_from_line(line)
                if is_symbol(label):
                    symbol_table.add_entry(label, addr)

            code.append(line)

            # Only increment address if line is not a label; labels
            # don't produce instructions
            if line[0] != '(':
                addr += 1

    return code


class Parser:
    """Parse an assembly program"""
    def __init__(self, assembly_file):
        """Open filestream for assembly file and prepare to parse it."""
        self.symbol_table = SymbolTable()
        self.code = parse(assembly_file, self.symbol_table)

    def set_current_command(self, command_index):
        """Set which command is being analysed currently."""
        self.current_command = self.code[command_index]

    def command_type(self):
        """Return the type of the current command."""
        command_prefixes = {'@': 'A_COMMAND', '(': 'L_COMMAND'}
        return command_prefixes.get(self.current_command[0], 'C_COMMAND')

    def c_instr_parts(self):
        """Return the specified part of self.current_command."""
        # C-commands are in the format 'dest=comp;jump', where either dest or
        # jump must be null. So there are 2 types of commands: 'dest=comp' and
        # 'comp;jump'.
        if ';' in self.current_command:
            comp, jump = self.current_command.split(';')
            dest = 'null'
        elif '=' in self.current_command:
            dest, comp = self.current_command.split('=')
            jump = 'null'
        else:
            raise ValueError("Oh dear, something has gone wrong with c_instr_parts")

        return (dest, comp, jump)

    def symbol(self):
        """Return the symbol for an A- or L-instruction."""
        if self.current_command[0] == '@':
            return self.current_command[1:]
        else:
            return self.current_command[1:-1]
