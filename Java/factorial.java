public class{
  public static void main(String args[]){
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
     System.out.print("Factorial of "+n+" is = "+get_factorial(n));
  }
  public static int get_factorial(int n){
    int factorial=1;
    for(int i=1; i<=n;i++){
      factorial *= i;
    }
    return factorial;
  }

}
