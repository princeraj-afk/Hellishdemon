#include<bits/stdc++.h>
#define ll long long
using namespace std;
int main(){
    // freopen("input.txt","r",stdin);
    ll t;
    cin>>t;
    while(t--){
         ll n,s,l;
         cin>>n>>s>>l;
         if(n==2){
             cout<<s<<" "<<l<<endl;
             continue;
         }
         ll p=n-1;
        while(1){
            if((l-s)%p==0)break;
            p--; 
        }
        vector<ll>ans;
        ll d=(l-s)/p;
        int count=1;
        ans.push_back(l);
        // ans.push_back(s);
        while(ans.size()!=n){
            if(l-count*d>0)ans.push_back(l-count*d);
            else break;
            count++;
        }
        count=1;
        while(ans.size()!=n){
           ans.push_back(l+count*d);
           count++;
        }
        for(auto it:ans)cout<<it<<" ";cout<<endl;
       
    }
    return 0;
}