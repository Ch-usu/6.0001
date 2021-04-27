def isPalindrome(s):
    """Asume a s como una str
    devuelve True si s es un palindromo, 
    False si s no es palindromo.
    Ignora mayusculas y non-letters"""
    def toChars(s):
        s = s.lower()
        letters = ''
        for i in s:
            if i in 'abcdfghijklmnopqrstuvw':
                letters = letters + i
        return letters
    
    def palindrome(s):
        s = toChars(s)
        if(len(s)<= 1):
            return True
        else:
            return s[0] == s[-1] and palindrome(s[1:-1])
    
    return palindrome(toChars(s))
            
print(isPalindrome('balalab?'))

