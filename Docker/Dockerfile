FROM python:3.11-slim-bullseye

ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV OMP_NUM_THREADS=4 

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    git \
    libpng-dev \
    libfreetype6-dev \
    pkg-config \
    sqlite3 \
    libsqlite3-dev \
    libomp-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /gprmax

RUN pip install --no-cache-dir --upgrade pip setuptools wheel

RUN pip install --no-cache-dir cython==0.29.36 

RUN pip install --no-cache-dir git+https://github.com/gprMax/gprMax.git

RUN pip install --no-cache-dir \
    pandas \
    matplotlib \
    tqdm \
    h5py \
    sqlalchemy

COPY Python/main.py Python/aggregator.py Python/database.py ./
COPY user_input.in ./

RUN mkdir -p /data && chmod 777 /data

CMD ["python3", "main.py"]