object Cuarto {
    def calculadora(funcion: (Int, Int) => Int, a: Int, b: Int) = {
        funcion(a,b)
    }
    
    def suma(x: Int, y: Int): Int = {
        return x + y
    }
    def resta(x: Int, y: Int) : Int = {
       return x - y
    }
    def multiplicacion(x: Int, y: Int) : Int = {
        return x * y
    }
    def division(x: Int, y: Int) : Int = {
        return x / y
    }

    def main(args: Array[String]) {
        print("Primero numero: ")
        var a = scala.io.StdIn.readInt()
        print("Segundo numero: ")
        var b = scala.io.StdIn.readInt()
        println("Suma: " + calculadora(suma,a,b));
        println("Resta: " + calculadora(resta,a,b));
        println("Multiplicacion: " + calculadora(multiplicacion,a,b));
        println("Division: " + calculadora(division,a,b));
    }
}