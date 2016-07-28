# Given two strings .Print all the interleavings of the two strings. 
# Interleaving means that the if B comes after A .It should also come after A in the interleaved string. 
# ex- 
# AB and CD 
# ABCD 
# ACBD 
# ACDB 
# CABD 
# CADB 
# CDAB

def interleave(prefix,str1,str2):

	if prefix is None:
		return

	len1 = len(str1)
	len2 = len(str2)
	
	if len1 == 0:
		if len2 == 0:
			return
		else:
			print prefix+str2
			return
	else:
		if len2 == 0:
			print prefix+str1
			return

	newPrefix = prefix + str1[:1]
	interleave(newPrefix,str1[1:],str2)
	newPrefix = prefix + str2[:1]
	interleave(newPrefix,str1,str2[1:])


interleave("","AB","CD")
