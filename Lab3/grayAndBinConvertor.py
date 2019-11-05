def dec_to_bin(num):
	arr = list(''.join(bin(num).split("0b")))
	
	if num < 0:
		arr.pop(0)

	if len(arr) < 8:
		arr.reverse()
		while True:
			arr.append("0")
			if len(arr) == 8:
				break
		arr.reverse()

	if num < 0:
		arr[0] = "-"

	return arr

bin_to_dec = lambda arr: int(''.join(arr),2)

# Helper function to xor two characters 
xor_c = lambda a, b: '0' if(a == b) else '1' 
  
# Helper function to flip the bit 
flip = lambda c: '1' if(c == '0') else '0'

def bin_to_gray(binary): 
	gray = ""
	gray += binary[0] 
	for i in range(1,len(binary)):
		gray += xor_c(binary[i - 1], binary[i]) 
  	
	return list(gray) 

def gray_to_bin(gray): 
	binary = ""
	binary += gray[0]   
	for i in range(1, len(gray)):
		binary += binary[i - 1] if (gray[i] == '0') else flip(binary[i - 1])  
  
	return list(binary)