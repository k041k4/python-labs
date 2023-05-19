FROM python:3.11-slim
LABEL platform_name="spheres"

#container environment
ENV LANG=C.UTF-8
ENV PORT=3000
EXPOSE 3000

# container content
WORKDIR /spheres

# dependencies
COPY . .
RUN pip install -r requirements.txt

# execute app
ENTRYPOINT ["python","/spheres/deploy/hello_world.py"]