FROM python:3.11-slim-bullseye

ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential git libpng-dev libfreetype6-dev pkg-config \
    sqlite3 libsqlite3-dev libomp-dev \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /gprmax

RUN pip install --no-cache-dir --upgrade pip setuptools wheel
RUN pip install --no-cache-dir \
    numpy==1.24.3 \
    cython==0.29.36 \
    scipy \
    scikit-learn \
    pandas \
    matplotlib \
    tqdm \
    h5py \
    sqlalchemy

RUN git clone --depth 1 https://github.com/gprMax/gprMax.git /opt/gprMax_src
ENV PYTHONPATH="/opt/gprMax_src:${PYTHONPATH}"

COPY Python/main.py Python/aggregator.py Python/database.py ./
COPY user_input.in ./

RUN mkdir -p /data && chmod 777 /data

RUN python3 -c "import sys; sys.path.append('/opt/gprMax_src'); import gprMax; print('Bhai, Jung Jeet Gaye!')"

CMD ["python3", "main.py"]