# ASSIGNMENT 2 - Wednesday, September 11th
# 1. Create an empty list called “friends”. Create a function that adds a friend to the friends list and
#     a function that removes a friend from the friends list. Both of the functions should take one parameter
#     which is the name of the person that will be added or removed.
# 2. Use the functions you created in step 1 to add 5 people to your friends list using your function.
#     Then remove two friends from your list using your remove function. If the friend is not in the list,
#     print a message that says the friend is not in the list and can’t be removed. Finally, print out your final 
#     friend list.



#Create an empty list called "friends"
Friends = ['Brad',]
#function that removes a friend from the friends list.
Friends.remove ('Brad')


#add 5 people to friends list using function
AddFriends = ('John','Mary','Joe','Mark','Sam')
Friends.extend(AddFriends)


#Remove two friends from your list using a remove function
Friends.remove('Mary')
Friends.remove('John')

# If the friend is not in the list, print a message that says friend is not in the list and can't be removed.

friend_to_remove = "Alice"
if friend_to_remove in Friends:
    friends.remove(friend_to_remove)
else:
    print("Friend is not in list and cannot be removed.")

# finally print out friends list
print(Friends)