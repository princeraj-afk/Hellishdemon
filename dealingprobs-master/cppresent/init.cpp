#include <iostream>
// #include <cmath>
// #include <math.h>
// #include <string.h>
#include <bits/stdc++.h>
using namespace std;

string reverseWord(string k)
{
    //Your code here
    int p;
    p = k.length();
    string ans = "";
    for (int i = p - 1; i >= 0; i--)
    {
        ans += k[i];
    }
    return ans;
}

int main()
{
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
    string a;
    cin >> a;
    cout << reverseWord(a);
}