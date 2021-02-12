#include <iostream>
#include <string>
#include <bits/stdc++.h>
using namespace std;
#include <algorithm>
typedef long long ll;
#include <cmath>
#include <list>
#include <map>
#include <set>

int main()
{
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
    int n;
    cin >> n;
    set<int, greater<int>> s;
    while (n--)
    {
        int x1, y1, x2, y2;
        cin >> x1 >> y1 >> x2 >> y2;
        for (int i = x1; i < x2; i++)
        {
            for (int j = y1; j < y2; j++)
            {
                s.insert((i, j));
            }
        }
    }
    cout << s.size();
}
