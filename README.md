# HELLO-WORLD application

This repo contains a boiler plate application with the github actions setup to deploy on the CADS

## Create the application

Create a web application to you hearts content. ECMWF provides a range of tools and libraries to assist:

TODO: Provide links to tools and libraries

## Build and test the docker image

When you are happy with the application we need to make sure that we can build it as a DockerImage.
Ensure that you have docker and all the pre-requistes installed and running

**Build local image to test with**

```bash
docker build -t hello-world:latest .
```

**Run the local image**

```
docker run -p 8080:8501 hello-world:latest
```

In the above example we map the port used by the application (8501, default of streamlit),
to the port we will forward to port 8080 on our localhost.
The application is now accessible in your web-browser at:

```
localhost:8080
```

## Build the production version of application and push to harbor

**Create a docker build context which build images for amd and arm platforms**

```bash
docker buildx create --name my-app-ctx --platform="linux/amd64" 
# if you need to provide arm64 support include the folloing in the platform: ",linux/arm64" 
```

**Build the docker image for your app and push to harbor (e.g. eccr.ecmwf.int)**

You will need to be logged in to your harbor and have appropriate permissions to upload your image. 

```
app="app-era5-comparison"

docker buildx build \
  --tag "eccr.ecmwf.int/cads/${app}:latest" \
  --builder=my-app-ctx \
  --platform=linux/amd64\   # ,linux/arm64 \
  --push \
  "${app}/"
```

