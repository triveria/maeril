FROM mcr.microsoft.com/devcontainers/universal:2-linux

# Prevent prompts during package installation
ENV DEBIAN_FRONTEND=noninteractive

# Switch to root user to install additional packages
USER root

# Install necessary packages
RUN apt-get update && \
    apt-get install -y \
    curl \
    python3-pip \
    python3-docutils \
    zsh \
    sudo \
    git \
    tree \
    ipython3 \
    vim \
    xclip \
    python3-dotenv \
    python3-pandas \
    python3-pytest \
    lsof \
    net-tools \
    iputils-ping \
    udev

# Install openai python package
RUN pip3 install tiktoken openai

# Always allow root user to use pip
ENV PIP_ROOT_USER_ACTION=ignore

# Enable installation of packages via pip
ENV PIP_BREAK_SYSTEM_PACKAGES=true

# Upgrade pip
RUN pip3 install --upgrade pip

# Install my maeril package
RUN pip3 install git+https://github.com/triveria/maeril.git

# Make codespace user the default user
USER codespace

# Copy the default Zsh setup file to the custom directory with correct ownership
COPY --chown=codespace:codespace default_zsh_setup.zsh /home/codespace/.oh-my-zsh/custom/

# Set the default shell to zsh
ENV SHELL=/bin/zsh

# Add /home/codespace/.local/bin to PATH so that pip installed packages are available
ENV PATH="/home/codespace/.local/bin:${PATH}"
