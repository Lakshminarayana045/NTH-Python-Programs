from pathlib import path
disk = [p for p in path('/sys/block').glob('sd[a-z]')]
disk_dict - {d.name: d.joinpath('size').read_text().strip() for d in disk}
for dev,size in disk.items():
    print(f"{'/dev/'+dev:15} {int(size)*512/1e+9:.of}G")