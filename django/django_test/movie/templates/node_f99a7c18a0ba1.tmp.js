<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <title>Movies App</title>
        <meta name="description" content="">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-KK94CHFLLe+nY2dmCWGMq91rCGa5gtU4mk92HdvYe+M/SXH301p5ILy+dN9+nJOZ" crossorigin="anonymous">
    </head>
    <body>
        <div class="container">
            <form action = "">
                <div class="mb-3">
                    <label class="form-label">Search for Movie:</label>
                    <input type="text" name= "searchMovie" class="form-control"/>
                </div>
                <button type="submit" class="btn btn-primary">Search</button>
            </form>
           <p>Searching for: {{ searchTerm }} </p>
            <br />
            <br />
            <h2>Join our mailing list:</h2>
            <form action="{% url 'signup' %}">
                <div class="mb-3">
                    <label for="email" class="form-label">Enter your email:</label>
                    <input type="email" class="form-control" name = "email" placeholder="name@example.com">
                </div>
                <button type="submit" class="btn-primary"> Sign Up</button>
            </form>
        </div>
    </body>
</html>