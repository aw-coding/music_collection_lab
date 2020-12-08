from models.artist import Artist


import repositories.artist_repository as artist_repository



artist_repository.delete_all()


david_bowie    = Artist('David Bowie')

artist_repository.save(david_bowie)

pulp           = Artist('Pulp')
the_beatles    = Artist('The Beatles')

artist_repository.save(pulp)
artist_repository.save(the_beatles)