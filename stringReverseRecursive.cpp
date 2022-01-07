#include <stdio.h>
#include <iostream>
using namespace std;

void reverse(string s){
    if(s.length() == 0){
        return;
    }
    
    string s1 = s.substr(1);
    reverse(s1);
    cout<<s[0]<<" ";
} 

int main()
{
    string s = "GAURAV";
    cout<<"The String is: \n"<<s<<"\nThe Reversed String is:"<<endl;
    reverse(s);
    return 0;
}
