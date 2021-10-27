str1 = "Good";  
str2 = "morning";  
   
print("Strings before swapping: " + str1 + " " + str2);  
   
#Concatenate both the string str1 and str2 and store it in str1  
str1 = str1 + str2;  
#Extract str2 from updated str1  
str2 = str1[0 : (len(str1) - len(str2))];  
#Extract str1 from updated str1  
str1 = str1[len(str2):];  
   
print("Strings after swapping: " + str1 + " " + str2);  
