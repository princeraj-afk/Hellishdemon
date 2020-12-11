#include <iostream>

using namespace std;

int main()
{
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
    int n, num;
    cin >> n;
    int arr[n];

    for (int i = 0; i < n; i++)
    {
        cin >> arr[i];
    }
    cin >> num;
    int index = 0;
    for (int i = 0; i < n; i++)
    {
        if (arr[i] == num)
        {
            break;
        }
        index += 1;
    }
    cout << index;
}