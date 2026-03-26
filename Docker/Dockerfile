FROM continuumio/miniconda3

ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential git libomp-dev \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /gprmax

RUN git clone --depth 1 https://github.com/gprMax/gprMax.git /opt/gprMax_src && \
    cd /opt/gprMax_src && \
    conda update -n base -c defaults conda && \
    conda install -y numpy scipy cython matplotlib tqdm h5py pandas sqlalchemy -c conda-forge && \
    pip install .

COPY Python/main.py Python/aggregator.py Python/database.py ./
COPY user_input.in ./

RUN mkdir -p /data && chmod 777 /data

RUN python3 -c "import gprMax; print('Bhai, Finally Jung Jeet Gaye!')"

CMD ["python3", "main.py"]