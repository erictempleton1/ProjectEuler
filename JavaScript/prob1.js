// find the sum of all multiples of 3 or 5 below 1000

var num_arr = []
var totalled = 0
for (var num = 0; num < 1000; num += 1) {
    if (num % 3 == 0 || num % 5 == 0)
        totalled += num;
};
