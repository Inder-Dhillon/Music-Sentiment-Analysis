#! /usr/bin/env python3 

import lyricsgenius
genius = lyricsgenius.Genius("xqFZcL_RT98570ZwGsCTrAhjzheN_R8TrIS1Pgez5WVfsbCwP7HIEeNX-GOXmHE4")
artist = genius.search_artist("eminem", max_songs=3, sort="title")
print(artist.songs)

