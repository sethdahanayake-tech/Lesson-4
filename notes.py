# Taking total amount as input from the user
Amount =int(input("Please Enter Amount for Withdraw :"))

# Calculating the number of notes of different denominations
note_1 = Amount//1000
note_2 = (Amount%1000)//50
note_3 = ((Amount%1000)%50)//10


print("notes of 1000 notes is" , note_1)
print("notes of 50 notes is" , note_2)
print("notes of 10 notes is" , note_3)

