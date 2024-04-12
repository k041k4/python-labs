# Build the image

```dockerfile
docker build . -t spheres_init
```

# run container structure

```dockerfile
docker run -it -e ACCESS_KEY_ID=<access_key_id> -e SECRET_ACCESS_KEY=<secret_access_key> -e S3_ENDPOINT=<s3_endpoint> -e BUCKET_NAME=<bucket_name> --privileged <image_tag>
```

# run container example

```dockerfile
docker run -it -e ACCESS_KEY_ID=AKIA2IDIBYLUBFBMCO5A -e SECRET_ACCESS_KEY=O7x3Gl3UwGl90xqYxaTy4W1qG1YLoV0sgAl10g0V -e S3_ENDPOINT=https://s3.us-east-1.amazonaws.com -e BUCKET_NAME=us-east-1-vbaranek-spheres-containers --privileged spheres_init:latest
```
