#to move items from one list to another you first need to hve two lists, the first with the items you need to move and then a blank list to hold them. see example below 
unconfirmed_users = ['alice' , 'robert' , 'jacob' , 'kimberly', 'amy' , 'naomi']
confirmed_users = [ ]
#the while command allows items to be moved
while unconfirmed_users:
    current_user = unconfirmed_users.pop( )
    
    print ( " Varifying user: " + current_user.title( ) )
    confirmed_users.append(current_user)
    #the \n makes a new line. The append() method adds an item to the end of the list.
    print ("\nThe following users are now confirmed:" )
    for confirmed_user in confirmed_users:
        print (confirmed_user.title( ) )
