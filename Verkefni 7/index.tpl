<!DOCTYPE html>
<html>
<head>
	<title></title>
</head>
<body>
	<h3>Nýskránigarform</h3>
	<form method="post" action='/donyskra' accept-charset="ISO-8859-1" id="ny">
		Notendanafn:<br>
		<input type="text" name="user" required=""><br>
		Lykilorð:<br>
		<input type="text" name="pass" required=""><br>
		Nafn:<br>
		<input type="text" name="nafn" required=""><br>
		<input type="submit" value="Nýskrá">
		<input type="reset" value="Hreinsa">
	</form>
	<hr>
	<h3>Innskráningarform:</h3>
	<form method='post' action='/doinnskra' accept-charset='ISO-8859-1' id='inn'>
		Notandanafn:<br>
		<input type="text" name="user" required><br>
		Lykilorð:<br>
		<input type="text" name="pass" required><br>
		<input type="submit" value="Innskrá">
		<input type="reset" value="Hreinsa">
	</form>

</body>
</html>