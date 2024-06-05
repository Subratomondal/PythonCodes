# Python program to count number of vowels,
#newlines and character in textfile
def vowel_count(str):
    count =0  # Initiating count with 0
    vowel = "aeiouAEIOU"
    for alphabates in str:
        if alphabates in vowel:
            count +=1
    print("no. of vowel:",count)
str = "subrato"
vowel_count(str)