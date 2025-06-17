# Python imajını kullan
FROM python:3.11

# Çalışma dizinini ayarla
WORKDIR /app

# Bağımlılık dosyalarını kopyala
COPY requirements.txt ./

# Bağımlılıkları yükle
RUN pip install --no-cache-dir -r requirements.txt

# Jupyter Notebook dosyalarını kopyala
COPY HR_Assistant.ipynb ./

# Çalışma portunu belirle
EXPOSE 8888

# Jupyter Notebook'u başlat
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]