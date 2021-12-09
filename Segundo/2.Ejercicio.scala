object Primero {
   def main(args: Array[String]) {
        print("Primero numero: ")
        var a = scala.io.StdIn.readInt()
        print("Segundo numero: ")
        var b = scala.io.StdIn.readInt()
        println("Suma: " + calculadora("+",a,b));
        println("Resta: " + calculadora("-",a,b));
        println("Multiplicacion: " + calculadora("*",a,b));
        println("Division: " + calculadora("/",a,b));
        
   }
   def calculadora(x: String, y: Int, z: Int): Int = {
        x match { 
            case "+" => ((a: Int, b:Int) => {a+b})(y,z)
            case "-" => ((a: Int, b:Int) => {a-b})(y,z)
            case "*" => ((a: Int, b:Int) => {a*b})(y,z)
            case "/" => ((a: Int, b:Int) => {a/b})(y,z)
        }
    }
}