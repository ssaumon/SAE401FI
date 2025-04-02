FROM ubuntu
RUN apt update && apt upgrade -y
RUN apt install -y python3 python3-pip python3-venv python3-flask
WORKDIR /app
COPY ImportSBOM.py ImportSBOM.py
COPY base_de_donnees_sbom.json base_de_donnees_sbom.json
ENV FLASK_APP=ImportSBOM.py
ENV FLASK_ENV=development
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0", "--port=5000"]
