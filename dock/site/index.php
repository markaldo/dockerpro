<html>
<head>
<style>
    .card {
        width: 200px;
        height: 200px;
        display: inline-block;
        padding: 10px 10px 10px 10px;
        
    }
</style>
</head>
    <body>
        <h2>Survival Kit Shop</h2>
        <h4>Prices @ 20% discount</h4>
            <?php 
               $json = file_get_contents('http://prices');
               $cart = json_decode($json);
               foreach ($cart as $pick) {
                echo ' <div class="card">
                <img src="https://mdbcdn.b-cdn.net/img/new/standard/nature/184.webp" class="card-img-top" alt="Fissure in Sandstone" width="150" height="150"/>
                <div class="card-body">
                <h4>'.$pick->name.'</h4>
                <p>$ '.$pick->price.'.99</p>
                <a href="#!">Buy</a>
                </div>
                </div>'."\r";
                }
            ?>
        <h4>Goods running out of stock</h4>
        <ul>
            <?php
                $json = file_get_contents('http://kit');
                $carts = json_decode($json);
                foreach ($carts as $picks) {
                 echo "<li>$picks->name</li>";
                }
            ?>
        </ul>
    </body>
</html>