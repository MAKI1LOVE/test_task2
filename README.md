# test_task2

## Dependencies
* docker-compose

## Build
* `docker-compose up`

## Test
Open terminal and run:

`curl -X 'POST' 'http://127.0.0.1:8080/users/?username=user' -H 'accept: application/json'`

Response will be:
```
{
  "uuid": "c61ab77f-7af7-4a23-b3bf-b3882a6e24b9",
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1dWlkIjoiYzYxYWI3N2YtN2FmNy00YTIzLWIzYmYtYjM4ODJhNmUyNGI5In0.sbiBgsuvriTXbmGrryIajatFqbXe__SHjly04Pcrn3c"
}
```

Copy uuid(user_uuid) and access_token and use it to send file:

```
curl -X 'POST' 'http://127.0.0.1:8080/record/?user_uuid=c61ab77f-7af7-4a23-b3bf-b3882a6e24b9&access_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1dWlkIjoiYzYxYWI3N2YtN2FmNy00YTIzLWIzYmYtYjM4ODJhNmUyNGI5In0.sbiBgsuvriTXbmGrryIajatFqbXe__SHjly04Pcrn3c' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@track1.wav;type=audio/x-wav'
```
where `track1.wav` relative path to file. Response will look like link to download file:
```
http://127.0.0.1:8080/record/?id=576c8a6b-1185-45ff-bece-eac151cdd46d&user=c61ab77f-7af7-4a23-b3bf-b3882a6e24b9
```
where `id` is record_uuid and `user` is user_uuid. To get file use given link and run:
```
curl -X 'GET' 'http://127.0.0.1:8080/record/?id=576c8a6b-1185-45ff-bece-eac151cdd46d&user=c61ab77f-7af7-4a23-b3bf-b3882a6e24b9' \
  --output track.mp3
```
where `track.mp3` output filename.