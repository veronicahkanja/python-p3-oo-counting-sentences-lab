#!/usr/bin/env python3
import re

class MyString:
    def __init__(self, value=""):
        self._value = ""
        self.value = value 

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if isinstance(new_value, str):
            self._value = new_value
        else:
            print("The value must be a string.")

    def is_sentence(self):
        """Returns True if the string ends with a period"""
        return self._value.endswith(".")
    
    def is_question(self):
        """Returns True if the string ends with a question mark"""
        return self._value.endswith("?")
    
    def is_exclamation(self):
        """Returns True if the string ends with an exclamation mark"""
        return self._value.endswith("!")
    
    def count_sentences(self):
        """Counts the number of sentences in the string.
        Sentences end with '.', '?', or '!'
        """
       
        sentences = re.split(r'[.!?]+', self._value)
        
        sentences = [s for s in sentences if s.strip() != ""]
        return len(sentences)
