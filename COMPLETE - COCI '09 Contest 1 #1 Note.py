# https://dmoj.ca/problem/coci09c1p

i = input()

temp = 0
_type = ""
final = ""

for x in i.split(" "):
    if temp:
        if final:
            if _type == final:
                answer = _type

        if int(x) - 1 == temp:
            _type = "ascending"
            if not final:
                final = "ascending"
        elif int(x) + 1 == temp:
            _type = "descending"
            if not final:
                final = "descending"
        else:
            answer = "mixed"
            break

    temp = int(x)

print(answer)