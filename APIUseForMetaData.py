import pylast

API_KEY = "52f1eeac01ec80f4a6d2f6f6e0dbf4dd"  # this is a sample key
API_SECRET = "1d3b08c87423135eaf73541773e75ddc"

# In order to perform a write operation you need to authenticate yourself
username = "marcus1aurelius"
password_hash = pylast.md5("eren28680000.")

network = pylast.LastFMNetwork(api_key=API_KEY, api_secret=API_SECRET)
                               #username=username, password_hash=password_hash)

track = network.get_track("Iron Maiden", "The Nomad")
info = track.info
print(track)