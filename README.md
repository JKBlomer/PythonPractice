## THE API file
### The API calls
```
- loadSecret(file_with_client_id_secret)
    returns credentials
- getAuthToken(credentials)
    returns token
- getVideosCount(token, account_number)
    returns count
- getVideos(token, account, videosCount, skip, sleepTime, limit)
    returns movieArray

```


## The Client file
include API file: <br>
    -> from api.calls import *
### To get an array of all movies
```
- open a command shell
- git clone https://github.com/LFP-Broadcasting/bc_calls.git
- cd bc_calls
- python get_ref_ids.sample.py

```



### To get a text of all sorted actors
```
- open a command shell
- git clone https://github.com/LFP-Broadcasting/bc_calls.git
- cd bc_calls
- python get_ordered_stars.sample.py
- stars get written to a file called: "stars_blHCGforGG.txt"
```