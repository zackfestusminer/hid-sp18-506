FROM ubuntu:16.04
MAINTAINER Ravinder Lambadi <rlambadi@iu.edu>

RUN apt-get update -q && apt-get install -qy \
 build-essential \
    python-dev \
    python-pip \
    libssl-dev \
    zlib1g-dev \
    libbz2-dev \
    libreadline-dev \
    libsqlite3-dev \
    pandoc \
    wget \
    curl \
    emacs \
    git-core \
    default-jre \
software-properties-common -y

RUN git clone git://github.com/yyuu/pyenv.git .pyenv
RUN git clone https://github.com/yyuu/pyenv-virtualenv.git ~/.pyenv/plugins/pyenv-virtualenv

ENV HOME  /
ENV PYENV_ROOT /.pyenv
ENV PATH $PYENV_ROOT/shims:$PYENV_ROOT/bin:$PATH

RUN pyenv install 2.7.14
RUN pyenv install 3.6.4
RUN pyenv global 3.6.4
RUN python -m ensurepip
RUN pip install PyMySQL

RUN git clone https://github.com/cloudmesh-community/hid-sp18-514.git

WORKDIR hid-sp18-514/swagger

RUN wget http://central.maven.org/maven2/io/swagger/swagger-codegen-cli/2.3.1/swagger-codegen-cli-2.3.1.jar -O swagger-codegen-cli.jar
RUN java -jar swagger-codegen-cli.jar generate -i sql-snp-price.yml -l python-flask -o snp -D supportPython3=true
RUN cp snpPriceFunctions.py snp/swagger_server/controllers
RUN cp config.py snp/swagger_server/controllers
RUN cp default_controller.py snp/swagger_server/controllers
RUN cd snp && pip install -r requirements.txt && python setup.py install

EXPOSE 8080

CMD cd /hid-sp18-514/swagger/snp && python -m swagger_server