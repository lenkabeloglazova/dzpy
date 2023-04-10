a1=int(input())
a2=int(input())
a3 = int(input())


# comp = (stud1 // 2 + stud2 // 2 + stud3 // 2 + stud1 % 2 + stud2 % 2 + stud3 % 2)
# comp = -(-(stud1+stud2+stud3)//2)
comp = -((-a1//2) + (-a2//2) + (-a3//2))
print(f"наименьшее число парт, которое нужно приобрести для них {comp}")
