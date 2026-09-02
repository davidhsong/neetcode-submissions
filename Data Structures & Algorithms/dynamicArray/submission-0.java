class DynamicArray {
    private int[] arr;
    private int size;

    public DynamicArray(int capacity) {
        arr = new int[capacity];
        size = 0;
    }

    public int get(int i) {
        if (i < 0 || i >= size) {
            throw new IndexOutOfBoundsException();
        }

        return arr[i];
    }

    public void set(int i, int n) {
        if (i < 0 || i >= size) {
            throw new IndexOutOfBoundsException();
        }

        arr[i] = n;
    }

    public void pushback(int n) {
        if (size == arr.length) {
            resize();
        }

        arr[size] = n;
        size++;
    }

    public int popback() {
        if (size == 0) {
            throw new IllegalStateException("Array is empty");
        }

        int last = arr[size - 1];
        size--;

        return last;
    }

    private void resize() {
        int newCapacity = Math.max(1, arr.length * 2);
        int[] newArr = new int[newCapacity];

        for (int i = 0; i < size; i++) {
            newArr[i] = arr[i];
        }

        arr = newArr;
    }

    public int getSize() {
        return size;
    }

    public int getCapacity() {
        return arr.length;
    }
}