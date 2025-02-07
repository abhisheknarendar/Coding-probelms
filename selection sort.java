//Selection Sort
class Main {
    public static void main(String[] args) {
       int[] numbers = {15,13,12,56,98,9};
       
       for(int i = 0 ; i<numbers.length-1;i++){
           int min =i ;
           for(int j = i; j<numbers.length;j++){
               if(numbers[min]<numbers[j]){
                   min = j;
                   
               }
           }
               
               int temp = numbers[min];
               numbers[min] = numbers[i];
               numbers[i] = temp;
               
               
           }
           for(int k = 0;k<numbers.length;k++){
           System.out.println(numbers[k]);
       }
    }
}