FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY pyproject.toml .
COPY src/ ./src/
COPY tests/ ./tests/
COPY examples/ ./examples/
COPY docs/ ./docs/
COPY README.md .

ENV PYTHONPATH=/app/src

ENTRYPOINT ["python", "-m", "code_review_toolkit.cli"]
CMD ["examples/sample.py"]
