FROM debian:bullseye-slim as build-image

WORKDIR /var/app

RUN apt-get update -y \
    && apt-get install --no-install-recommends -y \
        python3.9-dev \
        python3-pip \
        build-essential \
        ccache \
        clang \
        libfuse-dev \
        upx \
        patchelf \
    && python3.9 -m pip install nuitka

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN python3.9 -m nuitka --standalone \
                         --include-module=sqlalchemy.sql.default_comparator \
                         --include-data-files=data_dir/ml_model.txt=data_dir/ \
                         --include-data-files=data_dir/sample_license=data_dir/ \
                         --include-module=sqlalchemy.dialects \
                         --linux-onefile-icon=data_dir/python3.xpm \
                         sample_binary.py

FROM  debian:bullseye-slim as runtime-image
COPY --from=build-image /var/app/sample_binary.dist sample_binary.dist/
COPY --from=build-image /var/app/data_dir/sample_license sample_binary.dist/sample_license
CMD ["./sample_binary.dist/sample_binary version"]