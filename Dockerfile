# Stage 1: Build the environment with dependencies
FROM python:3-alpine AS builder

# Set working directory
WORKDIR /app

# Create a virtual environment
RUN python3 -m venv venv

# Environment variables for virtual environment
ENV VIRTUAL_ENV=/app/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Stage 2: Create the runtime environment
FROM python:3-alpine AS runner

# Set working directory
WORKDIR /app

# Copy the virtual environment from the builder stage
COPY --from=builder /app/venv venv

# Copy the application code
COPY store_world store_world
COPY mobile_store mobile_store

# Set environment variables for the virtual environment and port
ENV VIRTUAL_ENV=/app/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
ENV PORT=8000

# Expose the port
EXPOSE ${PORT}

# Run the application with Gunicorn
CMD ["gunicorn", "store_world.wsgi:application", "--bind", "0.0.0.0:${PORT}"]
