def hasher(key):
    return((125*key+342)%1009)%10
def main():
    lst = [12, 56, 22, 106, 36, 72, 902, 86, 96, 62, 42]
    lst2 = [hasher(i) for i in lst]
    print(lst2)
main()
