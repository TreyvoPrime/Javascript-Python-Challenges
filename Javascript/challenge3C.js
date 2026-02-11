
let vowels = "aeiou";
word = "greetings gurt"
function vowel_detector(vowels) {
    let number_vowels = 0
    for (let v of word) {
        if (vowels.includes(v)) {
            number_vowels = number_vowels + 1;
        }
    }
    console.log(number_vowels);
}
vowel_detector(vowels)