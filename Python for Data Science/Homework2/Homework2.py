
# 1: Kendi isminizde bir virtual environment oluşturunuz, oluşturma esnasında python 3 kurulumu yapınız.
conda create -n Python_for_Data_Science python=3

# 2: Oluşturduğunuz environment'ı aktif ediniz.
conda activate Python_for_Data_Science

# 3: Yüklü paketleri listeleyiniz.
conda list

# 4: Environment içerisine Numpy'ın güncel versiyonunu ve Pandas'ın 1.2.1 versiyonunu indiriniz.
conda upgrade numpy
conda install pandas=1.2.1

# 5: İndirilen Numpy'ın versiyonu nedir?
- 1.22.3

# 6: Pandas'ı upgrade ediniz.
-  1.2.1

# 7: Numpy'ı environment'tan siliniz.
conda remove -n Python_for_Data_Science numpy

# 8: Seaborn ve matplotlib kütüphanesinin güncel versiyonlarını aynı anda indiriniz.
conda install seaborn matplotlib

# 9: Virtual environment içindeki kütüphaneleri versiyon bilgisi ile beraber export ediniz ve yaml dosyasını inceleyiniz.
conda env export > environment.yaml

# 10: Oluşturduğunuz environment'i siliniz. Önce environment'i deactivate ediniz.
conda deactivate 
conda env remove -n Python_for_Data_Science

