FROM mcr.microsoft.com/playwright:focal

WORKDIR /app

# Install Python
RUN apt-get update \
    && apt-get install -y python3.9-dev python3-pip nano \
    && python3.9 -m pip install --no-cache-dir --upgrade pip \
    && python3.9 -m pip install --no-cache-dir playwright

COPY requirements.txt /app/requirements.txt
RUN rm -rf /ms-playwright/* \
    && python3.9 -m playwright install chromium \
    && chmod -Rf 777 /ms-playwright \
    && pip install --no-cache-dir -r requirements.txt

COPY . /app
