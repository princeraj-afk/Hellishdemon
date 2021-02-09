#include <iostream>
#include <string>
// #include <bits/stdc++.h>
using namespace std;
#include <algorithm>
typedef long long ll;
#include <cmath>
#include <list>
#include <map>

int n;
bool prime(n){
    if (n == 1)
        return false;
    for (int i = 2; i < n; i++)
    {
        if (n % i == 0)
            return false;
    }
    return true;
}

bool square(n)
{
    if ((n * *0.5) % 1 == 0)
    {
        return true;
    }
    else
    {
        return false;
    }
}

int main()
{
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
    // int n;
    // cin >> n;
    // int p;
    // for (int i = 0; i < n; i++)
    // {
    //     cin >> p;
    //     if (square(p) and prime(p * *0.5))
    //         cout << "YES";
    //     else
    //         cout << "NO";
    // }
    cout << prime(5);
    cout << prime(15);
    cout << square(3);
    cout << square(9);
}