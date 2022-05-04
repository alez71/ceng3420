count = open("count10.bin", "r");
countans = open("benchmarks/count10.bin", "r");

isa = open("isa.bin", "r");
isaans = open("benchmarks/isa.bin", "r");

swap = open("swap.bin", "r");
swapans = open("benchmarks/swap.bin", "r");
i = 1;
print("checking count.bin");
countcorrect = True;
for line in count:
    ans = countans.readline();
    if line != ans:
        countcorrect = False;
    i += 1;

i = 1;
print("checking isa.bin");
isacorrect = True;
for line in isa:
    ans = isaans.readline();
    if line != ans:
        isacorrect = False;
    i += 1;

i = 1;
print("checking swap.bin");
swapcorrect = True;
for line in swap:
    ans = swapans.readline();
    if line != ans:
        swapcorrect = False;
    i += 1;


if countcorrect and isacorrect and swapcorrect:
    print("Three file all correct");
