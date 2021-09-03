FROM python:3.9 as build
COPY requirements.txt .
RUN pip install --user -r requirements.txt

FROM python:3.9-slim
WORKDIR /bot
COPY --from=build /root/.local /root/.local
COPY . .
ENV PATH=/root/.local:$PATH
RUN apt-get update \
    && apt-get install -y ffmpeg
CMD ["python", "app/pup.py"]
