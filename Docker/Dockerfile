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

# 1. Upgrade build tools
RUN pip install --no-cache-dir --upgrade pip setuptools wheel

# 2. SEPARATE STEP: Install NumPy and Cython first
RUN pip install --no-cache-dir numpy==1.24.3 cython==0.29.36

# 3. Now install gprMax
RUN pip install --no-cache-dir git+https://github.com/gprMax/gprMax.git

# 4. Install remaining dependencies
RUN pip install --no-cache-dir \
    pandas \
    matplotlib \
    tqdm \
    h5py \
    sqlalchemy

# 5. Copy files
COPY Python/main.py Python/aggregator.py Python/database.py ./
COPY user_input.in ./

RUN mkdir -p /data && chmod 777 /data

CMD ["python3", "main.py"]