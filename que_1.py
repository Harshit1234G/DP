"""
QUESTION 1: Write a function to find the length of the longest common subsequence between two sequences. 
E.g. Given the strings "serendipitous" and "precipitation", the longest common subsequence is "reipito" and its length is 7.

A "sequence" is a group of items with a deterministic ordering. Lists, tuples and ranges are some common sequence types in Python.

A "subsequence" is a sequence obtained by deleting zero or more elements from another sequence. For example, "edpt" is a subsequence of "serendipitous".
"""
from jovian.pythondsa import evaluate_test_cases
from functools import lru_cache

@lru_cache
def longest_common_subsequence(
        seq1: str, 
        seq2: str, 
        index1: int = 0, 
        index2: int = 0
    ) -> int:
    if index1 == len(seq1) or index2 == len(seq2):
        return 0
    
    elif seq1[index1] == seq2[index2]:
        return 1 + longest_common_subsequence(seq1, seq2, index1 + 1, index2 + 1)
    
    else:
        option1 = longest_common_subsequence(seq1, seq2, index1 + 1, index2)
        option2 = longest_common_subsequence(seq1, seq2, index1, index2 + 1)
        return max(option1, option2)
    

if __name__ == '__main__':
    test_cases = [
        {
            'input': {
                'seq1': 'serendipitous',
                'seq2': 'precipitation'
            },
            'output': 7
        },
        {
            'input': {
                'seq1': 'longest',
                'seq2': 'stone'
            },
            'output': 3
        },
        {
            'input': {
                'seq1': 'asdfwevad',
                'seq2': 'opkpoiklklj'
            },
            'output': 0
        },
        {
            'input': {
                'seq1': '',
                'seq2': 'opkpoiklklj'
            },
            'output': 0
        },
        {
            'input': {
                'seq1': '',
                'seq2': ''
            },
            'output': 0
        },
        {
            'input': {
                'seq1': 'abcdef',
                'seq2': 'badcfe'
            },
            'output': 3
        },
        {
            'input': {
                'seq1': 'absent',
                'seq2': 'best'
            },
            'output': 3
        },
        {
            'input': {
                'seq1': 'analogy',
                'seq2': 'alchemy'
            },
            'output': 3
        },
        {
            'input': {
                'seq1': 'python',
                'seq2': 'python'
            },
            'output': 6
        }
    ]

    evaluate_test_cases(longest_common_subsequence, test_cases)