//program to print only the vowels

package com.example.demo;
class input{
    public static void main(String[] args){

        String s1 = "Abhishek";
         int count = 0;
        String s2 = s1.toLowerCase();
        String s3 = "";



        while(count< s1.length()){
            switch(s1.charAt(count)){
                case 'a':
                    s3 = s3 + s2.charAt(count) ;
                    break;

                case 'e':
                    s3 = s3 + s2.charAt(count);
                    break;
                case 'i':
                    s3 = s3 + s2.charAt(count);
                    break;
                case 'o':
                    s3 = s3 + s2.charAt(count);
                    break;
                case 'u':
                    s3 = s3 + s2.charAt(count);
                    break;
               

            }
            count++;
        }


        System.out.println(s3);
    }

}