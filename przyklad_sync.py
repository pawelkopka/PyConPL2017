import time


def drugie_sniadanie():
    print('zrób kanapki')
    time.sleep(2)
    return 'kanapki'


def sniadanie():
    print('włącz czajnik')
    time.sleep(2)
    print('zaparz herbatę')
    time.sleep(2)
    print('wypij herbatę')


def prysznic():
    print('prysznic zajęty')
    time.sleep(1)
    print('prysznic zajęty')
    time.sleep(1)
    print('prysznic zajęty')
    time.sleep(1)
    print('weź prysznic')


def pakowanie(*args):
    plecak = []
    plecak.append(drugie_sniadanie())
    print('spakować do plecaka', plecak)


def ubieranie():
    print('ubierz się')


start = time.time()
sniadanie()
prysznic()
pakowanie()
koniec = time.time() - start
print('Czas :', koniec)
