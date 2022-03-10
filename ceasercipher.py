'''

CEASER CIPHER PROGRAM

'''
m= input("Enter the message to be Encrypted or decrypted :" );

print("ENTER:(1 or 2) \n 1.Encryption \n2. Decryption" );

n = int(input());
result="";

if(n==1):
    k=int(input("Key value :"));
    for i in range(len(m)):
        char=m[i];
        if(char.isupper()):
            result+=chr((ord(char)+k-65)%26 +65);
        else:
            if (char.islower()):
                result+=chr((ord(char)+k-97)%26 +97);
            else:
                result+=chr((ord(char)));
    print("Encrypted Message:"+ result);
if (n==2):
    dk=int(input("Decryption Key Value:"));
    for i in range(len(m)):
        char=m[i];
        if(char.isupper()):
            result+=chr((ord(char)-dk-65)%26 +65);
        else:
            if (char.islower()):
                result+=chr((ord(char)-dk-97)%26 +97);
            else:
                result+=chr((ord(char)));
    print("Decrypted Message : "+result);
if (n>2 or n<1):
    print("[+] choose correct option [+]")
            
    

