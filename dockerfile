FROM python:3.8.10
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /my_courses
COPY requirementss.txt /my_courses/
RUN pip install -r requirementss.txt
COPY . /my_courses/
EXPOSE 8000


CMD [ "python", "manage.py", "runserver", "0.0.0.0"]
