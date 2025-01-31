
//second largest
class Main {
    public static void main(String[] args){

        int[] arr = {23,45,67,83,82};
        int largest = Integer.MIN_VALUE;
        int second_largest = Integer.MIN_VALUE;

        for(int element: arr){
            if(element>largest){
                second_largest = largest;
                largest = element;
                
            }
            else if (element > second_largest && element != largest) {  
                second_largest = element;
            }
        }
        System.out.println(second_largest);
    }
}

