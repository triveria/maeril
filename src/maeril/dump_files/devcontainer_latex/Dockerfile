# Use the TeX Live Docker image as the base image
FROM texlive/texlive:latest

# Set environment variables for locale
ENV LANG=C.UTF-8
ENV LC_ALL=C.UTF-8

# Prevent prompts during package installation
ENV DEBIAN_FRONTEND=noninteractive

# Switch to root user to install additional packages
USER root

# Install necessary packages
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    cargo \
    cookiecutter \
    curl \
    git \
    iproute2 \
    iputils-ping \
    ipython3 \
    lsof \
    net-tools \
    pdftk \
    python-is-python3 \
    python3-docutils \
    python3-dotenv \
    python3-openai \
    python3-pandas \
    python3-pip \
    python3-pytest \
    python3-tiktoken \
    python3-venv \
    sudo \
    tree \
    udev \
    vim \
    xclip \
    zsh

# Always allow root user to use pip
ENV PIP_ROOT_USER_ACTION=ignore

# Enable installation of packages via pip
ENV PIP_BREAK_SYSTEM_PACKAGES=true

# Upgrade pip
RUN pip3 install --upgrade --ignore-installed pip

# Install python packages globally
RUN pip3 install poetry
RUN pip3 install --upgrade git+https://github.com/triveria/maeril.git

# Configure the existing 'texlive' user (UID 1000)
RUN echo "texlive ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/texlive && \
    chmod 0440 /etc/sudoers.d/texlive

RUN chsh -s /bin/zsh texlive

# Make texlive user the default user
USER texlive

# Install latex formatter
RUN cargo install tex-fmt

# Install Oh My Zsh for the texlive user
RUN sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" "" --unattended

# Copy the default Zsh setup file to the custom directory with correct ownership
COPY --chown=texlive:texlive default_zsh_setup.zsh /home/texlive/.oh-my-zsh/custom/default_zsh_setup.zsh

# Set the default shell to zsh
ENV SHELL=/bin/zsh

# Add location of pip and cargo installed packages to the PATH
ENV PATH="/home/texlive/.local/bin:/home/texlive/.cargo/bin:${PATH}"
