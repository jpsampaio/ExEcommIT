from time import sleep
import urllib.request
import webbrowser
try:
    urllib.request.urlopen("http://www.pudim.com.br")
except Exception as erro:  
    print('\033[1; 31mO site Pudim não está acessível no momento.\033[m')
    er = erro  
else:  
    print('\033[1;32mConsegui acessar o site Pudim com sucesso!\033[m')
    print('Abrindo o site em 3, 2, 1...')
    sleep(3)
    webbrowser.open('http://www.pudim.com.br', new=2)