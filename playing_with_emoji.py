#!/usr/bin/env python3

str1 = input().split() #Sample input-> Morning :D I'm missing you :(
output = ""
emoji_dict = {":D":"😃", ":(":"😔"} # press windows key + . to bring up emoji set

for word in str1:
     if word in emoji_dict:
        output += emoji_dict[word] + " " 
     else:
        output += word + " "
        print(output)
