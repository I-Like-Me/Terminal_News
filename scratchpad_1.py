import terminal_api



results = terminal_api.Players("Characters_Players", '"name", "origin"')

wanted = results.get()

print(wanted)