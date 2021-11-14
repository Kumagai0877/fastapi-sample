FROM python:3.9-alpine
ENV PYTHONUNBUFFERED=1

WORKDIR /api/

#COPY ./pyproject.toml ./poetry.lock ./
#RUN pip install poetry
#RUN poetry config virtualenvs.in-project true
#RUN poetry install
#
#ENV PATH=/app/.venv/bin:$PATH
#
#ENTRYPOINT ["poetry", "run", "uvicorn", "src.main:app", "--host", "0.0.0.0", "--reload"]

COPY requirements.txt ./
RUN pip install --trusted-host pypi.python.org -r requirements.txt

CMD ["uvicorn", "src.main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]