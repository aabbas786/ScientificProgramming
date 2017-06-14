import string

def count_letters(s):
    """
      >>> z = count_letters('marco')
      >>> z == {'m': 1, 'a': 1, 'r': 1, 'c': 1, 'o': 1}
      True
      >>> m = count_letters('mississippi')
      >>> m == {'m': 1, 'i': 4, 's': 4, 'p': 2}
      True
      >>> result = count_letters('Jeff')
      >>> result.get('j', 0)
      1
      >>> a = count_letters('Hello world')
      >>> sorted(a)
      ['d', 'e', 'h', 'l', 'o', 'r', 'w']
      >>> a = count_letters('Hel@@lo! wo#rld')
      >>> sorted(a)
      ['d', 'e', 'h', 'l', 'o', 'r', 'w']
    """
    counts = {}
    
    for ch in s:
        if ch not in string.ascii_letters:
            continue
        ch = ch.lower()
        if ch in counts:
            counts[ch] += 1
        else:
            counts[ch] = 1
    
    return counts 


if __name__ == '__main__':
    uncreative = input("Please enter a string: ")
    result = count_letters(uncreative)

    for letter in sorted(result):
        print('\n{0}  {1}'.format(letter, result[letter]), end='') 
