def lengthOfLongestSubstring(s):
        longestTillNow = ""
        current = ""

        l = len(s)

        curpos = 0
        
        while curpos < l:
            i = 0
            while i < l:
                if s[i] not in current:
                    current += s[i]
                    i += 1

                    
                else:
                    current = s[curpos + 1]
                    print("In else: ", curpos, i, current)
                    i = curpos + 1

                l1 = len(longestTillNow)
                l2 = len(current)
                
                if l1 < l2:
                    longestTillNow = current
            
            print("Longest till now: ", longestTillNow)
            curpos += 1

        # Printing the current and longest substring.
        # print("current: ", current)
        # print("longestTillNow: ", longestTillNow)      
        return len(longestTillNow)

tCases = ["abcabcbb",
"bbbbb",
"pwwkew",
"aab"
]

print("The length of the longest substring is: ", lengthOfLongestSubstring("dvdf"))

# for s in tCases:
#     print("The length of the longest substring is: ", lengthOfLongestSubstring(s))
