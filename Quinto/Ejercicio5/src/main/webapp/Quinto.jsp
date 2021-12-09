<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="ISO-8859-1">
<title>Fibonacci</title>
</head>
<body>
<% 
int n = 15;
int a = 0;
int b = 1;
out.println(a);
out.println(b);
for(int i=2; i<n; i++) {
	out.println(a+b);
	int c = a+b;
	a = b;
	b = c;
}
%>
</body>
</html>