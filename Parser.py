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
        print('.' in self.punctuations_set)
        while (token_length > 0) and token[0] in self.punctuations_set:
            token = token[1:]
            token_length -= 1

        while (token_length > 1) and token[token_length - 1] in self.punctuations_set:
            token = token[:-1]
            token_length -= 1

        return token
