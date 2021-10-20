FROM python:3.8-buster
RUN python -m pip install streamlit

WORKDIR /containerized
COPY ./setup.py .
COPY ./dash.py .
COPY ./savagewattage ./savagewattage

RUN python -m pip install .