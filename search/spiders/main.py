import os

url_PDOT = os.getenv(
    "URL_PDOT", "https://www.sinj.df.gov.br/sinj/Norma/60298/Lei_Complementar_803_25_04_2009.html"
)

url_LUOS = os.getenv(
    "URLS_LUOS", "https://www.sinj.df.gov.br/sinj/Norma/fdab09844f754a998dea87e64a4b4d54/Lei_Complementar_948_16_01_2019.html"
)

url_ZEE = os.getenv(
    "URL_ZEE", "https://www.sinj.df.gov.br/sinj/Norma/912a61dfc1134ffebb691aa3e864673e/Lei_6269_29_01_2019.html"
)

URL_NORMAS = ";".join([url_PDOT, url_LUOS, url_ZEE])
