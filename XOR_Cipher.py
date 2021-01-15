import random 
  
  
# Function to create the  random binary string 
def rand_key(p): 
    
    # Variable to store the string 
    key1 = "" 
  
    # Loop to find the string of desired length 
    for i in range(p): 
          
        # randint function to generate 0, 1 randomly and converting  he result into str 
        temp = str(random.randint(0, 1)) 
  
        # Concatenatin the random 0, 1 
        # to the final result 
        key1 += temp 
          
    return(key1) 
  
# Driver Code 



def Convert_ASC8(str):
    # Generate ASCII 8 code 
    binary_String = int(''.join(bin(ord(c)) for c in str).replace('b',''))
    binary_String_length = len(''.join(bin(ord(c)) for c in str).replace('b',''))
    print("Binary_Sring length:{}".format(binary_String_length))
    print("After ASCII -8 Conversion:{}".format(binary_String))
    
    key = int(rand_key(binary_String_length))
    key_length = len(rand_key(binary_String_length))
   
    print("Evaluated Key is:         {} \n and key length= {}".format(key,key_length))
   
    cipher_text = binary_String ^ key
    binary_code = cipher_text ^ key
    print("CipherText:{}".format(cipher_text))
    print("Retrieved Binary code:    {}".format(binary_code))
    # return (cipher_text,binary_code)

def main():
    print(Convert_ASC8("Hiallbestofluckonthetest"))
    

if __name__ == "__main__":
    main()
