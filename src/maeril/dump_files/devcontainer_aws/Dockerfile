# Use the official Amazon Linux 2023 image
FROM amazonlinux:2023

# Set environment variables for locale
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

# Install necessary packages
RUN yum update -y && \
    yum install -y \
    git \
    vim \
    python3 \
    python3-pip \
    nodejs \
    npm \
    zsh \
    tree \
    sudo \
    lsof \
    net-tools \
    iproute \
    procps-ng

# Install required packages using pip
RUN pip3 install ipython tiktoken openai python-dotenv

# Create a new group and user with UID and GID 1000
RUN groupadd -g 1000 codespace && \
    useradd -m -u 1000 -g codespace -s /bin/zsh codespace && \
    echo "codespace ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

# Set the new user as the default user
USER codespace

# Install Oh My Zsh
RUN sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" "" --unattended

# Set the default theme to 'duellj'
RUN sed -i 's/ZSH_THEME=".*"/ZSH_THEME="duellj"/' ~/.zshrc
