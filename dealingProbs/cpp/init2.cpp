#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main()
{
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
    int a;
    cin >> a;
    for (int i = 0; i < a; i++)
    {
        int b, c;
        cin >> b >> c;
        cout << (__gcd(c, b) == 1 ? "Finite" : "Infinite") << endl;
    }
}