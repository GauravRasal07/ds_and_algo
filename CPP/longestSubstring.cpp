class Solution {
public:
    int lengthOfLongestSubstring(string s) {
    if(s.length()==1) 
        return 1;

    int maxLen=0,
        n=s.length();

    map<char,int> alphabets;
    map<char,int>::iterator itr;

    alphabets[s[0]]=0;

    int i=0;
    int currLen=0;
    
    while(alphabets.count(s[i])==0){
        alphabets[s[i]]=i;
        i++;
        currLen++;
    }
    
    maxLen=currLen;
    
    while(i<s.length()){
        if(alphabets.count(s[i])==0){
            alphabets[s[i]]=i;
            i++;
            currLen++;
        }
        else{
            currLen=i-alphabets[s[i]];
            i++;
        }
        maxLen=max(maxLen,currLen);
    }
    
    // for(itr=alphabets.begin();itr!=alphabets.end();itr++){
    //     cout<<itr->first<<itr->second<<endl;
    // }
    
    return maxLen;        
                
    }
                   
};