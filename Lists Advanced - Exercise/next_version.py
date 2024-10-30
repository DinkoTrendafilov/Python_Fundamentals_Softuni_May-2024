data = input().split(".")

next_version = int("".join(data)) + 1
next_version = str(next_version)


print(*next_version, sep=".")

