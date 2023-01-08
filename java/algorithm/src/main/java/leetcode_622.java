import java.util.Arrays;

public class leetcode_622 {
}

class MyCircularQueue {

    int[] q;
    int size, length = 0, front = 0, rear = -1;

    public MyCircularQueue(int k) {
        size = k;
        q = new int[size];
    }

    public boolean enQueue(int value) {
        if (isFull()) return false;
        rear = (rear + 1) % size;
        q[rear] = value;
        length++;
        return true;
    }

    public boolean deQueue() {
        if (isEmpty()) return false;
        front = (front + 1) % size;
        length--;
        return true;
    }

    public int Front() {
        return isEmpty() ? -1 : q[front];
    }

    public int Rear() {
        return isEmpty() ? -1 : q[rear];
    }

    public boolean isEmpty() {
        return length == 0;
    }

    public boolean isFull() {
        return length == size;
    }
}
