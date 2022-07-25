#include<iostream>
#include<conio.h>
#include<cstring>
using namespace std;

int main()
{
	int key,choice;
	string str1,str2;
	char dicLowerCase[27] = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'};
	char dicUpperCase[27] = {'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'};
	
	while(choice != 3)
	{
		cout<<"1. Encryption"<<endl;
		cout<<"2. Decryption"<<endl;
		cout<<"3. EXIT"<<endl;
		cout<<"Enter the choice: ";
		cin>>choice;
		fflush(stdin);
		switch(choice)
		{
			case 1:
				{
				cout<<"Enter a plain text: ";
				getline(cin,str1);
//				gets(str1);
								
				cout<<"Enter a key: ";
				cin>>key;
				
				int i=0;
				while(i<str1.length())
				{
					int j=0,flag=0;
					while(j<26)
					{
						flag = 1;
						if(str1[i] == dicLowerCase[j])
						{
							int index=(j+key)%26;
							str1[i] = dicLowerCase[index];
							break;
						}
						j++;
					}
					j=0;
					while(j<26)
					{
						flag = 1;
						if(str1[i] == dicUpperCase[j])
						{
							int index=(j+key)%26;
							str1[i] = dicUpperCase[index];
							break;
						}
						j++;
					}
					i++;
				}
				
				cout<<str1;
				break;}
				
		case 2:
		{
			cout<<"Enter a encrypted text: ";
			cin>>str1;
			
			cout<<"Enter a key: ";
			cin>>key;
			
			int i=0;
			while(i<str1.length())
			{
				int j=0,flag=0;
				
					while(dicLowerCase[j]!='\0')
					{
						flag = 1;
						if(str1[i] == dicLowerCase[j])
						{
							int index=(j-key)%26;
							str1[i] = dicLowerCase[index];
							break;
						}
						j++;
					}
					j=0;
					while(dicUpperCase[j]!='\0')
					{
						flag = 1;
						
						if(str1[i] == dicUpperCase[j])
						{
							int index=(j-key)%26;
							str1[i] = dicUpperCase[index];
							break;
						}

						j++;
					}
					i++;				
			}
			cout<<str1;
		}
			case 3:
				{
				cout<<"EXIT";
				exit(0);}
		}
	}
}
