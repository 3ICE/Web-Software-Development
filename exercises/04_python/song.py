import json

class Song:
	def __init__(self, path):
		#TRAHQDQ128F421F629.json is found in lastfm_subset/A/H/Q/
		self._data={}
		try:
			with open(
				'lastfm_subset/'+
				path[2:-15]+'/'+
				path[3:-14]+'/'+
				path[4:-13]+'/'+
				path+'.json') as json_file:
					self._data = json.load(json_file)
		except FileNotFoundError:
			self._data["artist"]="file"
			self._data["title"]="not found"
			self._data["timestamp"]="-1"
			self._data["track_id"]=path
			self._data["tags"]=[]
			self._data["similars"]=[]

	@property
	def artist(self):
		return self._data["artist"]

	@property
	def title(self):
		return self._data["title"]

	@property
	def timestamp(self):
		return self._data["timestamp"]

	@property
	def track_id(self):
		return self._data["track_id"]

	@property
	def tags(self):
		return self._data["tags"]

	@property
	def similars(self):
		return self._data["similars"]

	def get_tags(self, limit=0):
		#return a list of tags in the song that are equal or higher than the limit given
		#The limit is optional and should default to 0 (i.e. get all tags)
		#it should only return the tag names in the list.
		ret=[]
		for i in range(len(self._data["tags"])):
			if int(self._data["tags"][i][1])>=limit:
				ret.append(self._data["tags"][i][0])
		return ret

	def get_similars(self, limit=0):
		#return a list of track ids in the song that are equal or higher than the limit given. The limit is optional and should default to 0 (i.e. get all similar songs).
		ret=[]
		for i in range(len(self._data["similars"])):
			if int(self._data["similars"][i][1])>=limit:
				ret.append(self._data["similars"][i][0])
		return ret

	def shared_tags(self, other_song_instance):
		return set(self.get_tags()) & set(other_song_instance.get_tags())

	def combined_tags(self, other_song_instance):
		return set(self.get_tags()) | set(other_song_instance.get_tags())

#some_song = Song('TRAWHKS128F9330619') # create a new Song instance some_song

#print(some_song.artist)
#print(some_song.title)
#print(some_song.timestamp)
#print(some_song.track_id)
#print(some_song.tags)
#print(some_song.similars)

# Get all the tags for the song ['piano', 'Piano - pleasant']
#print(some_song.get_tags())
#some_song.get_tags(90) # Get subset of tags based on their score ['piano']
# Get all the track_ids of similar songs ['TRZKEHI128F93306C7', 'TRLNBWD128E0783584', ... 45 track_ids ..., 'TRMFVJD128F4258DCC']
#print(some_song.get_similars())
# Get similar track_ids that are at least 0.90 similar ['TRZKEHI128F93306C7']
#print(some_song.get_similars(0.9))
#other_song = Song('TRANXZZ128F4230613') # create another Song instance
# Get all tags for this song ['piano', 'new age', 'relaxing', 'beautiful']
#print(other_song.get_tags())
# Find out what tags these both songs have ('piano',)
#print(other_song.shared_tags(some_song))
# Find out the combined tags of these both ('new age', 'beautiful', 'relaxing', 'piano', 'Piano - pleasant')
#print(other_song.combined_tags(some_song))