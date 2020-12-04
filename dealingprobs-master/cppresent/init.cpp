#include <iostream>
#include <cmath>
#include <math.h>
#include <bits/stdc++.h>
using namespace std;

int main()
{
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
    int a, m, n, s = 0, k;
    for (int i = 0; i < a; i++)
    {
        cin >> m >> n;

        for (int i = 0; i < m; i++)
        {
            cin >> k;
            s += k;
        }
    }
    if (s == n)
    {
        cout << "YES";
    }
    else
    {
        cout << "NO";
    }
}
