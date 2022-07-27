#include<bits/stdc++.h>
#define limit 1000000
using namespace std;

long long a[limit+10];

void precalculate()
{
    //adding f(n) for every a[n]
    for(int i=2; i<=limit; i++)
    {
       //i is to be added for every multiple of i greater than i starting from 2i
       for(int j = 2*i; j<= limit; j+=i)
       {
           a[j] += i;
       }
       //As 1 is to be added for every f(n)
       a[i] += 1;
    }
    //Adding a[n-1] for every a[n]
    for(int i = 2; i<=limit; i++)
        a[i] += a[i-1];
}

int main ()
{
    precalculate();
    int T;
    scanf("%d",&T);
    for(int i=1; i<=T; i++)
    {
        int d;
        scanf("%d",&d);
        printf("%lld\n",a[d]);
    }
    return 0;
}