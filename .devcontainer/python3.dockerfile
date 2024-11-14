# Use a minimal base image
FROM python:3.10-alpine

LABEL maintainer="@k33g_org"

ARG USER_NAME=${USER_NAME}

# Set environment variables
ENV LANG=en_US.UTF-8
ENV LANGUAGE=en_US.UTF-8
ENV LC_COLLATE=C
ENV LC_CTYPE=en_US.UTF-8

# Install necessary packages
RUN apk update && apk add --no-cache \
    bash \
    curl \
    wget \
    git \
    sudo \
    && rm -rf /var/cache/apk/*

# Create a new user with sudo privileges
RUN adduser -D -s /bin/bash ${USER_NAME} \
    && echo "${USER_NAME} ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

# Switch to user
USER ${USER_NAME}

# Set the working directory
WORKDIR /home/${USER_NAME}

# Create a virtual environment
RUN python3 -m venv /home/${USER_NAME}/.venv

# Add the virtual environment's bin directory to the PATH
ENV PATH="/home/${USER_NAME}/.venv/bin:$PATH"

# Add the activation command to the .bashrc file
RUN echo "source /home/${USER_NAME}/.venv/bin/activate" >> /home/${USER_NAME}/.bashrc

# Verify the Python environment
RUN /bin/bash -c "source /home/${USER_NAME}/.venv/bin/activate && python3 --version"

# Install OhMyBash
RUN bash -c "$(curl -fsSL https://raw.githubusercontent.com/ohmybash/oh-my-bash/master/tools/install.sh)"