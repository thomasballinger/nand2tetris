class Parser:
    """Parse an assembly program"""
    def __init__(self, assembly_file):
        """Open filestream for assembly file and prepare to parse it."""
        with open(assembly_file, 'r') as raw_code:
            code = []
            for line in raw_code:
                # Strip whitespace
                line = line.strip('\n\r')
                line = line.replace(' ', '')
                line = line.replace('\t', '')

                # Remove comments
                split_comments = line.split('//')
                line = split_comments[0]

                # Empty lines or lines with just comments will now be of zero
                # length and will be ignored
                if len(line) > 0:
                    code.append(line)

            self.code = code

    def set_current_command(self, command_index):
        """Set which command is being analysed currently."""
        self.current_command = self.code[command_index]

    def command_type(self):
        """Return the type of the current command."""
        if self.current_command[0] == '@':
            command_type = 'A_COMMAND'
        elif self.current_command[0] == '(':
            command_type = 'L_COMMAND'
        else:
            command_type = 'C_COMMAND'
            
        return command_type

    def c_instr_parts(self):
        """Return the specified part of self.current_command."""
        split_equals = self.current_command.split('=')
        split_semicolon = self.current_command.split(';')

        if len(split_semicolon) == 2:
            dest = 'null'
            comp = split_semicolon[0]
            jump = split_semicolon[1]

            return (dest, comp, jump)

        if len(split_equals) == 2:
            dest = split_equals[0]
            comp = split_equals[1]
            jump = 'null'

            return (dest, comp, jump) 
        else:
            print("Oh dear, something has gone wrong with c_instr_parts")


    def symbol(self):
        """Return the symbol for an A- or L-instruction."""
        if self.current_command[0] == '@':
            return self.current_command[1:]
        else:
            return self.current_command[1:-1]













