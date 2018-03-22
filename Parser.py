import re


class Parser(object):

    def __init__(self):
        self.stop_words = set(line.strip() for line in open('stop_words.txt'))

    def parse_title(self, title):
        delimiters = " ", ",", ";", ".", "?", "\n", "\t", "(", ")"
        result = ""
        regex_pattern = '|'.join(map(re.escape, delimiters))
        words = re.split(regex_pattern, title)
        for word in words:
            if (word not in self.stop_words) or word is "\n":
                result += word + " "
        return result
