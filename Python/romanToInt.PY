def romanToInt(s):
        values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        
        res = 0
        l = len(s)
        
        i = 0
        while i < l :
            if i == l-1:
                res += values[s[i]]
                i += 1

            elif s[i] == "I" and s[i+1] == "V":
                res += values["V"] - values["I"]
                i += 2
                
            elif s[i] == "I" and s[i+1] == "X":
                res += values["X"] - values["I"]
                i += 2
                 
            elif s[i] == "X" and s[i+1] == "L":
                res += values["L"] - values["X"]
                i += 2
                
            elif s[i] == "X" and s[i+1] == "C":
                res += values["C"] - values["X"]
                i += 2
                
            elif s[i] == "C" and s[i+1] == "D":
                res += values["D"] - values["C"]
                i += 2
                
            elif s[i] == "C" and s[i+1] == "M":
                res += values["M"] - values["C"]
                i += 2
                
            else:
                res += values[s[i]]
                i += 1
        
        # res += values[s[l - 1]]
                
        return res

print(romanToInt("MCMXCIV"))
