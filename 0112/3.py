szo1 = input("Add meg az első szót: ")
szo2 = input("Add meg a második szót: ")


if len(szo1) <= len(szo2):
    rovidebb = szo1
    hosszabb = szo2
else:
    rovidebb = szo2
    hosszabb = szo1

if rovidebb in hosszabb:
    print("A rövidebb szó szerepel a hosszabbban.")
else:
    print("A rövidebb szó nem szerepel a hosszabbban.")