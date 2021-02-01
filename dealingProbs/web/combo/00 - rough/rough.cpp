#include <iostream>
#include <string>
#include <bits/stdc++.h>
using namespace std;
#include <algorithm>
typedef long long ll;
#include <cmath>
#include <list>

int main()
{
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    int a, b;
    cin >> a >> b;
    for (int i = 0; i < a; i++)
    {
        for (int j = 0; j < b; j++)
        {
            char s;
            cin >> s;
            if (s == '.')
            {
                if ((i + j) % 2 == 0)
                    cout << "B";
                else
                    cout << "W";
            }
            else
                cout << s;
        }
        cout << endl;
    }
}