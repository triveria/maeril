# Use the official Debian image, architecture independent
FROM debian:bookworm-slim

# Set environment variables for locale
ENV LANG=C.UTF-8
ENV LC_ALL=C.UTF-8

# Prevent prompts during package installation
ENV DEBIAN_FRONTEND=noninteractive

# Switch to root user to install initial packages
USER root

# Install necessary packages
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    can-utils \
    cookiecutter \
    curl \
    git \
    iproute2 \
    iputils-ping \
    ipython3 \
    lsof \
    net-tools \
    nmap \
    python-is-python3 \
    python3-autopep8 \
    python3-docutils \
    python3-dotenv \
    python3-openpyxl \
    python3-pandas \
    python3-pip \
    python3-pytest \
    python3-venv \
    ssh \
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
RUN pip3 install --upgrade pip

# Install python packages
RUN pip3 install poetry
RUN pip3 install pyusb
RUN pip3 install python-can
RUN pip3 install cantools
RUN pip3 install gs-usb

# Add user "codespace" with UID:GID 1000:1000
RUN groupadd -g 1000 codespace && \
    useradd -m -u 1000 -g codespace -s /bin/zsh codespace && \
    echo "codespace ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers.d/codespace && \
    chmod 0440 /etc/sudoers.d/codespace

# Ensure the codespace user owns their home directory
RUN chown -R codespace:codespace /home/codespace

# Make codespace user the default user for subsequent user-specific setup
USER codespace
WORKDIR /home/codespace

# Install Oh My Zsh
RUN sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" "" --unattended

# Copy the default Zsh setup file to the custom directory with correct ownership
COPY --chown=codespace:codespace default_zsh_setup.zsh /home/codespace/.oh-my-zsh/custom/

# Set the default shell to zsh
ENV SHELL=/bin/zsh

# Install my maeril package
RUN pip3 install --upgrade git+https://github.com/triveria/maeril.git

# Add /home/codespace/.local/bin to PATH so that pip-installed packages are available
ENV PATH="/home/codespace/.local/bin:${PATH}"
