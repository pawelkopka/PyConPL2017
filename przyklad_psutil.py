import psutil

cpu_count = psutil.cpu_count()
print(f'mam całe {cpu_count} procesory')

cpu_precent = psutil.cpu_percent(10)
print(f'właśnie zużywam  {cpu_precent}% procesorów')

memory = psutil.virtual_memory()
print(f'pamięć wirtualna {memory}')

processes = psutil.process_iter()
for process in processes:
    if 'firefox' in process.name():
        firefox = process

print(firefox)
cpu_firefox = firefox.cpu_percent(10)
print(f'lis zjada {cpu_firefox}%')
io_firefox = firefox.io_counters()
print(f'io lisa {io_firefox}')

processes = psutil.process_iter()
for process in processes:
    if 'python' in process.name():
        python = process

print(python)
python.kill()
