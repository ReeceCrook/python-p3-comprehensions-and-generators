#!/usr/bin/env python3

def return_evens(num_list):
    evens = [number for number in num_list if (number / 2).is_integer()]
    return evens

def make_exclamation(sentence_list):
    new_list = [f"{sentence}!" for sentence in sentence_list]
    return new_list