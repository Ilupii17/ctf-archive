<?php
// Shuffled output from the server
$shuffled = "7F6_23Ha8:5E4N3_/e27833D4S5cNaT_1i_O46STLf3r-4AH6133bdTO5p419U0n53Rdc80F4_Lb6_65BSeWb38f86{dGTf4}eE8__SW4Dp86_4f1VNH8H_C10e7L62154";

// The nthpw you used in the GET request
$nthpw = 1; // change if you used a different count

function get_permutation($len) {
    $indices = range(0, $len - 1);
    for ($i = $len - 1; $i > 0; $i--) {
        $j = rand(0, $i);
        [$indices[$i], $indices[$j]] = [$indices[$j], $indices[$i]];
    }
    return $indices;
}

// Seed exactly like the challenge
srand(0x1337);

// Advance RNG for previous shuffles
$len = strlen($shuffled);
for ($i = 0; $i < $nthpw - 1; $i++) {
    get_permutation($len);
}

// Get the final shuffle permutation
$perm = get_permutation($len);

// Invert the permutation
$original = array_fill(0, $len, '');
for ($k = 0; $k < $len; $k++) {
    $original[$perm[$k]] = $shuffled[$k];
}

echo implode('', $original) . PHP_EOL;
