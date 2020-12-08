#include <iostream>
#include <cmath>
#include <math.h>
#include <bits/stdc++.h>
using namespace std;

int hexToDecimal(char a, int b)
{
    int ans = 0;
    int counter = pow(16, a - 1);
    for (int i = 0; i < b; i++)
    {
        if (a[i] >= "0" && a[i] <= "9")
        {
            ans += counter * int(a[i]);
        }
        else if (a[i] >= "A" && a[i] <= "F")
        {
            ans += counter * (10 + int(a[i] - "A"));
        }
        counter /= 16;
    }
    return ans;
}

int main()
{
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
    char a;
    int b;
    cin >> a >> b;
    cout << hexToDecimal(a, b);
    return 0;
}