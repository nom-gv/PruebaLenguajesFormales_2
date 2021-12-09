object Tercero {
    def main(args: Array[String]) {
        print("Ingresar Cadena: ")
        var a = scala.io.StdIn.readLine()

        var letras = a.map(lines=>lines+"")

        for (i <- 0 to letras.length-1)
            print(letras(i)+" ")
        
        println()
        
        val palabras = a.split(" ")
        for(i <- 0 to palabras.length-1)
            println(palabras(i))
    }
}