FROM python:3.7.3
COPY . /build/
WORKDIR /build/
RUN pip install -r requirements.txt
RUN pelican content -s publishconf.py

FROM nginx
COPY --from=0 /build/output/ /usr/share/nginx/html/
