// Infinite loop ; the program wil return error since for loop is infinite and while loop wont run after that so this is just an exampple
class Main {
    public static void main(String[] args){

        System.out.println("Infinite for loop:");
        // prints infinitely because condition is default true and no condition is given
        for(;;){
            System.out.println("Hello abhishek");


        }
        // print infinitely because condition os always true
        while (true){
           System.out.println("Hello world");

        }
    }
    
    