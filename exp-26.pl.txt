fruit_color(apple, red).
fruit_color(banana, yellow).
fruit_color(grape, purple).
fruit_color(orange, orange).
fruit_color(plum, purple).
fruit_color(strawberry, red).
fruit_color(blueberry, blue).
get_color(fruit,color):-
    fruit_color(fruit,color).
