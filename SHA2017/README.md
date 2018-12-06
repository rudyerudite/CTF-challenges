#Stack Overflow

When we go through **stackoverflow.py** we see that a file flag.pdf has been encrypted with CTR block cipher mode of encryption.
But, the loophole here is that it's using a fixed nonce as well as a fixed counter. So, every 16 bytes of the file is encrypted 
with the same 16 bytes of the key. So we just find out which all bytes are same in every PDF and then just XOR them with their 
equivalent encrypted bytes and by this way we can get our key. Once, we get the key it just becomes a case of repeated key XOR and 
we decrypt our PDF file to get the flag!
