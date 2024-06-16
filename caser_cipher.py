alphabet_list=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
               'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
               'u', 'v', 'w', 'x', 'y', 'z']



def Play_again():
    print()
    option=input("Type 'yes'if you want to go again. otherwise type 'no': ").lower()
    print()
    if option=="yes":
        play()
    else:
        exit()


def encryption(user_input,shift_key):
    
    encrypted=""
    for items in user_input:
        if items==" ":
            encrypted=encrypted+" "
        else:
            position=alphabet_list.index(items)
            index=(position+shift_key)%26
            encrypted+=(alphabet_list[index]) 
    return encrypted



def decryption(user_input,shift_key):
    decrypted=""
    for items in user_input:
        if items==" ":
            decrypted=decrypted+" "
        else:
            position=alphabet_list.index(items)
            index_value=position+shift_key
            if index_value>0:
                index=(position-shift_key)%26
                decrypted+=(alphabet_list[index])
            else:
                index=(position-shift_key+26)%26
                decrypted+=(alphabet_list[index])
    return decrypted
    
    
def play():
    
    user_choice=input("Type'Encrypt'for encryptino and 'Decrypt' for decryption:").lower()
    user_input=input("Type your message: ").lower()
    shift_key=int(input("Type the shift key: "))
    
    if user_choice=="encrypt":
       cipher_text= encryption(user_input   = user_input,shift_key= shift_key)
       
       print(f"Here's is your encrypted result: {cipher_text}") 
       Play_again() 
        
    
    elif user_choice=="decrypt":
        plain_text= decryption(user_input,shift_key)
        
        print(f"Your decrypted result is: {plain_text}")
        Play_again()
        
    else:
        print("Wrong input!!! Try again")
        Play_again()
play()
        