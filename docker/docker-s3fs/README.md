# Build the image

```dockerfile
docker build . -t spheres_init --build-arg BUCKET_NAME=<s3_bucket_name>
```

# run container

```dockerfile
docker run -it -e ACCESS_KEY_ID=<access_key_id> -e SECRET_ACCESS_KEY=<secret_access_key> --privileged <image_tag>
```
