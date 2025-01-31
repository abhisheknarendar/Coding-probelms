//FizzBuzz program
import java.util.*;
class Main {
    public static void main(String[] args) {
        System.out.println("Enter number of terms");
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        ArrayList<String> list = new ArrayList<>();
        
        for(int i =1;i<=n;i++){
            if(i%3==0 &&  i%5 == 0){
                list.add("FizzBuzz");
            }
            else if(i%3==0){
                list.add("Fizz");
                //list.add((String.valueOf(i)));
            }
            else if(i%5==0){
                list.add("Buzz");
            }
            else{
                list.add(String.valueOf(i));
            }
            
        }
    System.out.println(list);
    }
}