# army_category = int(input())

#if army_category < 1:
#    print("no army")
#elif army_category < 10:
#    print("few")
#elif army_category < 50:
#    print("pack")
#elif army_category < 500:
#    print("horde")
#elif army_category < 1000:
#    print("swarm")
#else:
#    print("legion")


def get_category_name(number):
    if number < 1:
        return "no army"
    elif number < 10:
        return "few"
    else:
        return "legion"


input_number = int(input())
print(get_category_name(input_number))
