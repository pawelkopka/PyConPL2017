import asyncio
import time


async def drugie_sniadanie():
    print('zrob kanapki')
    await asyncio.sleep(2)
    return 'kanapki'


async def sniadanie():
    print('włącz czajknik')
    await asyncio.sleep(2)
    print('zaparz hebatę')
    await asyncio.sleep(2)
    print('wypij herbate')


async def prysznic():
    print('prysznic zajety')
    await asyncio.sleep(1)
    print('prysznic zajety')
    await asyncio.sleep(1)
    print('prysznic zajety')
    await asyncio.sleep(1)
    print('weź prysznic')


async def pakowanie(*args):
    plecak = []
    plecak.append(await drugie_sniadanie())
    print('spkować do plecaka', plecak)


def ubieranie():
    print('ubierz się')


loop = asyncio.get_event_loop()
start = time.time()
loop.run_until_complete(asyncio.gather(sniadanie(),
                                       prysznic(),
                                       pakowanie()))
koniec = time.time() - start
print('Czas :', koniec)
