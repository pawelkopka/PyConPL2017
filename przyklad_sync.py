import time


def drugie_sniadanie():
    print('zrob kanapki')
    time.sleep(2)
    return 'kanapki'


def sniadanie():
    print('włącz czajknik')
    time.sleep(2)
    print('zaparz hebatę')
    time.sleep(2)
    print('wypij herbate')


def prysznic():
    print('prysznic zajety')
    time.sleep(1)
    print('prysznic zajety')
    time.sleep(1)
    print('prysznic zajety')
    time.sleep(1)
    print('weź prysznic')


def pakowanie(*args):
    plecak = []
    plecak.append(drugie_sniadanie())
    print('spkować do plecaka', plecak)


def ubieranie():
    print('ubierz się')


start = time.time()
sniadanie()
prysznic()
pakowanie()
koniec = time.time() - start
print('Czas :', koniec)
