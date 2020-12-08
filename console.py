import pdb
from models.artist import Artist
from models.album import Album

import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository


album_repository.delete_all()
artist_repository.delete_all()



david_bowie    = Artist('David Bowie')

artist_repository.save(david_bowie)

pulp           = Artist('Pulp')
the_beatles    = Artist('The Beatles')

artist_repository.save(pulp)
artist_repository.save(the_beatles)

#pdb.set_trace()
testy = artist_repository.select(the_beatles.id)
testall = artist_repository.select_all()


david_bowie.name    = 'David Bowie in his later years'
artist_repository.update(david_bowie)



#----------------------------------------



low = Album('Low', 'Art Rock', david_bowie)
his_n_hers = Album('His \n Hers', "Britpop", pulp)

album_repository.save(low)
album_repository.save(his_n_hers)