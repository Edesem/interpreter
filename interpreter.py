# Credit to https://ruslanspivak.com/lsbasi-part1/ for the base layer of code

# Token types
#
# EOF (end-of-file) token is used to indicate that
# there is no more input left for lexical analysis
INTEGER, PLUS, MINUS, MULTIPLY, DIVIDE, EOF = 'INTEGER', 'PLUS', 'MINUS', 'MULTIPLY', 'DIVIDE', 'EOF'


class Token(object):
    def __init__(self, type, value):
        # token type: INTEGER, PLUS, or EOF
        self.type = type
        # token value: 0, 1, 2. 3, 4, 5, 6, 7, 8, 9, '+', or None
        self.value = value

    def __str__(self):
        """String representation of the class instance.

        Examples:
            Token(INTEGER, 3)
            Token(PLUS '+')
        """
        return 'Token({type}, {value})'.format(
            type=self.type,
            value=repr(self.value)
        )

    def __repr__(self):
        return self.__str__()


class Interpreter(object):
    def __init__(self, text):
        # client string input, e.g. "3+5"
        self.text = text
        # self.pos is an index into self.text
        self.pos = 0
        # current token instance
        self.current_token = None

    def error(self):
        raise Exception('Error parsing input')

    def integer(self, current_char):
        text = self.text
        num = current_char
        prev_char = current_char
        len_of_num = 1

        if self.pos < len(text) - 1:
            next_char = text[self.pos + 1]

            # Increment characters until end of num
            while next_char.isdigit():
                num += next_char
                len_of_num += 1
                prev_char = next_char

                if self.pos + len_of_num < len(text) - 1:
                    next_char = text[self.pos + len_of_num]
                else:
                    break

        self.pos += len_of_num
        return int(num)

    def remove_white_spaces(self):
        self.text = self.text.strip()

    def get_next_token(self):
        """Lexical analyzer (also known as scanner or tokenizer)

        This method is responsible for breaking a sentence
        apart into tokens. One token at a time.
        """
        self.remove_white_spaces()

        text = self.text

        # is self.pos index past the end of the self.text ?
        # if so, then return EOF token because there is no more
        # input left to convert into tokens
        if self.pos > len(text) - 1:
            return Token(EOF, None)

        # get a character at the position self.pos and decide
        # what token to create based on the single character
        current_char = text[self.pos]

        # If there is a space, keep incrementing the next char
        while current_char.isspace() and self.pos < len(text) - 1:
            self.pos += 1
            current_char = text[self.pos]

        # if the character is a digit then convert it to
        # integer, create an INTEGER token, increment self.pos
        # index to point to the next character after the digit,
        # and return the INTEGER token
        if current_char.isdigit():
            return Token(INTEGER, self.integer(current_char))

        elif current_char == '+':
            self.pos += 1
            return Token(PLUS, current_char)
        
        elif current_char == '-':
            self.pos += 1
            return Token(MINUS, current_char)

        elif current_char == '*':
            self.pos += 1
            return Token(MULTIPLY, current_char)

        elif current_char == '/':
            self.pos += 1
            return Token(DIVIDE, current_char)

        self.error()

    def eat(self, token_type):
        # compare the current token type with the passed token
        # type and if they match then "eat" the current token
        # and assign the next token to the self.current_token,
        # otherwise raise an exception.
        if self.current_token.type == token_type:
            self.current_token = self.get_next_token()
        else:
            self.error()

    def term(self):
        self.eat(INTEGER)

    def expr(self):
        """expr -> INTEGER PLUS INTEGER"""
        # set current token to the first token taken from the input
        self.current_token = self.get_next_token()

        # we expect the current token to be a single-digit integer
        left = self.current_token
        self.eat(INTEGER)

        terms = []
        terms.append(self.current_token)
        self.term()
        
        while self.

        # we expect the current token to be a '+' token
        op = self.current_token
        if op.type == PLUS:
            self.eat(PLUS)

        elif op.type == MINUS:
            self.eat(MINUS)

        elif op.type == MULTIPLY:
            self.eat(MULTIPLY)

        elif op.type == DIVIDE:
            self.eat(DIVIDE)

        # we expect the current token to be a single-digit integer
        right = self.current_token
        self.eat(INTEGER)
        # after the above call the self.current_token is set to
        # EOF token

        # at this point INTEGER PLUS INTEGER sequence of tokens
        # has been successfully found and the method can just
        # return the result of adding two integers, thus
        # effectively interpreting client input
        if op.type == PLUS:
            result = left.value + right.value
        elif op.type == MINUS:
            result = left.value - right.value
        elif op.type == MULTIPLY:
            result = left.value * right.value
        elif op.type == DIVIDE:
            result = left.value / right.value
        return result


def main():
    while True:
        try:
            # To run under Python3 replace 'raw_input' call
            # with 'input'
            text = input('calc> ')
        except EOFError:
            break
        if not text:
            continue
        interpreter = Interpreter(text)
        result = interpreter.expr()
        print(result)


if __name__ == '__main__':
    main()