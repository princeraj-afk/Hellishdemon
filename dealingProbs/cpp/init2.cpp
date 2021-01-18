#include <iostream>
#include <string>
#include <string.h>
#include <bits/stdc++.h>
using namespace std;

int main()
{
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
    int a, ans = 0, li = 0;
    cin >> a;
    int arr[a];
    int min = INT_MAX;
    for (int i = 0; i < a; i++)
    {
        cin >> arr[i];
        if (arr[i] <= min)
        {
            min = arr[i];
            li = i;
        }
        ans = i - li;
    }
    cout << ans;
}