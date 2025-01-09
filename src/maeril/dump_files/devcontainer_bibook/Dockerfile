# Use the TeX Live Docker image as the base image
FROM texlive/texlive:latest

# Prevent prompts during package installation
ENV DEBIAN_FRONTEND=noninteractive

# Switch to root user to install additional packages
USER root

# Install necessary packages
RUN apt-get update && \
    apt-get install -y \
    python3-pip \
    python3-docutils \
    python3-tiktoken \
    python3-openai \
    python3-dotenv \
    python3-pandas \
    python3-pytest \
    zsh \
    sudo \
    git \
    curl \
    tree \
    pdftk \
    ipython3 \
    vim \
    cargo \
    xclip

# Always allow root user to use pip
ENV PIP_ROOT_USER_ACTION=ignore

# Enable installation of packages via pip
ENV PIP_BREAK_SYSTEM_PACKAGES=true

# Upgrade pip
RUN pip3 install --upgrade pip

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

# Add user "codespace" with UID:GID 1000:1000
RUN groupadd -g 1000 codespace && \
    useradd -m -u 1000 -g codespace -s /bin/zsh codespace && \
    echo "codespace ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers.d/codespace && \
    chmod 0440 /etc/sudoers.d/codespace

# Ensure the codespace user owns their home directory
RUN chown -R codespace:codespace /home/codespace

# Make codespace user the default user
USER codespace

# Install latex formatter
RUN cargo install tex-fmt

# Install Oh My Zsh for the codespace user
RUN sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" "" --unattended

# Copy the default Zsh setup file to the custom directory with correct ownership
COPY --chown=codespace:codespace default_zsh_setup.zsh /home/codespace/.oh-my-zsh/custom/

# Set the default shell to zsh
ENV SHELL=/bin/zsh

# Add /home/codespace/.local/bin and /home/codespace/.cargo/bin to PATH so that pip installed packages are available
ENV PATH="/home/codespace/.local/bin:/home/codespace/.cargo/bin:${PATH}"
