#!/usr/bin/env python3

class MyString:
    def __init__(self, value=''):
        self.value = value
    
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, value):
        if isinstance(value, str):
            self._value = value
        else:
            print("The value must be a string.")
    
    def is_sentence(self):
        return self.value.endswith('.')
    
    def is_question(self):
        return self.value.endswith('?')
    
    def is_exclamation(self):
        return self.value.endswith('!')
    
    def count_sentences(self):
        # Replace multiple punctuation marks with a single period
        # Then split on periods and filter out empty strings
        value = self.value
        # Replace ! and ? with periods for splitting
        value = value.replace('!', '.')
        value = value.replace('?', '.')
        # Split on periods and filter out empty strings
        sentences = [s for s in value.split('.') if s.strip()]
        return len(sentences)
