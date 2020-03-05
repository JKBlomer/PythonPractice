

## To run this program
- open a command shell
```bash

 git clone https://github.com/LFP-Broadcasting/bc_calls.git
 ```
 ```bash
  cd bc_calls
```



## To get an array of all movies


```bash
python get_ref_ids.sample.py # returns video list
```
 

## To get a text of all sorted actors

```bash
python get_ordered_stars.sample.py #returns a video list sorted by actors
```


## To update videos on the platform

```bash
python update_videos.sample.py #returns true once all videos are updated
```


```
HTTP/1.1 200 OK
{
    "success": true,
    "code": "blacklist.created",
    "message": "blacklist.created",
    "errors": null,
    "params": [],
    "context": null  
}
```
```
HTTP/1.1 400 Bad Request
{
    "success": false,
    "code": "blacklist.notcreated",
    "message": "",
    "context": null,
    "errors": null,
    "params": []
}
```