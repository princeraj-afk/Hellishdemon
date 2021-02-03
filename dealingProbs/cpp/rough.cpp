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
    ll n;
    cin >> n;
    ll arr[n];
    for (int i = 0; i < n; i++)
        cin >> arr[i];
    ll sum = 0, l = 0;
    ll mx = INT_MIN;
    for (int i = 0; i < n; i++)
    {
        if (arr[i] > 0)
        {
            sum += arr[i];
            l += 1;
        }
        if (arr[i] > mx)
            mx = arr[i];
    }
    if (sum > 0)
        cout << sum << " " << l;
    else
        cout << mx << " " << 1;
}