import hashlib

jsonfilename = input("Enter the name of the json file: ")
sha256_hash = hashlib.sha256()
with open(jsonfilename,"rb") as f:
    # Read and update hash string value in blocks of 4K
    for byte_block in iter(lambda: f.read(4096),b""):
        sha256_hash.update(byte_block)
    print(sha256_hash.hexdigest())


  
# initializing string
str = "GeeksforGeeks"
  
# encoding GeeksforGeeks using encode()
# then sending to SHA256()
result = hashlib.sha256(str.encode())
  
# printing the equivalent hexadecimal value.
print("The hexadecimal equivalent of SHA256 is : ")
print(result.hexdigest())
  
print ("\r")