
public class maxArea {

    public static void main(String[] args) {
	// TODO Auto-generated method stub
	int[] h = new int[] { 1, 8, 6, 2, 5, 4, 8, 3, 7 };
	System.out.print(maxArea(h));
    }

    public static int maxArea(int[] height) {
	int left = 0, right = height.length - 1, max = 0, bottom = height.length - 1;
	while (left < right) {
	    int side = Math.min(height[left], height[right]);
	    max = Math.max(max, side * bottom);
	    if (height[left] < height[right]) {
		left++;
	    } else {
		right--;
	    }
	    bottom = bottom - 1;
	}
	return max;
    }

}
