#INPUT NILAI 
tugas = float(input("Masukan nilai Tugas: "))
uts = float(input("Masukan nilai UTS: "))
uas = float(input("Masukan nilai UAS: "))

nilai = (0.15 * tugas) + (0.35 * uts) + (0.5 * uas)

if nilai > 80:
    grade = 'A'
elif nilai > 70:
    grade = 'B'
elif nilai > 60:
    grade = 'C'
elif nilai > 50:
    grade = 'D'

if nilai > 60:
    status = 'LULUS'
else:
    status = 'TIDAK LULUS'

print('nilai akhir: %0.2f' % nilai)
print('grade: {}'.format(grade))
print('status; {}'.format(status))