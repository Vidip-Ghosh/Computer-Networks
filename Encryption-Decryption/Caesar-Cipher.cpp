#include <iostream>
using namespace std;

string encrypt(string text,int key)
{
    string result = "";
    for(int i=0;i<text.length();i++)
    {
        //checking for the upper case letters
        if(isupper(text[i]))
        {
            result += char(int(text[i]+key-65)%26 + 65);
        }
        //checking for the lower case letters
        else
        {
            result += char(int(text[i]+key-97)%26 + 97);
        }
    }
    return result;
}

string decrypt(string text,int key)
{
    string result = "";
    for(int i=0;i<text.length();i++)
    {
        //checking for the upper case letters
        if(isupper(text[i]))
        {
            result += char(int(text[i]-key-65)%26 + 65);
        }
        //checking for the lower case letters 
        else
        {
            result += char(int(text[i]-key-97)%26 + 97);
        }
    }
    return result;
}

int main()
{
    string text;
    cout<<"Enter a plain text: ";
    cin>>text;
    
    int key;
    cout<<"Enter a key-shift: ";
    cin>>key;
    
    cout<<"Encrypted text: "<<text<<endl;
    cout<<"Key-shift: "<<key<<endl;
    cout<<"Decrypted text: "<<decrypt(text,key)<<endl;
}
