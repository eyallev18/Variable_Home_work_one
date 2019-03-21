"""
This is virtual song only for the Exercise
written by Eyal Lev
Date March 21st 2019
"""

Name = "My First Exercise"                          # The name of the song
AuthorFirstName , AuthorLastName = "Jhon" , "Martin"   # The Name of the Author
Genre = "Eastern"                                     # The Genere of the Song
SongNumbeOfWords = 97                                  # The Number of Word in the Song
NumberOfDifferentWords = 72                            # The Number of different Words
SongPlayDuration = 4.36                                # Song Play duration
NumberOfKids= 4                                        # Author number of kids
FirstSon, SecondDaughter, ThirdDaughter, YoungestSon = "Gim", "Shelly", "Rebeca", "Mark"      # Author kids name
AuthorEifeName= "Lisa"                                                                        # Author wife's name

print ('The Author of : "' + Name+ '"  Song is: ' + AuthorFirstName +" "+ AuthorLastName)
print ('The Song:"'+ Name+ '" has ',SongNumbeOfWords , " Words.")
print ('The song has ',NumberOfDifferentWords," different words and ", SongNumbeOfWords-NumberOfDifferentWords," twice or more repeated words.")
print ('The song play duration is: ',SongPlayDuration, ' minutes. ')
print ('The Avenge play for word is: ',(4.36*60/97)," Second.")
print ('More about The Author:')
print ("The Author's wife name is: "+ AuthorEifeName+ " and he has ",NumberOfKids," Kids ,The Names are "+ FirstSon+","+ SecondDaughter+"," +ThirdDaughter + " and "+ YoungestSon+".")

