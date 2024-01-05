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

The actions in this repository are set up to build the docker image and push to harbor ready for deployment
on the CDS. The build and push actions use the following secrets and variables:

- secrets.HARBOR_USERNAME (Organisation secret with credentials for harbor)
- secrets.HARBOR_PASSWORD (Organisation secret with credentials for harbor)
- github.event.repository.name (repo name, that is used as the directory in harbor)
- $APP_PATH (When JS app, this is applied at build time to ensure that the app has correct build path)


