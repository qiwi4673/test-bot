FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim
WORKDIR /bot
COPY pyproject.toml uv.lock /bot/
RUN uv sync --frozen --no-dev
EXPOSE 8080
COPY . /bot
CMD ["uv", "run", "main.py"]
# 30.3s