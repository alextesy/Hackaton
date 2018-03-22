def is_valid_number(token):
    percent_symbol_flag = False
    fraction_flag = False
    number_of_dots = 0

    two_last_char = token[-2:]
    # one_last_char = two_last_char[-1:]

    if two_last_char == "bn":
        token = token[:-2]
        for c in token:
            is_numeric_number = c.isnumeric()
            is_punctuation = False
            if c == '.' or c == ',' or c == '%' or c == '/':
                is_punctuation = True
                if c == '.':
                    number_of_dots += 1
            if (not is_numeric_number) and (not is_punctuation):
                return False

        if number_of_dots > 1:
            return False
        else:
            return True

    else:
        for c in token:
            if c == '%':
                percent_symbol_flag = True
            elif c == '/':
                fraction_flag = True
            is_numeric_number = c.isnumeric()
            is_punctuation = False
            if c == '.' or c == ',' or c == '%' or c == '/':
                is_punctuation = True
                if c == '.':
                    number_of_dots += 1
            if (not is_numeric_number) and (not is_punctuation):
                return False

        if number_of_dots > 1:
            return False
        if percent_symbol_flag:
            i = 0
            while i < (len(token) - 1):
                if token[i] == '%':
                    return False
                i += 1

        if fraction_flag:
            fraction_list = token.split('/')
            if not fraction_list[1].isnumeric():
                return False
            if len(fraction_list) != 2:
                return False

    return True


class Parser(object):

    def __init__(self):
        self.stop_words = set(line.strip() for line in open('stop_words.txt'))
        self.punctuations_set = {'[', '(', '{', '`', ')', '<', '|', '&', '~', '+', '^', '@', '*', '?', '$', '.',
                                 '>', ';', '_', '\'', ':', ']', '/', '\\', "}", '!', '=', '#', ',', '\"', '-'}

    def parse_title(self, title):
        title = title.replace('-', ' ')
        title = title.split()
        index = 0
        index_last_word = len(title) - 1
        result = ""

        while index < index_last_word + 1:
            word = self.clean_token(title[index])
            word_length = len(word)

            if word_length > 0:  # check if the word is not empty
                if (word not in self.stop_words) or word in "\n":
                    result += word + " "

            index += 1

        return result

    def clean_token(self, token):
        token_length = len(token)
        while (token_length > 0) and token[0] in self.punctuations_set:
            token = token[1:]
            token_length -= 1

        while (token_length > 1) and token[token_length - 1] in self.punctuations_set:
            token = token[:-1]
            token_length -= 1

        return token
