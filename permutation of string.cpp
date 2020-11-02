#include<iostream>
#include<string.h>
using namespace std;
int permutation(string s,char result[100],int a[100],int level)
{
	if(level==s.length())
	{
		for(int j=0;j<s.length();j++)
		cout<<result[j];
		cout<<"\n";
	}
	else
	{
		for(int j=0;j<s.length();j++)
		{
			if(a[j]==0)
			continue;
			else
			{
				result[level]=s[j];
				a[j]--;
				permutation(s,result,a,level+1);
				a[j]++;
			}
		}
	}
	return 0;
}
int main()
{
	string s;
	char result[100]={" "};
	cout<<"Enter string\n";
	cin>>s;
	int n=s.length();
	int a[100],level=0;
	for(int i=0;i<n;i++)
	a[i]=1;
	permutation(s,result,a,level);
	return 0;
}

