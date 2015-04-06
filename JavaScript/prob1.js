// find the sum of all multiples of 3 or 5 below 1000

// simple for loop version
var totalled = 0
for (var num = 0; num < 1000; num += 1) {
    if (num % 3 == 0 || num % 5 == 0)
        totalled += num;
};

// function version
var primed = function(max_num) {
    var totalled = 0
    for (var num = 0; num < max_num; num += 1)
        if (num % 3 == 0 || num % 5 == 0)
            totalled += num;
    return totalled;
};

console.log(primed(1000));