from jovian.pythondsa import evaluate_test_cases


def lcs_dp(seq1: str, seq2: str) -> int:
    n1, n2 = len(seq1), len(seq2)
    table = [[0] * (n2 + 1) for _ in range(n1 + 1)]
    
    for i in range(n1):
        for j in range(n2):
            if seq1[i] == seq2[j]:
                table[i + 1][j + 1] = 1 + table[i][j]

            else:
                table[i + 1][j + 1] = max(table[i][j+1], table[i + 1][j])

    return table[-1][-1]


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

    evaluate_test_cases(lcs_dp, test_cases)