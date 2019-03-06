const quickSort = (array) => {
    if (array.length < 2) {
        return array;
    }
    const pivot = array[0];
    const less = array.slice(1).filter(key => key <= pivot);
    const greater = array.slice(1).filter(key => key > pivot);
    return [...quickSort(less), pivot, ...quickSort(greater)]
};

console.log(quickSort([10, 5, 2, 3])); // [2, 3, 5, 10]