# Use the official Debian image, architecture independent
FROM debian:bookworm-slim

# Set environment variables for locale
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

# Prevent prompts during package installation
ENV DEBIAN_FRONTEND=noninteractive

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
    portaudio19-dev \
    ffmpeg

# Always allow root user to use pip
ENV PIP_ROOT_USER_ACTION=ignore

# Enable installation of packages via pip
ENV PIP_BREAK_SYSTEM_PACKAGES=true

# Upgrade pip
RUN pip3 install --upgrade pip

# Install python packages
RUN pip3 install poetry

# Add user "codespace" with UID:GID 1000:1000
RUN groupadd -g 1000 codespace && \
    useradd -m -u 1000 -g codespace -s /bin/zsh codespace && \
    echo "codespace ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers.d/codespace && \
    chmod 0440 /etc/sudoers.d/codespace

# Ensure the codespace user owns their home directory
RUN chown -R codespace:codespace /home/codespace

# Make codespace user the default user
USER codespace

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

# Install platform.io packages
USER codespace
ENV PLATFORMIO_CORE_DIR=/home/codespace/.platformio
RUN pip install platformio
RUN pio pkg install --platform espressif32 --global
RUN curl -fSL -o /home/codespace/get-platformio.py https://raw.githubusercontent.com/platformio/platformio-core-installer/master/get-platformio.py && python3 /home/codespace/get-platformio.py
RUN pio pkg install --tool platformio/framework-arduinoespressif32 --global
RUN pio pkg install --tool platformio/tool-scons --global
RUN pio pkg install --tool platformio/tool-mkspiffs --global
RUN pio pkg install --tool platformio/tool-mklittlefs --global
RUN pio pkg install --tool platformio/tool-mkfatfs --global
RUN pip install tiktoken
RUN pip install openai
RUN pip install python-dotenv
RUN pip install rpi-gpio-emu
RUN pio pkg install --library "mathieucarbou/ESPAsyncWebServer@^3.4.0" --global
RUN pio pkg install --library "mathieucarbou/AsyncTCP@^3.2.15" --global

# ESPAsyncWebServer installs AsyncTCP_RP2040W as well, which leads to compilation errors. Therefore, we need to manually uninstall it.
# RUN pio pkg uninstall --library AsyncTCP_RP2040W

USER root
RUN curl -fsSL https://raw.githubusercontent.com/platformio/platformio-core/develop/platformio/assets/system/99-platformio-udev.rules -o /etc/udev/rules.d/99-platformio-udev.rules

USER codespace
