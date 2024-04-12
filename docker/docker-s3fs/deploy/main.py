import os

if __name__ == "__main__":
    print('Checking mount status')
    if os.path.ismount(f"s3_bucket/"):
        print(f"bucket mounted successfully :)")
    else:
        print(f"bucket not mounted :(")
    print("list s3 directories")
    print(os.listdir(f"/home/spheres/s3_bucket/"))

    print("STARTING DOCKER FINISHED BUILD")
    os.system('docker build . -t hello:latest')

    print("FINISHED BUILD")
    os.system('docker images')

    print("PUSHING IMAGE TO ECR")
    os.system('aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 704592855784.dkr.ecr.us-east-1.amazonaws.com/us-east-1-vbaranek')
    os.system('docker tag hello:latest 704592855784.dkr.ecr.us-east-1.amazonaws.com/us-east-1-vbaranek:hello')
    os.system('docker push 704592855784.dkr.ecr.us-east-1.amazonaws.com/us-east-1-vbaranek:hello')

    print("DONE")