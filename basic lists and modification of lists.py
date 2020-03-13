car = [ 'chevy impala' , 'dodge grand caravan' , '2020 honda civic' ] #this introduction is about items in a list.
message = "my first car was a " + car[0].title( )  + "." + " then I got a " + car[1].title( ) + " but I really want to buy " + car[2].title( )
#the first item on the list is reffered as item zero 
#to keep the string message gammatically correct spacing wthin the message qoute is manitory 
print (message)
alcohol = [ 'Jameson ' , 'Apothic Red ' , 'Apothic Dark ' , 'B53 ' , ' Crown Royal ' , 'Kraken ' ]
print (alcohol)
alcohol [ 0 ] = 'Makers Mark ' #replaces first item in list. 
print (alcohol)
alcohol = [ 'Jameson ' , 'Apothic Red ' , 'Apothic Dark ' , 'B53 ' , ' Crown Royal ' , 'Kraken ' ]
alcohol . append ( ' Makers Mark ' )
print (alcohol)
alcohol . insert ( 6, ' Scewball ' ) #insert function adds a new item to the position
print (alcohol) 
alcohol = [ 'Jameson ' , 'Apothic Red ' , 'Apothic Dark ' , 'B53 ' , ' Crown Royal ' , 'Kraken ' ]
del alcohol [ 1 ] #deletes an item form a list. To remove more then one item, each diesired item needs its own line.  
print (alcohol)
alcohol = [ 'Jameson ' , 'Apothic Red ' , 'Apothic Dark ' , 'B53 ' , ' Crown Royal ' , 'Kraken ' ]
del alcohol [ 0 ]
del alcohol [ 1 ]
del alcohol [ 2 ]
print (alcohol)
alcohol = [ 'Jameson ' , 'Apothic Red ' , 'Apothic Dark ' , 'B53 ' , ' Crown Royal ' , 'Kraken ' ]
alcohol . sort ( ) #sorts a list perminatly 
print (alcohol) 

