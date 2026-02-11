let number_array = [10,5,10,8,9,10,12,15]

function highest_number(number_array) {
    max_num = Math.min(...number_array)
    console.log(max_num);
}
highest_number(number_array)