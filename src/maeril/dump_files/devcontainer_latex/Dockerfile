# Use the TeX Live Docker image as the base image
FROM texlive/texlive:latest

# Set environment variables for locale
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

# Prevent prompts during package installation
ENV DEBIAN_FRONTEND=noninteractive

# Switch to root user to install additional packages
USER root

# Install necessary packages
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    curl \
    zsh \
    sudo \
    git \
    tree \
    vim \
    xclip \
    python-is-python3 \
    ipython3 \
    python3-pip \
    python3-venv \
    python3-docutils \
    python3-tiktoken \
    python3-openai \
    python3-dotenv \
    python3-pandas \
    python3-pytest \
    lsof \
    net-tools \
    iputils-ping \
    udev \
    iproute2 \
    build-essential \
    cookiecutter \
    pdftk \
    cargo \
    npm \
    sqlite3

# Always allow root user to use pip
ENV PIP_ROOT_USER_ACTION=ignore

# Enable installation of packages via pip
ENV PIP_BREAK_SYSTEM_PACKAGES=true

# Install python packages
RUN pip3 install poetry

# Install Python packages
RUN pip3 install torch --index-url https://download.pytorch.org/whl/cpu
RUN pip3 install sentence_transformers
RUN pip3 install scikit-learn
RUN pip3 install deep-translator

# Set Hugging Face home directory
ENV HF_HOME=/opt/huggingface

# Create Hugging Face cache directory and set ownership
RUN mkdir -p $HF_HOME && \
    chown -R 1000:1000 $HF_HOME

# Download the Snowflake Sentence Transformer model to the Hugging Face cache
RUN python3 -c "from sentence_transformers import SentenceTransformer; SentenceTransformer('Snowflake/snowflake-arctic-embed-l-v2.0')"

# Install my maeril package
RUN pip3 install git+https://github.com/triveria/maeril.git

# Allow texlive user to use sudo without password
RUN echo '%sudo   ALL=(ALL:ALL) NOPASSWD: ALL' > /etc/sudoers.d/99-texlive-nopasswd && \
    chmod 0440 /etc/sudoers.d/99-texlive-nopasswd

# Make texlive user the default user
USER texlive

# Install latex formatter
RUN cargo install tex-fmt

# Install Oh My Zsh for the texlive user
RUN sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" "" --unattended

# Copy the default Zsh setup file to the custom directory with correct ownership
COPY --chown=texlive:texlive default_zsh_setup.zsh /home/texlive/.oh-my-zsh/custom/

# Set the default shell to zsh
ENV SHELL=/bin/zsh

# Add /home/texlive/.local/bin and /home/texlive/.cargo/bin to PATH so that pip installed packages are available
ENV PATH="/home/texlive/.local/bin:/home/texlive/.cargo/bin:${PATH}"
