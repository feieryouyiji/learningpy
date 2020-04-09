db_config = {
    "name": "psl",
    "ip": "127.0.0.1",
    "port": 1080,
}
db_config.update({"time_out": 100})
print(db_config)

items = db_config.items()
print(items)

for key, value in db_config.items():
    print(key, value)
    print("\t")
