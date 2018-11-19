<!DOCTYPE html>
<html lang="is">
<head>
	<meta charset="utf-8">
	<title>Members</title>
	<style type="text/css">
		body{
			background-color: lightblue;
			margin: 3em;
		}

		h2{
			color: #a00;
		}
	</style>
</head>
<body>
	<h2>Félagskrá</h2>
	<p>Meðlimirnir eru:</p>
	<table border="1">
	%for row in rows:
		<tr>
		%for col in row:
			<td>{{col}}</td>
		%end
		</tr>
	%end
	</table>
	<a href="/">Til baka</a>
</body>
</html>
