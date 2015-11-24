def longest_palindrome (s):
    return 0 if not s else max([max([k - i if s[i:k][::-1] == s[i:k] else 0
				    		    for k in range(i + 1, len(s) + 1)])
				    		    for i, c in enumerate(s)])
