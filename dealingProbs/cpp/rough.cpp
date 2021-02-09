#include <iostream>
#include <string>
// #include <bits/stdc++.h>
using namespace std;
#include <algorithm>
typedef long long ll;
#include <cmath>
#include <list>
#include <map>

bool prime(int n)
{
    if (n == 1)
    {
        return false;
    }
    for (int i = 2; i < n; i++)
    {
        if (n % i == 0)
            return false;
    }
    return true;
}
bool square(int n)
{
    if (pow(sqrt(n), 2) == n)
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
    // #ifndef ONLINE_JUDGE
    //     freopen("input.txt", "r", stdin);
    //     freopen("output.txt", "w", stdout);
    // #endif
    int n;
    cin >> n;
    int p;
    for (int i = 0; i < n; i++)
    {
        cin >> p;
        if (square(p) && prime(sqrt(p)))
            cout << "YES\n";
        else
            cout << "NO\n";
    }
}