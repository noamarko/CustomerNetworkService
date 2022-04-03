# CustomerNetworkService

This service was written in Python, using fastapi framework  
[fastapi documentation](https://fastapi.tiangolo.com/)

## Installations

1. Download and install python(version 3.6 and above): https://www.python.org/downloads/

2. Install fastapi packages: `pip install fastapi`

3. Install ASGI server: `pip install "uvicorn[standard]"`

4. fastapi-pagination: `pip install fastapi-pagination`

## Run

- To run the application: `uvicorn src.app:app --reload`

The fastapi UI (much like Swagger-ui) will be available at `localhost:8000/docs`

## If encountered a problem in one of the installation phases:

1. Uninstall the package that isn't loading properly via `pip uninstall package-name`
2. Try installing the package via `python3 -m pip install package-name`

## If encountered a problem running the project

1. Try running with `python3 -m uvicorn src.app:app --reload`
